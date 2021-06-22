class Zoo:
    def __init__(self, name, budget, animal_capacity,
                 workers_capacity):
        self.name = name
        self.animals = []
        self.workers = []
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif len(self.animals) < self.__animal_capacity and self.__budget < price:
            return f"Not enough budget"

        return f"Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        # try:
        #     searched_worker = [w for w in self.workers if w.name == worker_name][0]
        #     if searched_worker:
        #         self.workers.remove(searched_worker)
        #         return f"{worker_name} fired successfully"
        #
        # except IndexError:
        #     return f"There is no {worker_name} in the zoo"

        searched_worker = [w for w in self.workers if w.name == worker_name]
        if searched_worker:
            workers_left = [w for w in self.workers if not w.name == worker_name]
            self.workers = workers_left
            return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        money_to_pay = sum([s.salary for s in self.workers])
        if self.__budget >= money_to_pay:
            self.__budget -= money_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_for_tend = sum(
            [a.get_needs() for a in self.animals])
        if self.__budget >= money_for_tend:
            self.__budget -= money_for_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def return_animal_data(self, name):
        result2 = "".join('\n'.join([repr(a) for a in self.animals if a.__class__.__name__ == name]))
        return result2

    def return_worker_data(self, name):
        result2 = "".join('\n'.join([repr(w) for w in self.workers if w.__class__.__name__ == name]))
        return result2

    def animals_status(self):
        result = f"You have {len(self.animals)} animals" \
                 f"\n----- {len([l for l in self.animals if l.__class__.__name__ == 'Lion'])} Lions:\n"
        result += Zoo.return_animal_data(self, "Lion")
        result += "\n"
        result += f"----- {len([t for t in self.animals if t.__class__.__name__ == 'Tiger'])} Tigers:\n"
        result += Zoo.return_animal_data(self, "Tiger")
        result += "\n"
        result += f"----- {len([c for c in self.animals if c.__class__.__name__ == 'Cheetah'])} Cheetahs:\n"
        result += Zoo.return_animal_data(self, "Cheetah")
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers" \
                 f"\n----- {len([w for w in self.workers if w.__class__.__name__ == 'Keeper'])} Keepers:\n"
        result += Zoo.return_worker_data(self, "Keeper")
        result += "\n"
        result += f"----- {len([w for w in self.workers if w.__class__.__name__ == 'Caretaker'])} Caretakers:\n"
        result += Zoo.return_worker_data(self, "Caretaker")
        result += "\n"
        result += f"----- {len([w for w in self.workers if w.__class__.__name__ == 'Vet'])} Vets:\n"
        result += Zoo.return_worker_data(self, "Vet")
        return result

# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
#            Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
#            Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
#            Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
