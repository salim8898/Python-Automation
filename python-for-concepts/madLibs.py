import os
import re
madLibs = open('madLibs.txt')
template = madLibs.read()
madLibs.close()

regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')

for i in regex.findall(template):
    for j in i:
        if j != '':
            reg = re.compile(r'{}.format(j)')
            print(reg)



