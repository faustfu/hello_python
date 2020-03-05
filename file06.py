# 1. Module:configparser is for process configurations.
import configparser

filename = 'a.cfg'


cfg = configparser.ConfigParser()
cfg.add_section('a')
cfg.add_section('b')

for section in cfg.sections():
    cfg[section]['greeting'] = 'hi'

with open(filename, 'wt') as fout:
    cfg.write(fout)

with open(filename, 'rt') as fin:
    cfg.read(fin)
    for section in cfg.sections():
        print('%s greeting = %s' % (section, cfg[section]['greeting']))
