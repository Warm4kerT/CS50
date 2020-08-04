people=[
    {"name":"Harry", "house": "Grynffindor"},
    {"name":"Cho", "house": "Ravenclaw"},
    {"name":"Draco", "house": "Slytherin"}
]

def f(person):
    return person["house"]

people.sort(key=f)

# or

people.sort(key=lambda person: person["house"])

print(people)