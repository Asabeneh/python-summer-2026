from pprint import pprint

'''
Packing and unpacking

* tuple
** dictionary

'''

""" def sum_of_five_nums(*args):
    print(args)
    return sum(args)


print(sum_of_five_nums(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))

a, b, *rest = (10, 20, 30, 40, 50)
print(a, b, rest) """


def sum_of_five_nums(a, b, c, d, e):
    print(a,b, c, d, e)
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15


numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, second_last, last = numbers
print(one, middle, second_last, last)

'''
* => args => arguments
** => kwargs => key and value arguments

'''

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} years old.'


print(unpacking_person_info('Asab', 'Finland', 'Helsink', 150))

dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
#values = list(dct.values()) # ['Asabeneh', 'Finland', 'Helsinki', 250]
print(unpacking_person_info(**dct))
# print(values)

#print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.


def packing_person_info(**kwargs):
    print('let us see the pack:', kwargs)
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} =>>>>> {kwargs[key]}")
    return kwargs

pprint(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250, email= 'asab@gmail.com', nationality='Ethiopian'))


lst_one = (1, 2, 3)
lst_two = (4, 5, 6, 7)
lst = [0, lst_one, lst_two]
print(lst)


countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

for i in range(len(countries)):
    print(i + 1, countries[i])

print('================ ENUMERATE ====================')
for item in enumerate(countries):
    index, value = item 
    print(index + 1, value)

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
cities = ['Helsinki','Stockholm', 'Oslo','Copenhagen',' Reykjavík']
items = zip(countries, cities)
# print(list(items))

for country, city in items:
    print(country, city)