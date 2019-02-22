class JsonParser(object):

    @classmethod
    def try_get_parameter(cls, json, name):
        try:
            return json[name]
        except:
            return None

    @classmethod
    def try_get_parameter_with_sub_name(cls, json, name, sub_name):
        try:
            return json[name][sub_name]
        except:
            return None
