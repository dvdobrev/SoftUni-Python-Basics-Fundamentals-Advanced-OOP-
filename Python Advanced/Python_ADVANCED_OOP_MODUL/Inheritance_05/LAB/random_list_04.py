import random


class RandomList(list):
    def get_random_element(self):
        element_index = random.randint(0, len(self) - 1)
        element = self[element_index]
        self.pop(element_index)
        return element

# rl = RandomList([10, 20, 30, 40, 50])
# while rl:
#     print(rl.get_random_element())
