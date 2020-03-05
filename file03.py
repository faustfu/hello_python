# 1. Module:csv is for CSV files.
import csv

filename = 'a.csv'
a = [
    ['ab', 'cd'],
    ['ok', 'not ok'],
    ['aqw', 'p02']
]
b = [
    {'first': 'ab', 'last': 'cd'},
    {'first': 'ok', 'last': 'not ok'},
    {'first': 'aqw', 'last': 'p02'}
]

with open(filename, 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(a)

with open(filename, 'rt') as fin:
    cin = csv.reader(fin)
    print([row for row in cin])

with open(filename, 'rt') as fin:
    # read data and assign fields.
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    print([row for row in cin])

with open(filename, 'wt') as fout:
    csvout = csv.DictWriter(fout, ['last', 'first'])  # write data by fields
    csvout.writeheader()
    csvout.writerows(b)

with open(filename, 'rt') as fin:
    cin = csv.DictReader(fin)  # read data by fields
    print([row for row in cin])
