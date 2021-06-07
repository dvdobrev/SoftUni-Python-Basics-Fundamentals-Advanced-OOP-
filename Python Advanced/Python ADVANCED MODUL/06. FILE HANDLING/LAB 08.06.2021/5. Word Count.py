import re

def write_result(res):
    with open("output.txt", "w") as file:
        for k, v in res.items():
            file.writelines(f"{k} - {v}")
            file.writelines("\n")
        #file.writelines("\n".join(res))


def read_text():
    with open("text.txt", "r") as file:
        text = "".join(file.readlines()).lower()
        return re.findall(r"[a-zA-Z']+", text)

def read_words():
    with open("words.txt", "r") as file:
        words = "".join(file.readlines())
        return re.findall(r"[a-zA-Z]+", words)


text_file = read_text()
words_file = read_words()

result = {}

for word in words_file:
    if word in text_file:
        result[word] = text_file.count(word)

sorted_result = dict(sorted(result.items(), key=lambda kvp: -kvp[1]))
#test_result = [f"{el[0]} - {el[1]}" for el in sorted(result.items(), key=lambda x: -x[1])]
write_result(sorted_result)
#write_result(test_result)


#
# def write_result(res):
#     with open("output.txt", "w") as file:
#         file.writelines("\n".join(res))
#
# def get_file_words(path_to_file):
#     with open(path_to_file, "r") as file:
#         text = "".join(file.readlines())
#         return re.findall(r"[a-z']+", text.lower())
#
# path_to_words = "words.txt"
# path_to_text = "text.txt"
#
# first_file_words = get_file_words(path_to_words)
# second_file_words = get_file_words(path_to_text)
#
# analyse = {}
#
# for word in first_file_words:
#     if word in second_file_words:
#         analyse[word] = second_file_words.count(word)
#
# result = [f"{el[0]} - {el[1]}" for el in sorted(analyse.items(), key=lambda x: -x[1])]
# write_result(result)




