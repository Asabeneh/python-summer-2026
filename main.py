
'''
import custom_modules 
# print(dir(custom_modules))
print(custom_modules.make_square(3))
print(custom_modules.make_square(5))
print(custom_modules.make_square(10))

print(custom_modules.add_two_nums(3, 2))
print(custom_modules.add_two_nums(100, 900))

print(custom_modules.sum_all_nums(3)) # 6
print(custom_modules.sum_all_nums(100)) # 6
'''
from custom_modules import make_square, add_two_nums, sum_all_nums

print(make_square(3))
print(make_square(5))
print(make_square(10))

print(add_two_nums(3, 4))
print(add_two_nums(9, 1))

print(sum_all_nums(100))
print(sum_all_nums(3)) 


""" 
from custom_modules import *
print(make_square(3))
print(make_square(5))
print(make_square(10))

print(add_two_nums(3, 4))
print(add_two_nums(9, 1))

print(sum_all_nums(100))
print(sum_all_nums(3)) """

