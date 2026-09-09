'''
Strings: are text data types, they can be created by putting single, double or triple quote

'''

letter = 'a'
print(len(letter))
alphabets = 'abcdefghijklmnopqrstuvwxyz'
print(len(alphabets))
sentence = '''The brown fox jumps over the lazy dog.'''
print(sentence.split())
words = sentence.lower().split()
unique_words = set(words)

print(sentence.upper().split())
print(words, type(words), len(words))
print(unique_words)

# You should identify the difference between builtin function and methods
print(sentence.title())
print(sentence.lower().count('the'))
print(sentence.startswith('The'))
print(sentence.endswith('dog.'))
print('fox' in sentence)
print(sentence.find('T'))
print(sentence.find('t'))
print(sentence.find('e'))
print(sentence.rfind('e'))
print(sentence.find('k'))

print(sentence.index('T'))
print(sentence.index('t'))
print(sentence.index('e'))
print(sentence.rindex('e'))
# print(sentence.index('k'))
if 'k' in sentence:
    print(sentence.index('k'))
else:
    print('k was not found')

'''
String concatenation

'''

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
country = 'Finland'
weight = 75
height = 1.72

full_name = first_name + ' ' +  last_name
print('I am ' + full_name + '. ' + 'I live in ' + country + '. ' + 'I am ' + str(age) + ' years old. ' + 'I weigh about ' + str(weight) + '.' + 'I am ' + str(height) + ' tall.')



print('I am %s. I live in %s. I am %d years old. I weigh about %d years old. I am %.2f meter tall.' %(full_name, country, age, weight, height))

print(f'I am {full_name}. I live in {country}. I am {age} years old. I weigh about {weight}. I am {height} meter tall.')

print('I am {}. I live in {}. I am {} years old. I weigh about {} years old. I am {} meter tall.'.format(full_name, country, age, weight, height))

print('Desale is a researcher.\nHe lives in France.\nHe is married and has some kids.')
print('Day 1\t Day 2 \t Day 3')
print('**********************')
# print('Day 1\t Day 2 \t Day 3')
print('1 hr\t 1hr \t 15 hrs')

print("In old python it was hard to write this back slash symbol \ ")
print("In old python it was hard to write this back slash symbol \\ ")
print('It doesn\'t matter to make some typos in this text')
print("It doesn't matter to make some typos in this text")
print("The old cliche goes like this \"An apple a day keep the doctor away\".")

a = 3 
b = 4

print(f'{a} +  {b}  = {a + b}')
print(f'{a} -  {b}  = {a - b}')
print(f'{a} x {b}  = {a * b}')
print(f'{a} / {b}  = {a / b}')


print('%d +  %d  = %d' %(a, b, a + b))
print('%d -  %d  = %d' %(a, b, a - b))
print('%d x  %d  = %d' %(a, b, a * b))
print('%d /  %d  = %.2f' %(a, b, a / b))


print('{} +  {}  = {}'.format(a, b, a + b))
print('{} -  {}  = {}'.format(a, b, a - b))
print('{} x {}  = {}'.format(a, b, a * b))
print('{} / {}  = {}'.format(a, b, a / b))

word = 'race car'
print(word[0:4])
print(word[5:])
print(word[1:3])  # ace
print(word[5:7])
print('cat')
print('cat'[::-1])
print('cat'.isalpha())
print('cat123'.isalnum())
print('cat'.isdecimal())
print('123'.isdecimal())
print( '\u00B2'.isdecimal())

skills = ['HTML', 'CSS', 'JavaScript', 'React']
print(skills)
print(', '.join(skills))

print('  Desale  ')
print('  Desale  '.strip())

txt = '''Love is a profound force that shapes human existence, acting as an essential anchor that provides deep emotional security, enduring strength, and transformative meaning to our lives through both joy and hardship. At its core, love transcends a mere fleeting emotion; it is a deliberate and continuous choice to care for, protect, and cherish another person or community despite inevitable flaws and challenges. This powerful bond manifests in many forms, from the fierce loyalty of family and the comforting warmth of deep friendship to the passionate devotion shared between romantic partners and the quiet compassion we extend to strangers in need. When we love, we step outside the narrow confines of our own ego, choosing instead to practice empathy, patience, and radical acceptance. It requires vulnerability, because opening our hearts to another person always carries the risk of pain or loss, yet this exact willingness to be hurt is what makes the experience so profoundly valuable and real. Throughout history, art, philosophy, and everyday human experience have shown that love has the unique capacity to heal deep wounds, bridge vast cultural and social divides, and inspire individuals to perform acts of extraordinary courage and selflessness. It teaches us how to see the inherent worth in others and, in turn, helps us understand our own place within the wider human family. Ultimately, love is not just something we passively feel, but a dynamic practice of connection that sustains us, challenges us to grow into better versions of ourselves, and remains the single most enduring legacy we leave behind in the world long after our own days have passed'''

words = txt.lower().replace('.', '' ).replace(',', '').split()
total_words = len(words)
unique_words = set(words)
number_unique_words = len(unique_words)
print(total_words, number_unique_words)
lexical_variety = number_unique_words / total_words * 100
print(lexical_variety)
print('CaT'.swapcase())

print('Thirty' + ' ' +  'Days' + ' ' +  'Of' + ' ' +  'Python')
company = "Coding For All"
print(company)


