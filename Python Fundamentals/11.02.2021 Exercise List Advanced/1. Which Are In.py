first_list = input().split(", ")
second_list = input().split(", ")

new_list = [first for first in first_list for second in second_list if first in second]

# for first in first_list:
#     for second in second_list:
#         if first in second:
#             new_list.append(first)
#
print(sorted(set(new_list), key=new_list.index))