"""import json

# encode data structure (aka object) to a string
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json.loads(json_string))
"""
"""
import pickle

# encoding object to JSon to return string
pickledString = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickledString)

# turn pickled_string back to object
pickledObject = pickle.loads(pickledString)
print(pickledObject)
"""

#_____________________________________________________________________

import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def addEmployee(salaries_json, name, salary):
    #data = {name : salary}
    salaries_json[name] = salary  # this is adding values to dictionary salaries_json
    return salaries_json

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }' #salaries is a string
decoded_salaries = json.loads(salaries)      # decoded_salaries is a dict, json type  --- because string salaries has been loaded to json type in decoded_salaries.
new_salaries = addEmployee(decoded_salaries, "Me", 800)   # new_salaries is dict, json type
print("First way to print:\n", new_salaries)
print("Second way to print: ")
for key, val in new_salaries.items():
    print(key, "=>", val)


"""print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])"""
