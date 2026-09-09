'''
Crete a function named make_square
It takes one paramter
It returns the square of the paramter

'''

def make_square (n):
    return n ** 2

print(make_square(3))
print(make_square(10))

def make_cube(n):
    return n ** 3
print(make_cube(3))


def make_square (n):
    return n ** 2

func = lambda a, b, c: a * b + c
print(func(3, 4, 10))
