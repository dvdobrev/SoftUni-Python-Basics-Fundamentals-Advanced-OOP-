import os

path = os.walk(".")


by_extention = {}
for root, directories, files in path:
    
    
    for file in files:
        ext = file.split('.')[-1]
        if not ext in by_extention:
            by_extention[ext] = []
        by_extention[ext].append(file)

with open('report.txt', 'w') as out_file:
    for ext in sorted(by_extention.keys()):
        files = sorted(by_extention[ext])
        out_file.write(f'.{ext}\n')

        
        for file in files:
            out_file.write(f'---{file}\n')


