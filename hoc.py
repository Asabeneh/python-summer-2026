def make_square(n):
    return n * n

# This a higher order function because it takes a function as a parameter.
def make_cube(func, n):
    return func(n) * n

print(make_cube(make_square, 10))


# Higher order function because it returns another function as a value
def do_math(n):
    def add_ten():
        return n + 10
    return add_ten

func = do_math(990)
print(func())