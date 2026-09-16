'''
Write a Python script that calcuates employee income

'''

""" try:
    wage = float(input('Enter wage per hour: '))
    hours = float(input('Number of hours per week: '))
    amount = wage * hours
    print(amount)
except:
    print('Wage shouldn\'t be text. Try it again with a number.')

else:
    print('I will be excuted with the try block')
    pass

finally:
    print('I will be excuted no matter what')
    pass """


try:
    print(10 + '5')
except Exception as e:
    print(e)
    print('Something went wrong')



""" try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2026 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)
    print('Something went wrong') """


try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 10 + '10'
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

