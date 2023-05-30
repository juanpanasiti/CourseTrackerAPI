from httpx import Client

from app.core import settings


class PlatziEI():
    def __init__(self) -> None:
        self.client = Client(base_url=settings.PLATZI_URL)

    def get_page(self, path:str) -> str:
        try:
            response = self.client.get(path)
            # !DELETE PRINT
            print('\033[92m', f'Requested URL: {response.request.url}', '\033[0m')
            return response.text
        except Exception as ex:
            print('\033[41m', type(ex), '\033[0m')
            print('\033[91m', ex.args, '\033[0m')
            raise ex
