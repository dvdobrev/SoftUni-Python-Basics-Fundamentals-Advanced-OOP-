data = input()

file_name = ""
file_extencion = ""
text = data.split("\\")

searched_text = text[-1].split(".")

print(f"File name: {searched_text[0]}")
print(f"File extension: {searched_text[1]}")
