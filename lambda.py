people = [
    {"name": "Akbar", "house": "Urgench"},
    {"name": "Bakhrombek", "house": "Urgench"},
    {"name": "Varvara", "house": "Kiev"}
]


def f(person):
    return person["house"]


people.sort(key=lambda person: person["name"])

print(people)
