#bit.ly/tk-db-mlab

import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds233769.mlab.com:33769/c4e24-web2

host = "ds233769.mlab.com"
port = 33769
db_name = "c4e24-web2"
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