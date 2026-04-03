from abc import ABC, abstractmethod
from project.equipment.base_equipment import BaseEquipment
import math
class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins: int = 0
        self.equipment: list[BaseEquipment] = []

    #VALIDATIONS
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage
    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    #METHODS
    @abstractmethod
    def win(self):
        pass
    def get_statistics(self):
        total_price_equipment = sum(p.price for p in self.equipment)
        all_equipment_protection = sum(e.protection for e in self.equipment)
        avg_team_protection = math.floor(all_equipment_protection / len(self.equipment)) if self.equipment else 0
        return f"Name: {self.name}\nCountry: {self.country}\nAdvantage: {self.advantage} points\nBudget: {self.budget:.2f}EUR\nWins: {self.wins}\nTotal Equipment Price: {total_price_equipment:.2f}\nAverage Protection: {avg_team_protection}"

