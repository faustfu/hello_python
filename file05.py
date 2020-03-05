# 1. Module:yaml(pyyaml) is for yaml processing.
import yaml

filename = 'a.yaml'
a = {'col1': {'col11': 'a'}, 'col2': '一'}

with open(filename, 'wt') as fout:
    fout.write(yaml.dump(a))

with open(filename, 'rt') as fin:
    raw = fin.read()
    print(raw)
    print(yaml.safe_load(raw))
