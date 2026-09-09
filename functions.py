'''
function: is a block of code that implement a certain task
'''

from countries import countries
from pprint import pprint

def do_something(activity):
    print(f'I am {activity}.')

do_something('teaching')
do_something('learning')
do_something('playing')
do_something('exercising')

def add_two_nums(a, b):
    total = a + b 
    return total

print(add_two_nums(4, 5))
print(add_two_nums(40, 50))
print(add_two_nums(999, 1))

result = add_two_nums(400, 500)
print(result)

def print_fullname(first_name, last_name):
    return first_name + ' ' + last_name

print(print_fullname('Asabeneh','Yetayeh'))
print(print_fullname('Desale','Kidane'))
print(print_fullname('Donald','Trump'))

'''

0 to 100

'''

# numbers = list(range(101))
# total = sum(numbers)
# print(total)

def sum_all_nums(n):
    total = 0
    for i in range(n + 1):
        total = total + i
    return total
print(sum_all_nums(100))
print(sum_all_nums(50))

'''
The name of the function is area_of_circle
- it takes radius as a paremeter:
'''

def area_of_circle(radius):
    pi = 3.14
    return pi * radius ** 2

print(area_of_circle(10))
print(area_of_circle(50))

def filter_countries(term = 'land'):
    lst = []
    for country in countries:
        if term in country:
            lst.append(country)
    return lst
filter_countries()
# print(filter_countries())
# print(filter_countries('ia'))






