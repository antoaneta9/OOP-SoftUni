import re
from project.equipment.base_equipment import BaseEquipment
from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad
from project.teams.base_team import BaseTeam
from project.teams.outdoor_team import OutdoorTeam
from project.teams.indoor_team import IndoorTeam

class Tournament:
    def __init__(self, name:str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: list[BaseEquipment] = []
        self.teams: list[BaseTeam] = []

    #VALIDATIONS
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        regex = r'^[A-Za-z0-9]+$'
        if not re.match(regex, value):
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    #METHODS
    _VALID_TYPES_EQUIPMENT = [
        "KneePad",
        "ElbowPad"
    ]
    _VALID_TEAM_TYPES = [
        "OutdoorTeam",
        "IndoorTeam"
    ]
    def add_equipment(self, equipment_type:str):
        if equipment_type not in self._VALID_TYPES_EQUIPMENT:
            raise Exception("Invalid equipment type!")
        equipment = ''
        if equipment_type == "KneePad":
            equipment = KneePad()
        elif equipment_type == "ElbowPad":
            equipment = ElbowPad()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def __check_team_name(self, name:str):
        return next((n for n in self.teams if n.name == name), None)

    def add_team(self,team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self._VALID_TEAM_TYPES:
            raise Exception("Invalid team type!")
        if self.__check_team_name(team_name) is not None:
            pass
        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."
        team = ''
        if team_type == "OutdoorTeam":
            team = OutdoorTeam(team_name, country, advantage)
        elif team_type == "IndoorTeam":
            team = IndoorTeam(team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."


    def sell_equipment(self, equipment_type:str, team_name:str):
        equipment = next((e for e in reversed(self.equipment) if e.__class__.__name__ == equipment_type), None)
        team = self.__check_team_name(team_name)
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name:str):
        if self.__check_team_name(team_name) is None:
            raise Exception('No such team!')
        team = self.__check_team_name(team_name)
        if team.wins > 0:
            raise Exception(f"The team has {wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f'Successfully removed {team_name}.'

    def increase_equipment_price(self, equipment_type:str):
        count = 0
        for e in self.equipment:
            if e.__class__.__name__ == equipment_type:
                e.increase_price()
                count += 1
        return f"Successfully changed {count}pcs of equipment."

    def play(self, team_name1:str, team_name2:str):
        team_1 = self.__check_team_name(team_name1)
        team_2 = self.__check_team_name(team_name2)
        if team_1.__class__.__name__ != team_2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")
        team_1_result = team_1.advantage + sum(e.protection for e in team_1.equipment)
        team_2_result = team_2.advantage + sum(e.protection for e in team_2.equipment)
        if team_1_result > team_2_result:
            team_1.win()
            return f"The winner is {team_1.name}."
        if team_2_result > team_1_result:
            team_2.win()
            return f"The winner is {team_2.name}."
        return "No winner in this game."


    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [
            f"Tournament: {self.name}",
            f"Number of Teams: {len(self.teams)}",
            "Teams:"
        ]
        for team in sorted_teams:
            result.append(team.get_statistics())
        return "\n".join(result)

t = Tournament('SoftUniada2023', 2)

print(t.add_equipment('KneePad'))
print(t.add_equipment('ElbowPad'))

print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))

print(t.sell_equipment('KneePad', 'Spartak'))

print(t.remove_team('Levski'))
print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))

print(t.increase_equipment_price('ElbowPad'))
print(t.increase_equipment_price('KneePad'))

print(t.play('Lokomotiv', 'Spartak'))

print(t.get_statistics())
