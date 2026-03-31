from project.zones.base_zone import BaseZone
from project.battleships.pirate_battleship import PirateBattleship


class RoyalZone(BaseZone):
    INITIAL_VOLUME = 10

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self):
        return self._build_zone_info("Royal", PirateBattleship, "Pirate Battleships")