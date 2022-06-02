import re

text = open('text.txt')

for index, line in enumerate(text.readlines()):
    if not index % 2 == 0:
        continue
    line = re.sub('[-,\\.!?]', '@', line)
    
    print(' '.join(reversed(line.split())))