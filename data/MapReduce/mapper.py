#https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print('%s\t%s' % (word, 1))

## EJEMPLO DE EJECUCIÓN COMPLETO CON REDUCER EN WINDOWS CON POWERSHELL:
# cat .\carpeta1\1.txt | python .\MapReduce\mapper.py | Sort-Object | python .\MapReduce\reducer.py
## LINUX:
#cat .\carpeta1\1.txt | python .\MapReduce\mapper.py | sort -k1,1 | python .\MapReduce\reducer.py