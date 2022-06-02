class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.__data = iter(self.dictionary.items())

    def __iter__(self):
        self.__data = iter(self.dictionary.items())
        return self

    def __next__(self):
        result = next(self.__data)
        return result


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
