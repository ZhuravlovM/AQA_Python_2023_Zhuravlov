from requests import get, Response
from lesson24_api.homework24.app_starships import config


class StarshipsService():
    def __init__(self):
        self.__starships_url = f"{config['host']}/starships"

    def get_starship(self, starship_id) -> Response:
        return get(f"{self.__starships_url}/{starship_id}")
