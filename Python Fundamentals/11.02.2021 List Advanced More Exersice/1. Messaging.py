num_list = input().split()
text = input()
sum_of_elements_digits = []

for num in num_list:
    sum_for_element = 0
    for el in num:
        element = int(el)
        sum_for_element += element
    sum_of_elements_digits.append(sum_for_element)

element_value_1 = []

for element_value in range(len(sum_of_elements_digits)):
    current_chr = ""
    index = 0
    next_value = False
    while True:
        current_index = 0
        for chrkt in text:
            current_chr = chrkt
            if index == sum_of_elements_digits[element_value]:
                element_value_1.append(current_chr)
                text = text[0:current_index:] + text[current_index + 1 ::]
                next_value = True
                break
            index += 1
            current_index += 1
        if next_value:
            break
print("".join(element_value_1))


