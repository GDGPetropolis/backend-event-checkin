import json
import http.client

from src.clients.base_client import BaseClient


class PersonClient(BaseClient):

    def __init__(self, base_url: str, group: str, api_key: str):
        super().__init__(base_url, group, api_key)

    def get_all(self):
        page_index = 1

        json_obj = self.get("events?photo-host=public&page=" + str(page_index))

        print(json_obj)
