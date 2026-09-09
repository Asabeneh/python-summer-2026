'''
We will learn in this file about built-in functions:
print - DONE
len - DONE
type - DONE
int - DONE
float - DONE
bool - DONE
min - DONE
max - DONE
sum - DONE
range
round - DONE
input

'''
# This builtin print function takes one or unlimited number inputs
print('hello', 2026, 9.81 )

print(len('cat'))
print(len('book'))
print(len('book worm'))
print(len('I love python because it is just amazing.'))
print(type(100))
print(type(3.14))
print(type(4j + 2))

print(int(9.81), type(int(9.81)))
print(float(7))
print(bool(0))
print(bool(''))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(1))
print(bool(-1))
print(bool('andndy any string'))

ages = [24, 35, 65, 40, 39, 31, 33, 22, 24, 39]
print(len(ages))
print(min(ages))
print(max(ages))
print(sum(ages))

'''
Average age = total number of ages/ total students
mean, standard deviation, varience, mode, range
range = max - min 
'''
total = sum(ages)
n = len(ages)
average = total / n
mx = max(ages)
mn = min(ages)

print('Average age:', average)
difference_between_max_min = mx - mn
print('The range of the data', difference_between_max_min)

radius = 45.56
area = 3.14 * radius ** 2
print(area, round(area), round(area, 1))

print(list(range(100, 1001, 100)))

whole_numbers = list(range(0, 101))
print(whole_numbers)

counting_numbers = list(range(1, 101))
print(counting_numbers)

odd_numbers = list(range(1, 101, 2))
print(odd_numbers)

even_numbers = list(range(0, 101, 2))
print(even_numbers)

# input
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
country = input('Where are you located? ')
date_of_birth = int(input('When were you born? '))
current_year = 2026
age = current_year - date_of_birth

print(f'My name is {first_name} {last_name}. I live in {country}. I was born in {date_of_birth}. Currently, I am {age} years old.')

