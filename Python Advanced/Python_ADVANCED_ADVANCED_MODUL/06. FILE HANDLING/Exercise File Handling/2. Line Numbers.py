def text_append(lines):
    striped_text = lines.strip("\n")
    with open("output_task_02.txt", "a") as file:
        file.writelines(f"Line {line_counter}: {striped_text} ({counter(line)[0]})({counter(line)[1]})")
        file.writelines("\n")


def counter(line):
    letters_counter = 0
    punctuations_counter = 0
    line_as_list = [el for el in line]
    # punctuations = ["!", '"', "'", "-", ".", ":", ";", "?", ""]
    punctuations = [33, 34, 39, 44, 45, 46, 58, 59, 63, 96]
    for el in line_as_list:
        if el.isalpha():
            letters_counter += 1
        elif ord(el) in punctuations:
            punctuations_counter += 1
    return letters_counter, punctuations_counter


line_counter = 1
with open("text.txt", "r") as file:
    for line in file.readlines():
        counter(line)
        text_append(line)
        line_counter += 1
