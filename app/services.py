from requests import Session
from urllib.parse import urljoin

class StrapiSession(Session):
    def __init__(self, base_url=None, *args, **kwargs):
        super(StrapiSession, self).__init__(*args, **kwargs)
        self.base_url = base_url
    
    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.base_url, url)
        return super(StrapiSession, self).request(method, url, *args, **kwargs)
    
    
session = StrapiSession(base_url="http://10.140.127.124:1337")

   

