def age_assignment(*args, **kwargs):
    name_age = {}
    for name in args:
        for letter, age in kwargs.items():
            if name.startswith(letter):
                name_age[name] = age

    return name_age

print(age_assignment("Peter", "George", G=26, P=19))