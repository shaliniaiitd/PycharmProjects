# Create a Python dictionary representing information about a person, including their name, age, and email.

person = {"name": "person1", "age": 23, "email":"abc@xyz.com"}

#SERIALIZATION
# Write this dictionary to a JSON file named "person.json.":
import json

with open("person.json", 'w') as f:
    json.dump(person, f)
    s = json.dumps(person)
    print(type(s))

#DE-SERIALIZATION
# Read the data from "person.json" and print it.
with open("person.json") as fr:
    person_dict = json.load(fr)
    person_from_str = json.loads(s)
print(person_from_str)
print(person_dict)

# Update the person's age in the JSON data.
person_dict["age"] = 78

# Write the updated data back to "person.json."

with open("person.json",'a') as fw:
    fw.write('\n')
    json.dump(person_dict,fw)

