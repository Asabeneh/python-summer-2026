'''
Loops allow us to solve repetitive problems
'''

for num in  [1, 2, 3]:
    print(num, num * num, num * 100)


new_lst = []
for country in ['Finland','Sweden','Norway','Denmark','Iceland']:
    new_lst.append((country, country.upper(), country.upper()[0:3], len(country)))


print(new_lst, len(new_lst))

for num in range(1, 101):
    print(num)

nums = [3, 0, 2, -1, 4, -5,-6, 8]

for num in nums:
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

# for num in nums:
#     if num < 0:
#         break  # stop
#     print(num)


for num in nums:
    if num < 0:
        continue # skip
    print(num)

import random


for _ in range(1000):
    m = random.randint(1, 5)
    x = random.randint(15, 20)
    b = 100
    y = m*x + b
    print(y)


for i in range(6):
    print(i)

for i in range(5, -1, -1):
    print(i)