# 1. Module:json is for json processing.
# 2. Module:json cannot process datetime by default.
import json
import datetime


class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


filename = 'a.json'
a = {'col1': {'col11': 'a'}, 'col2': '一'}
now = datetime.datetime.utcnow()

print(json.dumps(a))  # dumps() convert an object to be a json string.
print(json.loads(json.dumps(a)))  # lodas() convert a json string to an object.

print(now)
print(json.dumps(now, cls=DTEncoder)) # pass new encoder to replace default encoder to convert datetime.
