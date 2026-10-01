
from pprint import pprint
from web.utils.utils import create_json_file
from web.utils.utils import fetch_data, minifiy_data

'''
population, captial
name,
region
subregion
languages
landlocked

'''
url = 'https://studies.cs.helsinki.fi/restcountries/api/all'
data = fetch_data(url)
minified_data = minifiy_data(data)

# pprint(counries)


create_json_file('test.json', minified_data)





'''
ETL = Extraction, Transformation, Loading

'''
    