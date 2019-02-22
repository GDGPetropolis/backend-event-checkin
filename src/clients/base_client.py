import json
import http.client


class BaseClient(object):

    def __init__(self, base_url: str, group: str, api_key: str):
        self.base_url = base_url
        self.group = group
        self.api_key = api_key

    def get(self, path: str):
        conn = http.client.HTTPSConnection(self.base_url)
        complete_path = "/" + self.group + "/" + path + "?key=" + self.api_key
        print(complete_path)
        conn.request("GET", complete_path)
        response = conn.getresponse()

        string = response.read().decode('utf-8')
        json_obj = json.loads(string)

        return json_obj
