import os
from google.cloud import secretmanager

class Secret:
    def __init__(self):
        # Create the Secret Manager client.
        self.client = secretmanager.SecretManagerServiceClient()

        self.project_id = os.getenv('GOOGLE_CLOUD_PROJECT')

    def get_secret(self, secret_id):
        # Build the parent name from the project.
        name = f"projects/{self.project_id}/secrets/{secret_id}/versions/latest"

        # Access the secret version.
        response = self.client.access_secret_version(request={"name": name})

        # Print the secret payload.
        #
        # WARNING: Do not print the secret in a production environment - this
        # snippet is showing how to access the secret material.
        return response.payload.data.decode("UTF-8")
