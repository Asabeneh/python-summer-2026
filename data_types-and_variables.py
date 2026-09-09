'''
 Data types in Python:
Number - int, float, complex, e.g 10, 9.81, 4 + j
String - any data types under a single, double or triple quote
Booleans - The values are always True or False
List: A list of ordered items and mutable, eg [1, 2, 3, 4], ['Finland', 'Sweden', 'Denmark', 'Norway','Iceland']
Set: It is a collection of items and mutable, but items cannot be repeated and don't have order, e.g {1, 2, 3, 4}
Tuple: It is an order collection of items but cannot be modified(immutable), eg (1, 2, 3)
Dictionary:It is key value pair, e.g {'Amhara':'Bahir Dar', 'Tigray':'Mekele', 'Oromia':'Adama'}

'''

# Variables
a = 3
b = 4

print(f'The sum of {a} and {b} is {a + b}.')
print(f'The difference of {a} and b is {a - b}.')
print(f'The product of {a} and {b} is {a * b}.')
print(f'The remain of {a} divided by {b} is {a % b}')
print(f'The floor division of {a} by {b} is {a // b}')
print(f'The {a} the power of {b} is {a ** b}')

first_name = 'Desale'
last_name = 'Kidane'
age = 35
counry = 'Belgium'
city = 'Brussles'
skills = ['Python','Data Analysis','AI tools', 'Geospatial Analysis']
year = 2016

print(first_name, last_name, age, counry, city, skills, year)

# Data types
'''
Numbers: int, float, complex

'''
print(type(10))
print(type(9.81))
print(type(4j + 1))
print(type(1j + 4))

a = 10
print(type(a))
gravity = 9.81
print(type(gravity))
cpx = 4j + 2
print(type(cpx))

# Booleans: True or False
print(True)
print(False)
print(4 > 3)
print(4 < 0)
print(4 == '4')
print(type(True))
print(type(False))
print(type(0 > 1))

# Strings: any data under a single, double or triple quote
print('a', type('a'))
alphabets = 'abcdefghijklmnopqrstuvwxyz'
print(alphabets, type(alphabets))
txt = 'I really love people because I chose to love.'
print(type(txt), len(txt))

some_text = '''The 30 Days of Python programming challenge is a step-by-step guide to learn the Python programming language in 30 days. This challenge may take more than 100 days. Follow your own pace. These videos may help too: https://www.youtube.com/channel/UC7PNRuno1rzYPb1xLa4yktw'''


# List: It is an ordered, mutable, index list of items.

nums = [1, 2, 3, 4, 5]
print(type(nums))
print(len(nums))
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])

last_index = len(nums) - 1 # 4
print(nums[last_index])
print(nums[-1])
print(nums[-5])

countries = ['Finland', 'Sweden','Denmark','Norway','Iceland', 'Finland']
print('This is from the list', countries)
fruits = ['Apple','Mango', 'Avocado','Guava','Orange']


# Set - It is mutable, not inexed and don't allow duplicates
countries = {'Finland', 'Sweden','Denmark','Norway','Iceland','Finland'}
print('This is from the set', countries)
fruits = {'Apple','Mango', 'Avocado','Guava','Orange'}

# Tuple: ordered, indexed, but not mutuable
countries = ('Finland', 'Sweden','Denmark','Norway','Iceland', 'Finland')
print('This from your tuple:', countries)
fruits = ('Apple','Mango', 'Avocado','Guava','Orange')

# Dictionary:key value pair

am_en_dict = {
    'house':'bet',
    'chair':'wonber',
    'food':'megeb',
    
}
print(am_en_dict)
print(am_en_dict['house'])
print(am_en_dict['food'])