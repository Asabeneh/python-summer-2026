'''
conditionals

'''

a = 0
print(a)
print(a > 0)

if a > 0:
    print(f'{a} is greater than 0')
elif a == 0:
    print(f'{a} is equal to 0')
else:
    print(f'{a} is less than 0')



is_raining = False

if is_raining == True:
    print('Go with a raincoat.')
else:
    print('Go out freely, it seems just a shiny day.')


"""
weather = input('What is the weather is today? ').lower()
if weather == 'rainy':
    print('Go with a raincoat.')
elif weather == 'sunny':
    print('Go out freely, it seems just a shiny day.')
elif weather == 'windy':
    print('Be careful, it might be a very windy day')
elif weather == 'cloudy':
    print('There is high chance of rain.')
elif weather == 'snowy':
    print('Watch out, it might be very slippery')
else:
    print('No one knows about today weather.')

"""


a = int(input('Enter a number: '))

if a % 2 == 0:
    print(f'{a} is an even number.')
else:
    print(f'{a} is an odd number.')