import random
import math
# from math import sqrt, pi, log10, ceil, floor

print(math.pi)
print(math.floor(9.81))
print(math.ceil(9.81))
print(math.sqrt(2), 2 ** 0.5)
print(math.log10(100))

print(math.log10(10000))

print() # 0 and 0.999999 => 99.999999
# I want you to create a script that generate a random number between 1 and 100

# rand_number = math.floor(random.random() * 101)
# print(rand_number)
# print(random.randint(1, 100))
print(random.choice([1, 2, 3, 4, 5]))


def random_id_generator(n = 4):
    id = ''
    for _ in range(n):
        letter = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        id = id + letter
    return id

print(random_id_generator(24))
print(random_id_generator(10))
print(random_id_generator())

