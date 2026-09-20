'''
.txt
.pdf
.md
.csv => comma separated value
.tsv => tab separated values
.doc
.json
.xml
.xlsx
.tson
'''

'''
.txt
.csv
.json
.xlsx => csv
.xml
'''
from utils import freq_table, change_text2words


# words =  change_text2words('./notes.txt')
# print(freq_table(words, 5))


words = change_text2words('./sample.txt')

print(freq_table(words, 3))

words = change_text2words('./asab.txt')
# print(words)
print(freq_table(words, 10))
    






