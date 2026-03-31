
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop
class ComputerStoreApp:
    VALID_COMPUTER_TYPES = {
        "Desktop Computer": DesktopComputer,
        "Laptop": Laptop,
    }

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(
        self,
        type_computer: str,
        manufacturer: str,
        model: str,
        processor: str,
        ram: int
    ):
        if type_computer not in self.VALID_COMPUTER_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        computer = self.VALID_COMPUTER_TYPES[type_computer](manufacturer, model)
        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        available_computers = [
            computer for computer in self.warehouse
            if computer.price <= client_budget
            and computer.processor == wanted_processor
            and computer.ram >= wanted_ram
        ]

        if not available_computers:
            raise Exception("Sorry, we don't have a computer for you.")

        computer = min(available_computers, key=lambda c: c.price)
        self.warehouse.remove(computer)
        self.profits += client_budget - computer.price

        return f"{computer} sold for {client_budget}$."