
class Url:
    def __init__(self):
        self.base_url = 'http://127.0.0.1:8000'

    def set_Url(self,endpoint:str)->str:
        return f'{self.base_url}{endpoint}'