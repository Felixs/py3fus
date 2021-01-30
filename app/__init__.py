# This file initializes your application and brings together all of the various components.
import os
from flask import Flask, render_template, g, request
from app.db import get_all_url_info, get_url_info

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, template_folder='./templates', static_folder='./static')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'py3fus.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/s/<short_url>')
    def short_url(short_url):
        if short_url is not None and len(short_url) > 0:
            db_data = get_url_info(short_url)
            if db_data is not None:
                return render_template('redirect.html', short_url=short_url, long_url=db_data[2])
        
        return render_template('unknown_url.html', short_url=short_url)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html', url=request.path), 404

    from . import db
    db.init_app(app)

    return app




