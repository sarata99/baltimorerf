from flask import Flask
from flask import Flask, render_template, json, current_app as app
import os

app = Flask(__name__)



@app.route('/map')
def map():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static', 'data', 'map.json')
    f = open(json_url)
    data = json.load(f)
    return render_template('map.html', jsonn=data)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/volunteer')
def volunteer():
    return render_template('calendar.html')


@app.route('/how_to')
def how():
    return render_template('how.html')

if __name__ == "__main__":
    app.run(port=5000)