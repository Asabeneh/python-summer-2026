'''
map:one to one mapping
filter - filter based on condition
reduce- one item
'''
from functools import reduce
from countries import countries
from countries_data import data
from pprint import pprint
from functools import reduce

nums = [1, 2, 3, 4, -5, 8, 10]
new_lst = [num * 2 for num in nums]
print(new_lst)
double_nums = map(lambda n: n * 2, nums)
print(list(double_nums))

positive_nums = list(filter(lambda n: n < 0, nums))
print(positive_nums)
total = reduce(lambda a, b: a + b, nums)
print(total)

countries_code = map(lambda country: country.upper()[:3], countries)
print(list(countries_code))
countries_with_land = filter(lambda country: 'land' in country, countries)
print(list(countries_with_land))


st = set()
for country in data:
    st.update(country['languages'])
print(st, len(st))

total = reduce(lambda a, b: a + b['population'], data, 0)
print(total)
