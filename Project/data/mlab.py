# mongodb://<dbuser>:<dbpassword>@ds123834.mlab.com:23834/project_c4e24

import mongoengine


host = "ds123834.mlab.com"
port = 23834
db_name = "project_c4e24"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())