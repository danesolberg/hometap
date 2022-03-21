from abc import ABCMeta, abstractmethod
from requests import Session
from requests.adapters import HTTPAdapter, Retry
from app.clients.exceptions import UnauthorizedAccessException
from .property_detail_provider import PropertyDetailProvider


class PropertyDetailClient(metaclass = ABCMeta):
    def __init__(self, api_url, timeout=9.1):
        self.url = api_url
        self.timeout=timeout
        self.session = Session()

        retries = Retry(total=3, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])
        self.session.mount(self.url, HTTPAdapter(max_retries=retries))
        self.session.hooks['response'].append(check_auth)

    @abstractmethod
    def get_sewer_type(**kwargs):
        pass

    @property
    @abstractmethod
    def provider(self):
        provider: PropertyDetailProvider = None
        return provider

def check_auth(response, *args, **kwargs):
    if response.status_code == 401:
        raise UnauthorizedAccessException()