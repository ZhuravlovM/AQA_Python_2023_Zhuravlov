import random

name = ['Roberto', 'Lucas', 'Michelle', 'Gilbert']
surname = ['Waters', 'Counsellor', 'Bright', 'Aldrich']
location = ['California', 'Texas', 'Washington', 'Cincinnati']

def generate_person():
    random_person = {
        'Name': random.choice(name),
        'Surname': random.choice(surname),
        'Location': random.choice(location)
    }
    return random_person


person = generate_person()
print(person)
