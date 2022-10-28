import json

#
# person = '{"name": "Bob", "languages": ["English", "French",["Python","Java"]]}'
# person_dict = json.loads(person)
#
# print(person_dict)
# print(person_dict['languages'][0])
# print(person_dict['languages'][1])
# print(person_dict['languages'][2][0])

# with open('person.json', 'r') as f:
#     data = json.load(f)
# print(data)

dict = {'name': 'Bob',
        'age': 12,
        'children': None
        }

# dict_json = json.dumps(dict)
# print(dict_json)

with open('person2.json', 'w') as json_f:
    json.dump(dict, json_f, indent=4, sort_keys=True)
