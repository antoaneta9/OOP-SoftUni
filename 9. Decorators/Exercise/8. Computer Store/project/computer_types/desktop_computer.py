from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    AVAILABLE_PROCESSORS = {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800,
    }

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(
                f"{processor} is not compatible with desktop computer "
                f"{self.manufacturer} {self.model}!"
            )

        if ram > 128 or ram < 2 or (ram & (ram - 1)) != 0:
            raise ValueError(
                f"{ram}GB RAM is not compatible with desktop computer "
                f"{self.manufacturer} {self.model}!"
            )

        ram_price = ram.bit_length() - 1
        ram_price *= 100

        self.processor = processor
        self.ram = ram
        self.price = self.AVAILABLE_PROCESSORS[processor] + ram_price

        return (
            f"Created {self.manufacturer} {self.model} with {self.processor} "
            f"and {self.ram}GB RAM for {self.price}$."
        )