from google.oauth2 import service_account
from dataclasses import dataclass, asdict


@dataclass
class ServiceAccountJson:
    type: str
    project_id: str
    private_key_id: str
    private_key: str
    client_email: str
    client_id: str
    auth_uri: str
    token_uri: str
    auth_provider_x509_cert_url: str
    client_x509_cert_url: str
    universe_domain: str


class BigQueryAuth:
    """
    Class to generate credentials object from the service account key information (json data)
    """

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.credentials = self.__generate_credentials()

    def __generate_credentials(self):
        """
        Method to generate credentials object from service account object
        """
        service_json_object = ServiceAccountJson(**self.kwargs)
        credentials = service_account.Credentials.from_service_account_info(asdict(service_json_object))
        return credentials

    def get_credentials(self):
        """
        Getter Method to return credentials object generated from service account information.
        """
        return self.credentials
