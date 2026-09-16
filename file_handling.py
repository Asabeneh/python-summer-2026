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

f = open('./notes.txt')
lines = f.read().splitlines()
lst = []
for line in lines:
    words = line.replace('.', '').replace(',', '').lower().split()
    lst.extend(words)

def freq_table(lst, n = None):
    dct = {}
    for word in lst:
        if word in dct:
            dct[word] = dct[word] + 1
        else:
            dct[word] = 1
    items = dct.items()
    sorted_items = sorted(items, key = lambda item:item[1], reverse=True)
    if n:
        return sorted_items[0:n]
    return sorted_items

print(freq_table(lst, 5))






