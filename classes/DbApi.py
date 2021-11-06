import json
from os.path import abspath


class DbApi:

    def READ_JSON(path):
        abs_path = abspath(path)
        with open(abs_path, 'r') as f:
            obj = json.load(f)
        return obj

    def WRITE_JSON(path, obj):
        abs_path = abspath(path)
        with open(abs_path,'w') as f:
            f.write(json.dumps(obj))
