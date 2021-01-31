import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def get_all_url_info():
    return get_db().execute(
            'SELECT * FROM urls',
        ).fetchall()

def get_url_info(short_url):
    return get_db().execute('SELECT * FROM urls WHERE short = ? AND active = 1', (short_url, )).fetchone()

def create_short_url(short_url, long_url, valid_until=0):
    db = get_db()
    db.execute('INSERT INTO "main"."urls" ("short", "long", "valid_until") VALUES (?, ?, ?)', (short_url, long_url, valid_until))
    db.commit()
