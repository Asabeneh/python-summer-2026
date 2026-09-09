'''
Arithmetic Operators: +, -, *, /, //, **, %
Comparison Operators: >, >=, <, <=, ==, !=
Logical Operators: and, or, not

'''

# comparison operators
print('===== **** Comparison Operators *** ====')
print(4 > 3)
print(4 >= 3)
print(4 >= 4)

print(4 < 3)
print(4 <= 3)
print(3 <= 3)

print(3 == 4)
print(3 == '3')
print(3 == 3)
print(100 == 10 ** 2)

print(3 != '3')
print(3 != 1)


# Logical orperators: and, or, not
print('===== **** Logical Operators **** =====')

print(4 > 3 and 2 > 1) # True
print(4 > 3 and 2 < 1) # False
print(4 < 3 and 2 < 1) # False


print(4 > 3 or 2 > 1) # True
print(4 > 3 or 2 < 1) # True
print(4 < 3 or 2 < 1) # False

# Not
print('==== *** Negation *** ====')

print(not 4 > 3)
print(not True)
print(not False)
print(not not True)

print('a' is 'a')
print('a' is not 'b')
print('abc' in 'abcde')
print('on' in 'python' and 'on' in 'Dragon')
print('land' in 'Finland')

