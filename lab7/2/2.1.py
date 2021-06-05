import json
dict = {"name":"saeed","id":"95102157"}

dict_str = json.dumps(dict)
str_dict = json.loads(dict_str)