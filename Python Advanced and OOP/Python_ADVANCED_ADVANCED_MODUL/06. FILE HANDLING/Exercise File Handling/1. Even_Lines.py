import re

def replaced_symbols(line):
    return re.sub(r"[,-.!?]", "@", line)

with open("text.txt", "r") as file:
    lines = file.readlines()
    for row_number in range(0, len(lines), 2):
        replaced = replaced_symbols(lines[row_number]).split()
        print(" ".join((replaced[::-1])))