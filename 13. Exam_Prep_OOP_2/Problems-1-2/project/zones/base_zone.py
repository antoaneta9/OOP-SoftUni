from abc import ABC, abstractmethod

from project.battleships.base_battleship import BaseBattleship


class BaseZone(ABC):
    def __init__(self, code: str, volume: int):
        self.code = code
        self.volume = volume
        self.ships: list[BaseBattleship] = []

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self.__code = value

    def get_ships(self):
        return sorted(self.ships, key=lambda ship: (-ship.hit_strength, ship.name))

    def _build_zone_info(self, zone_type: str, counted_class, counted_class_name: str):
        ships = self.get_ships()
        total_count = len(ships)
        counted_ships = sum(isinstance(ship, counted_class) for ship in ships)

        result = [
            f"@{zone_type} Zone Statistics@",
            f"Code: {self.code}; Volume: {self.volume}",
            f"Battleships currently in the {zone_type} Zone: {total_count}, "
            f"{counted_ships} out of them are {counted_class_name}."
        ]

        if ships:
            ship_names = ", ".join(ship.name for ship in ships)
            result.append(f"#{ship_names}#")

        return "\n".join(result)

    @abstractmethod
    def zone_info(self):
        pass
