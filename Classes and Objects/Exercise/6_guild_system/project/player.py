
class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.skills = {}
        self.name = name
        self.hp = hp
        self.mp = mp
        self.guild = 'Unaffiliated'
    
    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        else:
            return 'Skill already added'

    def player_info(self):
        result = []
        result.append(f"Name: {self.name}")
        result.append(f"Guild: {self.guild}")
        result.append(f"HP: {self.hp}")
        result.append(f"MP: {self.mp}")
        for sk, mn in self.skills.items():
            result.append(f"==={sk} - {mn}")
        return '\n'.join(result)



        