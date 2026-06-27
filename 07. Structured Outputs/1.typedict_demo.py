from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name': 'Nikhil', 'age': 36}

print(new_person)