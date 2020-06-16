import json
from json import JSONEncoder


class Config:
    
    def __init__(self, token):
        self.token = token

class ConfigEncoder(JSONEncoder):

    def default(self, o):
        return o.__dict__


# Code below from here just plain doesn't work :)
tv = Config(tv)

if tv is None:
    print("Undeclared token!")
else:
    tjd = json.dumps(tv, indent=4, cls=ConfigEncoder)
    td = json.loads(tjd)

    with  open("config.json", "w") as of:
        json.dump(td, of)



'''
token_value = None
if token_value == None:
    print("NULL INPUT ON CONFIG.JSON!")
else:
    token_data = Config(token_value)

token_json_data = json.dumps(token_data, indent=4, cls=ConfigEncoder)
print(token_json_data)
token_data = json.loads(token_json_data)

with open("config.json", "w") as outfile:
    json.dump(token_data, outfile)
'''