def palidrome(num):
    num = num.split(", ")
    forward_list = []
    backward_list = []
    answers = []
    for n in num:
        n = str(n)
        forward_list = []
        backward_list = []
        for forward in n:
            chr = int(forward)
            forward_list.append(chr)
        for backward in n:
            chr = int(backward)
            backward_list.insert(0, chr)
        if forward_list == backward_list:
            answers.append("True")
        else:
            answers.append("False")
    return answers


numbers = input()
result = palidrome(numbers)
for i in result:
    print(i)
