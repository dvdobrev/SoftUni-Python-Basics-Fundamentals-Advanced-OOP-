n1 = int(input())
n2 = int(input())
multiple_num = 0
my_list = []

for i in range(n2):
    multiple_num += n1
    my_list.append(multiple_num)
print(my_list)