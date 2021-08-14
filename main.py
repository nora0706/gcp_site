# [START gae_python39_app]
# [START gae_python3_app]
import os
from datetime import datetime
from flask import Flask
from google.cloud import secretmanager



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

@app.route('/health')
def health():
    return 'I am healty!'


@app.route('/secret')
def secret():
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
    # Build the parent name from the project.
    name = f"projects/{project_id}/secrets/test/versions/latest"

    # Access the secret version.
    response = client.access_secret_version(request={"name": name})

    # Print the secret payload.
    #
    # WARNING: Do not print the secret in a production environment - this
    # snippet is showing how to access the secret material.
    payload = response.payload.data.decode("UTF-8")
    return str(payload)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8082, debug=True)
# [END gae_python3_app]
# [END gae_python39_app]
