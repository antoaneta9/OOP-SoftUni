from abc import ABC, abstractmethod
import re
from project.artifacts.base_artifact import BaseArtifact


class BaseCollector(ABC):
    def __init__(self, name: str, available_money: float, available_space: int):
        self.name = name
        self.available_money = available_money
        self.available_space = available_space
        self.purchased_artifacts: list[BaseArtifact] = []

    # VALIDATIONS
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, value):
        regex = r'^[A-Za-z0-9]+(?: [A-Za-z0-9]+)*$'
        if not re.fullmatch(regex, value):
            raise ValueError('Collector name must contain letters, numbers, and optional white spaces between them!')
        self.__name = value

    @property
    def available_money(self):
        return self.__available_money
    @available_money.setter
    def available_money(self, value):
        if value < 0.0:
            raise ValueError('A collector cannot have a negative amount of money!')
        self.__available_money = value

    @property
    def available_space(self):
        return self.__available_space
    @available_space.setter
    def available_space(self, value):
        if value < 0:
            raise ValueError("A collector cannot have a negative space available for exhibitions!")
        self.__available_space = value
    #METHODS
    @abstractmethod
    def increase_money(self):
        pass

    def can_purchase(self, artifact_price: float, artifact_space_required: int):
        if (self.available_money >= artifact_price) and (self.available_space >= artifact_space_required):
            return True
        else:
            return False

    def __str__(self):
        artifacts = ', '.join(f.name for f in sorted(self.purchased_artifacts, key=lambda x: x.name, reverse= True))
        artifacts_if_none = artifacts if artifacts else 'none'
        return f"Collector name: {self.name}; Money available: {self.available_money:.2f}; Space available: {self.available_space}; Artifacts: {artifacts_if_none}"


