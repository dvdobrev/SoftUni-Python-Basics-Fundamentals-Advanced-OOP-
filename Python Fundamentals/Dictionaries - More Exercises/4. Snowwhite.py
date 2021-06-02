data = input()

dwarfs = {}
second_dwarf = {}

while not data == "Once upon a time":
    dwarf_name, hat_color, physics = data.split(" <:> ")
    physics = int(physics)
    if dwarf_name not in dwarfs:
        dwarfs[dwarf_name] = {hat_color: physics}
    else:
        if dwarf_name not in second_dwarf:
            second_dwarf[dwarf_name] = {hat_color: physics}



    data = input()

