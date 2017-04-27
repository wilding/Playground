import json

json_object = {
    "instructions": [
        {
            "text": 1,
            "image": 2,
            "video": 3,
            "gif": 4,
            "note": 5
        }
    ]
}


print json_object  # is a dict
print '\n'


json_string = json.dumps(json_object)  # is a string representation of dict
print json_string
print '\n'


print json.loads(json_string)  # is a dict
print '\n'
