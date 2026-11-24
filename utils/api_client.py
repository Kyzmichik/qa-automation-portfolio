import requests


class ApiClient:
    """Thin wrapper around requests: one session, base URL and default timeout."""

    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json", "Accept": "application/json"})

    def _url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(self, path, **kwargs):
        return self.session.get(self._url(path), timeout=self.timeout, **kwargs)

    def post(self, path, **kwargs):
        return self.session.post(self._url(path), timeout=self.timeout, **kwargs)

    def put(self, path, **kwargs):
        return self.session.put(self._url(path), timeout=self.timeout, **kwargs)

    def patch(self, path, **kwargs):
        return self.session.patch(self._url(path), timeout=self.timeout, **kwargs)

    def delete(self, path, **kwargs):
        return self.session.delete(self._url(path), timeout=self.timeout, **kwargs)
