import string
text = open('text.txt')
count = 0
for index, line in enumerate(text.readlines()):
    
    count_punct = [char for char in line if char in string.punctuation]
    count_words = [char for char in line.replace(" ", "").strip() if char not in string.punctuation]
    print(f'Line {index+1}: {line.strip()}({len(count_words)})({len(count_punct)})')
                      