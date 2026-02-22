class Vet:
    animals = []
    space = 5

    def __init__(self, name: str):
        self.name = name
        self.animals = []
    
    def register_animal(self, animal_name):
        self.animal_name = animal_name
        if Vet.space != 0:
            Vet.space-= 1
            Vet.animals.append(self.animal_name)
            self.animals.append(self.animal_name)
            return f"{self.animal_name} registered in the clinic"
        else:
            return f"Not enough space"
    
    def unregister_animal(self, animal_name):
        self.animal_name = animal_name
        if self.animal_name in self.animals:
            Vet.space += 1
            Vet.animals.remove(self.animal_name)
            self.animals.remove(self.animal_name)
            return f"{self.animal_name} unregistered successfully"
        else:
            return f"{self.animal_name} not in the clinic"
    
    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"
    
peter = Vet("Peter")

george = Vet("George")

print(peter.register_animal("Tom"))

print(george.register_animal("Cory"))

print(peter.register_animal("Fishy"))

print(peter.register_animal("Bobby"))

print(george.register_animal("Kay"))

print(george.unregister_animal("Cory"))

print(peter.register_animal("Kitty"))

print(peter.unregister_animal("Molly"))

print(peter.unregister_animal("Kitty"))

print(peter.info())

print(george.info()) 

    

    
        