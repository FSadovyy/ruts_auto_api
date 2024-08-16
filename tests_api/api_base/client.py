import requests
from requests import Response


class Client:
    @staticmethod
    def project_request(method: str, url: str, **kwargs) -> Response:
        return requests.request(method, url, **kwargs)
