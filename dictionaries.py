'''
Dictionary: a python data type with key and value pair
'''
from pprint import pprint

empty_dict = {}
print(empty_dict, type(empty_dict))

user = {
    'username':'asab',
    'email':'asab@example.com',
    'password':'123456',
    'creat_at':'August 23, 2026'
}
print(user)
print(user['username'])
print(user['email'])
print(user['password'])
print(user['creat_at'])

person =  {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'is_married':True,
    'country':'Finland',
    'city':'Helsinki',
    'email':'asab@example.com',
    'age':250,
    'height':1.72,
    'gender':'male',
    'skills':['HTML','CSS','JavaScript','Python']
}


print(person['first_name'])
print(person['last_name'])
full_name = person['first_name'] + ' ' + person['last_name']
print(full_name)
print(person.get('first_name'))
print(person.get('last_name'))
print(person.get('nationality'))

if 'nationality' in person:
    print(person['nationality'])
else:
    print('Unknow nationality')

person['nationality'] = 'Ethiopian'

pprint(person)

person['age'] = 55
print(person)

print(len(person))
print(person['skills'])
person['skills'].append('databases')
pprint(person)
# person.pop('age')
del person['age']

pprint(person)

items = person.items()
for item in items:
    print(item)

copied_person = person.copy()
print(copied_person)

keys = person.keys()
print(keys)
values = person.values()
print(values)

items = person.items()
for item in items:
    print(item[1])