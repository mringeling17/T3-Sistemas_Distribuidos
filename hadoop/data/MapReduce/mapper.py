#!/usr/bin/python

#https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/
import sys
import re

for line in sys.stdin:
    line = line.lower()

    line = re.sub(r'[áàäâ]', 'a', line)
    line = re.sub(r'[éèëê]', 'e', line)
    line = re.sub(r'[íìïî]', 'i', line)
    line = re.sub(r'[óòöô]', 'o', line)
    line = re.sub(r'[úùüû]', 'u', line)
    line = re.sub(r'[ñ]', 'n', line)
    line = re.sub(r'[ç]', 'c', line)

    line = re.sub(r'[^a-zA-Z0-9]', ' ', line)
    line = line.strip()
    words = line.split()
    for word in words:
        print('%s\t%s' % (word, 1))

## EJEMPLO DE EJECUCIÓN COMPLETO CON REDUCER EN WINDOWS CON POWERSHELL:
# cat ..\carpeta1\1.txt | python .\mapper.py | Sort-Object | python .\reducer.py
## LINUX:
#cat ..\carpeta1\1.txt | python .\mapper.py | sort -k1,1 | python .\reducer.py