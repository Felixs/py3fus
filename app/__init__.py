# This file initializes your application and brings together all of
# the various components.
import os
from flask import Flask, render_template, request, redirect, url_for, session
from . import name_generator
from . import db
import validators


def create_app(test_config=None):
    ''' factory fuction to create app with flask run '''
    app = Flask(__name__, instance_relative_config=True,
                template_folder='./templates', static_folder='./static')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'py3fus.sqlite'),
        WORD_DICT='german_dict.txt'
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
        ''' websites index page '''
        return render_template('index.html')

    @app.route('/admin', methods=('GET', 'POST'))
    def admin():
        ''' admin panel page'''
        if request.method == 'POST':
            session['authtoken'] = request.form.get('authtoken')

        # TODO: make auth token dynamic at startup or save to db?
        if 'authtoken' not in session or session['authtoken'] != 'testtoken':
            return render_template('admin_auth.html')

        url_list = db.get_all_url_info()
        return render_template('admin.html', url_list=url_list)

    @app.route('/created', methods=('GET', 'POST'))
    def create():
        ''' displays infos about created short list'''
        print(request.method)
        if request.method != 'POST':
            return redirect(url_for('index'))

        long_url = request.form.get('long_url')
        if validators.url(long_url) != True:
            return render_template('not-created.html', long_url=long_url, message='Input given is not an URL!')

        short_url = name_generator.generate_short_url_name()
        db.create_short_url(short_url, long_url)
        return render_template('created.html', short_url=short_url)

    @app.route('/s/<string:short_url>')
    def short_url(short_url):
        ''' redirect page '''
        if short_url is not None and len(short_url) > 0:
            db_data = db.get_url_info(short_url)
            if db_data is not None:
                return render_template('redirect.html', short_url=short_url, long_url=db_data[1])

        return render_template('unknown_url.html', short_url=short_url)

    @app.errorhandler(404)
    def page_not_found(error):
        ''' error handler page'''
        return render_template('404.html', url=request.path), 404

    # Init-routines
    db.init_app(app)

    return app
