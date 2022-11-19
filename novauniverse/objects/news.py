from ..api import NovaAPI, Endpoints

class NewsAll(NovaAPI):
    def __init__(self):
        super().__init__(Endpoints.NEWS_ALL)

        self.data = self.get()