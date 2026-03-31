class Employee:
    def __init__(self, id: int, first_name: str, last_name: str, salary: int):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    def get_annual_salary(self):
        return self.salary * 12
    def raise_salary(self, amount):
        self.salary += amount
        return self.salary
p1 = Employee(123456, "Rosen", 'Rosenov', 2500)
print(p1.get_full_name())
print(p1.get_annual_salary())
print(p1.raise_salary(2500))
print(p1.get_annual_salary())