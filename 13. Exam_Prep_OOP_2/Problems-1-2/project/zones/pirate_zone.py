from project.zones.base_zone import BaseZone
from project.battleships.royal_battleship import RoyalBattleship


class PirateZone(BaseZone):
    INITIAL_VOLUME = 8

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self):
        return self._build_zone_info("Pirate", RoyalBattleship, "Royal Battleships")
