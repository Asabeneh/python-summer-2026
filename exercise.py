'''
Number guessing game

'''

from random import randint

lives = 7
print('====== WELCOME TO NUMBER GUESSING GAME =====')
print('I have chosen a secret number between 1 and 100')
print('Guess the number')
print(f'You have {lives}.')
print('====== GOOD LUCK =======================')
number = randint(1, 100)



while True:
    your_number = int(input('Guess the number: '))
    if your_number == number:
        print("🎉"*25)
        print('CONGRATULATIONS! You won!')
        print(f'Your number is {your_number}, and the winning number is also {number}')
        print("🎉"*25)
        break
    else:
         if your_number > number:
             print(f'Your number is greater than my number')
         else:
            print(f'Your number is less than my number')
    lives = lives - 1
    print(f'You have {lives}.')
        
           
       
       

