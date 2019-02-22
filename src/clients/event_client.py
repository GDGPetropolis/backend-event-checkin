import json
import http.client

from src.clients.base_client import BaseClient


class EventClient(BaseClient):

    def __init__(self, base_url: str, group: str, api_key: str):
        super().__init__(base_url, group, api_key)

    def get_all(self):
        conn = http.client.HTTPSConnection("api.meetup.com")

        person_list = list()
        page_index = 1

        #while True:
        conn.request("GET", )
        response = conn.getresponse()

        string = response.read().decode('utf-8')
        json_obj = json.loads(string)

        print(json_obj)
