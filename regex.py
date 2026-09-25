import re 
from utils import change_text2words_from_txt

'''
match
findall
sub

'''


pattern = 'love'

txt = 'I love people because love is great if i do not love what else can i do.'
result = re.match(pattern, txt)

print('Finland'.startswith('Fin'))

if result:
    print('found')
else:
    print('do not start with your pattern')

result = re.search(pattern, txt)
print(result)


result = re.findall(pattern, txt)


print(result)

result = re.sub('love', 'like', txt)
print(result)



txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

result = re.sub('%', '', txt)
print(result)

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

result = re.split('\n', txt)
print(result)

print('what is in here?')
print(change_text2words_from_txt(txt))
