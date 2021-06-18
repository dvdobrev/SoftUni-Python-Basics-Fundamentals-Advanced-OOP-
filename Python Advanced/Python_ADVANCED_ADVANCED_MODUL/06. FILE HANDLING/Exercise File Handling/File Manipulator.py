import os
def create(file):
    open(f"{file}", "w")
def add(file,content):
    file_obj = open(f"{file}", "a")
    file_obj.write(f"{content}\n")
    file_obj.close()
def replace(file,old_string,new_string):
    
    try:
        with open(f"{file}", "r") as line:
            data = line.read()
        with open(f"{file}", "w") as line:
            data = data.replace(old_string,new_string)
            line.write(data)
    except FileNotFoundError:
        print("An error occured")
    
def delete(file):
    try:
        os.remove(f"{file}")
    except FileNotFoundError:
        print("An error occured")
    
        
        
        
command = input()
while not command == "End":
    command = command.split('-')
    if command[0] == "Create":
        create(command[1])
    elif command[0] == "Add":
        add(command[1], command[2])
    elif command[0] == "Replace":
        replace(command[1],command[2], command[3])
    elif command[0] == "Delete":
        delete(command[1])
    
    command = input()  