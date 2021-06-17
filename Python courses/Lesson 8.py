### JSON SAMPLE FORMAT
import json


json_string = """"""
{
  "people": [
    {
      "name": "Jack Sumers",
      "phone": "555-555-555",
      "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
      "has_licence": false,
      "salary": 1500
    },
    {
      "name": "Mary Smith",
      "phone": "777-777-777",
      "emails": null,
      "has_licence": true,
      "salary": 1700
    },
    {
      "name": "Steven Cooke",
      "phone": null,
      "emails": "stevencooke@example.com",
      "has_licence": true,
      "salary": 2500
    }
  ]
}
""""""

data = json.loads(json_string)
print(type(data))
print(data)

print(data['people'][0]['name'])
print(data['people'][0]['emails'][2])
#####
# print(data['people'])
# print(type(data)['peolpe'])
#
# for person in data['people']:
#     print(person)
########
print(data['people'][0]['name'],data['people'][0]['emails'][1])

print(type(data))

new_json = json.dumps(data, indent=2)
print(new_json)
print(type(new_json))

# ##
new_json = json.dumps(data, indent=2, sort_keys=True)
###
person1 = data['people'][1]
print(person1)

people = data['people']
person1 = people
print(person1['name'])


