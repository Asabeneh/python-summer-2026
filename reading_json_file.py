import json 
from pprint import pprint

with open('./countries.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    pprint(data)


'''
1. Put all the languages together and find out the number of languages
2. Create a list of cities from this data
3. Find the world population from thid data
4. Transformat this json to a new json the new json will have only this format
[
{
 {'capital': 'Montevideo',
  'languages': ['Spanish'],
  'name': 'Uruguay',
  'population': 3480222
  }

}

]
5. Find the 10 most spoken languages
6. Find the 10 most populous nation

'''

