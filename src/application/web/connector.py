from time import sleep
from httpx import Client, HTTPError, Response


class Connector():
    @staticmethod
    def connect(method: str, client: Client, url: str,
                data: dict | None = None, params: str | None = None,
                headers: dict | None = None, follow_redirects: bool = True,
                current_attempt: int = 0, attempts: int = 3,
                wait_sec: float = 3.0) -> Response | None:
        """
        Позволяет делать http запросы без опасения,
        что при ошибке доступа к сайту у нас упадёт скрипт.

        method -- метод для отправки http запроса
        client -- клиент, сохраняющий куки и заголовки для подключения к сайту
        data -- передаваемые данные для запроса
        params -- передаваемые параметры для запроса
        url -- путь до сайта
        follow_redirects -- разрешить переходы, если их делает сайт
        current_attempt -- текущая попытка
        attempts -- кол-во попыток
        wait_sec -- кол-во секунд между попытками
        """
        try:
            if current_attempt < attempts:
                response = client.request(
                    method, url, headers=headers, data=data, params=params,
                    follow_redirects=follow_redirects)
                with open('index.json', 'w', encoding="utf-8") as file:
                    file.write(response.text)
                if response.status_code != 200:
                    raise HTTPError(str(response.status_code))
                return response
            return None
        except HTTPError:
            sleep(wait_sec)
            return Connector.connect(method, client, url, data, params,
                                     headers, follow_redirects,
                                     current_attempt+1, attempts, wait_sec)

    @staticmethod
    def get(client: Client, url: str,
            params: str | None = None,
            headers: dict | None = None, follow_redirects: bool = True,
            current_attempt: int = 0, attempts: int = 3,
            wait_sec: float = 3.0):
        """
        Реализация метода connector для GET запросов.

        client -- клиент, сохраняющий куки и заголовки для подключения к сайту
        url -- путь до сайта
        params -- передаваемые параметры для запроса
        follow_redirects -- разрешить переходы, если их делает сайт
        current_attempt -- текущая попытка
        attempts -- кол-во попыток
        wait_sec -- кол-во секунд между попытками
        """

        return Connector.connect("GET", client, url, params=params,
                                 headers=headers, attempts=attempts,
                                 wait_sec=wait_sec,
                                 current_attempt=current_attempt,
                                 follow_redirects=follow_redirects)

    @staticmethod
    def post(client: Client, url: str,
             data: dict | None = None,
             headers: dict | None = None, follow_redirects: bool = True,
             current_attempt: int = 0, attempts: int = 3,
             wait_sec: float = 3.0):
        """
        Реализация метода connector для POST запросов.

        client -- клиент, сохраняющий куки и заголовки для подключения к сайту
        url -- путь до сайта
        data -- передаваемые данные для запроса
        follow_redirects -- разрешить переходы, если их делает сайт
        current_attempt -- текущая попытка
        attempts -- кол-во попыток
        wait_sec -- кол-во секунд между попытками
        """

        return Connector.connect("POST", client, url, data=data,
                                 headers=headers, attempts=attempts,
                                 wait_sec=wait_sec,
                                 current_attempt=current_attempt,
                                 follow_redirects=follow_redirects)
