class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum([worker.salary for worker in self.workers])
        if self.__budget < salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        tend = sum([animal.get_needs() for animal in self.animals])
        if self.__budget < tend:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= tend
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [animal for animal in self.animals if animal.__class__.__name__ == "Lion"]
        tigers = [animal for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == "Cheetah"]
        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        result += "\n".join([repr(lion) for lion in lions])
        result += f"\n----- {len(tigers)} Tigers:\n"
        result += "\n".join([repr(tiger) for tiger in tigers])
        result += f"\n----- {len(cheetahs)} Cheetahs:\n"
        result += "\n".join([repr(cheetah) for cheetah in cheetahs])
        return result

    def workers_status(self):
        keepers = [worker for worker in self.workers if worker.__class__.__name__ == "Keeper"]
        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        vets = [worker for worker in self.workers if worker.__class__.__name__ == "Vet"]
        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += "\n".join([repr(keeper) for keeper in keepers])
        result += f"\n----- {len(caretakers)} Caretakers:\n"
        result += "\n".join([repr(caretaker) for caretaker in caretakers])
        result += f"\n----- {len(vets)} Vets:\n"
        result += "\n".join([repr(vet) for vet in vets])
        return result
