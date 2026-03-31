from project.computer_types.computer import Computer

class Laptop(Computer):
    AVAILABLE_PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200,
    }

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(
                f"{processor} is not compatible with laptop "
                f"{self.manufacturer} {self.model}!"
            )

        if ram > 64 or ram < 2 or (ram & (ram - 1)) != 0:
            raise ValueError(
                f"{ram}GB RAM is not compatible with laptop "
                f"{self.manufacturer} {self.model}!"
            )

        ram_price = (ram.bit_length() - 1) * 100

        self.processor = processor
        self.ram = ram
        self.price = self.AVAILABLE_PROCESSORS[processor] + ram_price

        return (
            f"Created {self.manufacturer} {self.model} with {self.processor} "
            f"and {self.ram}GB RAM for {self.price}$."
        )