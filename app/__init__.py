# This file initializes your application and brings together all of the various components.
from flask import Flask, render_template

app = Flask(__name__, template_folder='./templates', static_folder='./static')

@app.route('/')
def hello_world():
    # load template to create new short url
    return render_template('index.html', title = 'Welcome', content = 'Welcome to Py3fus!')

@app.route('/s/<short_handel>')
def short_url_handel(short_handel):
    if short_handel is None or len(short_handel) <= 0:
        abort(404)
    # if short_handel in db:
    # create template with redirect
    # else abort(404)
    return render_template('short_url_handel.html', title='Redirecting', short_handel=short_handel)
    return f'Got short route {short_handel}'

@app.errorhandler(404)
def page_not_found(error):
    # create redirect to homepage
    return "404 - Page not found", 404
    #return render_template('404.html', title = '404'), 404


