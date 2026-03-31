from abc import ABC, abstractmethod
class Computer(ABC):
    VALID_TYPES = ["Laptop", "Desktop Computer"]

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str):
        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")
        self._manufacturer = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value: str):
        if value.strip() == "":
            raise ValueError("Model name cannot be empty.")
        self._model = value

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        pass

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

