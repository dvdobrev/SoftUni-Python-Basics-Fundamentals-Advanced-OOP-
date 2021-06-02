# def concatenate(*args):
#     text = ""
#     for el in args:
#         text += el
#     return text

def concatenate(*args):
    text = "".join([el for el in args])
    return text

print(concatenate("Soft", "Uni", "Is", "Great", "!"))