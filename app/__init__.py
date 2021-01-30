# This file initializes your application and brings together all of the various components.
from flask import Flask

app = Flask('Py3fus - simple url shortener')

@app.route('/')
def hello_world():
    # load template to create new short url
    return 'Py3fus - simple url shortener by FelixS'

@app.route('/s/<short_handel>')
def short_url_handel(short_handel):
    if short_handel is None or len(short_handel) <= 0:
        abort(404)
    # if short_handel in db:
    # create template with redirect
    # else abort(404)
    return f'Got short route {short_handel}'

@app.errorhandler(404)
def page_not_found(error):
    # create redirect to homepage
    return "404 - Page not found", 404
    #return render_template('404.html', title = '404'), 404


