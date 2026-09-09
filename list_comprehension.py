'''
It is an efficient way to write a code
'''
from countries import countries

new_lst = []
for country in countries:
    new_lst.append(country.upper())

print(new_lst)

new_lst_2 = [country.upper() for country in countries if 'land' in country]
print(new_lst_2)

nums = [1, 3, 0, -1, 2, 5, 6, -3]
result = [num ** 2 for num in nums]
print(result)
positive_nums = [ num for num in nums if num > 0]
print(positive_nums)

negative_nums = [ num for num in nums if num < 0]
print(negative_nums)

even_nums = [ num for num in nums if num % 2 == 0]
print(even_nums)

countries_with_stan = [country for country in countries if country.startswith('C')]
print(countries_with_stan)

countries_code = [country.upper()[:3] for country in countries]
print(countries_code)