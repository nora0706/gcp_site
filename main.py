# [START gae_python39_app]
# [START gae_python3_app]
from datetime import datetime
from flask import Flask, render_template
from google.cloud import secretmanager

from database import MySQL
from secret import Secret


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__, template_folder='template')
gsecret = Secret()

dns = {
    'user': gsecret.get_secret('DB_USER'),
    'host': gsecret.get_secret('DB_HOST'),
    'password': gsecret.get_secret('DB_PASS'),
    'database': 'testdb'
}
db = MySQL(**dns)


@app.route('/dogs')
def dogs():
    props = {'title': 'Dog List', 'msg': 'Dogs List'}
    stmt = 'SELECT * FROM dog;'
    dogs = db.query(stmt)
    html = render_template('dogs.html', props=props, dogs=dogs)
    return html


@app.route('/dog/<int:id>')
def dog(id):
    props = {'title': 'Dog Information', 'msg': 'Dog Information'}
    stmt = 'SELECT * FROM dog WHERE id = ?;'
    dog = db.query(stmt, id, prepared=True)
    html = render_template('dog.html', props=props, dog=dog[0])
    return html


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/<name>')
def helloName(name = 'World'):
    """Return a friendly HTTP greeting."""
    return str(datetime.now())+'<br /><h1>Hello ' + str(name) + '!</h1>'

@app.route('/health')
def health():
    return 'I am healty!'


@app.route('/secret')
def secret():
    payload = gsecret.get_secret('test')
    return str(payload)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8082, debug=True)
# [END gae_python3_app]
# [END gae_python39_app]
