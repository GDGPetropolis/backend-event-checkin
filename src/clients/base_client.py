import json
import http.client


class BaseClient(object):

    def __init__(self):
        self.base_url = "api.meetup.com"
        self.group = "GDGPetropolis"
        self.api_key = "..."

    def _get_many(self, path: str, from_json):
        json_response = self.__do_request(path, "GET")
        return [from_json(json_obj) for json_obj in json_response]

    def _get_one(self, path: str, from_json):
        json_response = self.__do_request(path, "GET")
        print(json_response)
        return from_json(json_response)

    def __do_request(self, path, verb):
        conn = http.client.HTTPSConnection(self.base_url)
        uri = self.__build_uri(path)
        conn.request(verb, uri)
        response = conn.getresponse()

        string = response.read().decode('utf-8')
        json_response = json.loads(string)

        return json_response

    def __build_uri(self, path):
        uri = "/" + self.group + "/" + path + "?key=" + self.api_key
        print(uri)
        return uri
