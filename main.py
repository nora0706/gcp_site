# [START gae_python39_app]
# [START gae_python3_app]
from datetime import datetime
from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/<name>')
def helloName(name = 'World'):
    """Return a friendly HTTP greeting."""
    return str(datetime.now())+'<br /><h1>Hello ' + str(name) + '!</h1>'


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8082, debug=True)
# [END gae_python3_app]
# [END gae_python39_app]
