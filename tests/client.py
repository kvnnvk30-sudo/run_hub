import requests
""" Initializes the TestClient with a base URL and a requests session. """
class TestClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def set_requests(self,method:str ,endpoint: str='', **kwargs):
        url = f"{self.base_url}/{endpoint}"
        return self.session.request(method, url, **kwargs)

    def set_get(self,endpoint: str='', **kwargs):
        return self.set_requests('GET', endpoint, **kwargs)
    
    def set_post(self,endpoint: str='', **kwargs):
        return self.set_requests('POST', endpoint, **kwargs)

    def set_options(self, endpoint: str = '', **kwargs):
        return self.set_requests('OPTIONS', endpoint, **kwargs)