person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person)

# print out the name of the second child
list_of_children = person['children']
print(person["children"][1])

# print out the name of the cat
print(person['children'][1])


# use a loop to print out the names of each child
dict_of_pets = person['pets']
print(dict_of_pets['cat'])

#without a variable
print(person["pets"]['cat'])

#name of each child
for child in person['children']:
    print(child)


# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido
for pet in person['pets'].items():
    print(f"The type of pet is: dog and the name of the pet is: {name}")