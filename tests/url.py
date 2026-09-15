class Url_ui:
    def __init__(self):
        self.base_url = "http://127.0.0.1:5500/"

    def set_url_ui(self, endpoint: str = "index.html") -> str:
        return f"{self.base_url}{endpoint or 'index.html'}"


class Url_api:
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000"

    def set_Url_api(self, endpoint: str) -> str:
        return f"{self.base_url}{endpoint}"