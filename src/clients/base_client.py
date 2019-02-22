import json
import http.client


class BaseClient(object):

    def __init__(self):
        self.base_url = "api.meetup.com"
        self.group = "GDGPetropolis"
        self.api_key = "..."

    def get(self, path: str, from_json):
        conn = http.client.HTTPSConnection(self.base_url)
        complete_path = "/" + self.group + "/" + path + "?key=" + self.api_key
        conn.request("GET", complete_path)
        response = conn.getresponse()

        string = response.read().decode('utf-8')
        json_objs = json.loads(string)

        return [from_json(json_obj) for json_obj in json_objs]
