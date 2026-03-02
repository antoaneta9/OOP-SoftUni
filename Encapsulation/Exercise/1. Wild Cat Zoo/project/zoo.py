from project.animal import Animal
from project.worker import Worker

from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.caretaker import Caretaker
from project.vet import Vet

class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal]= []
        self.workers:list[Worker] = []

    def add_animal(self, animal: Animal, price: int):
        if len(self.animals) < self.__animal_capacity:
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            else:
                return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"


    def pay_workers(self):
        total_salaries = sum(w.salary for w in self.workers)
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_care_cost = sum(a.money_for_care for a in self.animals)
        if self.__budget >= total_care_cost:
            self.__budget -= total_care_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_animals_count = len(self.animals)

        lions = [a for a in self.animals if isinstance(a, Lion)]
        tigers = [a for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a for a in self.animals if isinstance(a, Cheetah)]

        result = [f"You have {total_animals_count} animals"]

        result.append(f"----- {len(lions)} Lions:")
        result.extend(repr(lion) for lion in lions)

        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(repr(tiger) for tiger in tigers)

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(repr(cheetah) for cheetah in cheetahs)

        return "\n".join(result)

    def workers_status(self):
        total_workers_count = len(self.workers)
        keepers = [w for w in self.workers if isinstance(w, Keeper)]
        caretakers = [w for w in self.workers if isinstance(w, Caretaker)]
        vets = [w for w in self.workers if isinstance(w, Vet)]
        result = [f"You have {total_workers_count} workers"]
        result.append(f"----- {len(keepers)} Keepers:")
        result.extend(repr(keeper) for keeper in keepers)
        result.append(f"----- {len(caretakers)} Caretakers:")
        result.extend(repr(caretaker) for caretaker in caretakers)
        result.append(f"----- {len(vets)} Vets:")
        result.extend(repr(vet) for vet in vets)

        return "\n".join(result)

