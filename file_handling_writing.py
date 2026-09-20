from utils import format_time
import os



""" name = input('Enter you name: ')
role = input('What is your role? ')
time = format_time()
f = open('./text.txt', 'a')
f.write(f'{time} - {name} - {role}\n') """

'''
f = open(f'test-1.txt', 'a')
for i in range(1, 101):
    f.write(f'{i} x {i} = {i ** 2}\n')
f.close()

'''


with open(f'test-1.txt', 'a') as f:
    for i in range(1, 101):
        f.write(f'{i} x {i} = {i ** 2}\n')
    


