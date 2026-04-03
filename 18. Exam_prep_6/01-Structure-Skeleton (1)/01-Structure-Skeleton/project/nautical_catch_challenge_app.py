from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish

from project.divers.base_diver import BaseDiver
from project.divers.scuba_diver import ScubaDiver
from project.divers.free_diver import FreeDiver


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers: list[BaseDiver] = []
        self.fish_list: list[BaseFish] = []

    _DIVERS_VALID_TYPES = [
        'ScubaDiver',
        'FreeDiver',
    ]

    _FISH_VALID_TYPES = [
        'PredatoryFish',
        'DeepSeaFish',
    ]

    def __check_diver_name(self, name:str):
        return next((d for d in self.divers if d.name == name), None)
    def __check_fish_name(self, name:str):
        return next((f for f in self.fish_list if f.name == name), None)

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self._DIVERS_VALID_TYPES:
            return f"{diver_type} is not allowed in our competition."
        if self.__check_diver_name(diver_name) is not None:
            return f"{diver_name} is already a participant."
        diver = ''
        if diver_type == 'ScubaDiver':
            diver = ScubaDiver(diver_name)
        elif diver_type == 'FreeDiver':
            diver = FreeDiver(diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self._FISH_VALID_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."
        if self.__check_fish_name(fish_name) is not None:
            return f"{fish_name} is already permitted."
        fish = ''
        if fish_type == 'PredatoryFish':
            fish = PredatoryFish(fish_name, points)
        elif fish_type == 'DeepSeaFish':
            fish = DeepSeaFish(fish_name, points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        #VALIDATIONS
        diver = self.__check_diver_name(diver_name)
        if diver is None:
            return f"{diver_name} is not registered for the competition."
        fish = self.__check_fish_name(fish_name)
        if fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."
        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."
        #CONDITIONS
        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0 and not diver.has_health_issue:
                diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."
        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0 and not diver.has_health_issue:
                    diver.update_health_status()
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                if diver.oxygen_level == 0 and not diver.has_health_issue:
                    diver.update_health_status()
                return f"{diver_name} missed a good {fish_name}."
        diver.hit(fish)
        if diver.oxygen_level == 0 and not diver.has_health_issue:
            diver.update_health_status()
        return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        sick_divers = [d for d in self.divers if d.has_health_issue]
        for diver in sick_divers:
            diver.update_health_status()
            diver.renew_oxy()
        return f"Divers recovered: {len(sick_divers)}"

    def diver_catch_report(self, diver_name: str):
        diver = self.__check_diver_name(diver_name)
        result = [f"**{diver_name} Catch Report**"]
        for fish in diver.catch:
            result.append(f"{fish.fish_details()}")
        return '\n'.join(result)

    def competition_statistics(self):
        healthy_divers = [d for d in self.divers if not d.has_health_issue]
        result = [f"**Nautical Catch Challenge Statistics**"]
        for diver in sorted(healthy_divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name)):
            result.append(str(diver))
        return '\n'.join(result)
nautical_catch_challenge = NauticalCatchChallengeApp()

# Dive into competition
print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "MaxineHarper"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "JamalCarter"))
print(nautical_catch_challenge.dive_into_competition("SkyDiver", "FionaBennett"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "OscarWallace"))
print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "LilaMoreno"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "LilaMoreno"))

# Swim into competition
print(nautical_catch_challenge.swim_into_competition("ReefFish", "AzureDamselfish", 8.7))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "BluestripeSnapper", 6.3))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "YellowtailSurgeonfish", 5.0))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Barracuda", 9.2))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Coryphaena", 9.7))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Bluefish", 4.4))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "SwordFish", 10.0))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Mahi-Mahi", 9.1))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Tuna", 8.5))
print(nautical_catch_challenge.swim_into_competition("AquariumFish", "SilverArowana", 3.3))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Barracuda", 8.6))

# Conduct fishing competitions
print(nautical_catch_challenge.chase_fish("FionaBennett", "AzureDamselfish", False))
print(nautical_catch_challenge.chase_fish("JamalCarter", "SilverArowana", True))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "YellowtailSurgeonfish", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Tuna", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Coryphaena", True))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "BluestripeSnapper", True))
print(nautical_catch_challenge.chase_fish("OscarWallace", "Barracuda", False))
print(nautical_catch_challenge.chase_fish("OscarWallace", "YellowtailSurgeonfish", False))
print(nautical_catch_challenge.chase_fish("OscarWallace", "Tuna", True))
print(nautical_catch_challenge.chase_fish("JamalCarter", "Barracuda", True))
print(nautical_catch_challenge.chase_fish("JamalCarter", "YellowtailSurgeonfish", True))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))

# Check health recovery
print(nautical_catch_challenge.health_recovery())

# Conduct fishing competitions
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))

# View catch reports
print(nautical_catch_challenge.diver_catch_report("LilaMoreno"))

# View competition statistics
print(nautical_catch_challenge.competition_statistics())
