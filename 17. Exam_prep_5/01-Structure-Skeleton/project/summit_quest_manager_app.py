from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.climbers.arctic_climber import ArcticClimber

from project.peaks.base_peak import BasePeak
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak

class SummitQuestManagerApp:
    _VALID_CLIMBERS = [
        "ArcticClimber",
        "SummitClimber"
    ]

    _VALID_PEAKS = [
        'ArcticPeak',
        'SummitPeak',
    ]

    def __init__(self):
        self.climbers: list[BaseClimber] = []
        self.peaks: list[BasePeak] = []

    #VALIDATIONS
    def __find_climber_name(self, name:str):
        return next((c for c in self.climbers if c.name == name), None)
    def __find_peak_name(self, name:str):
        return next((p for p in self.peaks if p.name == name), None)

    #METHODS
    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self._VALID_CLIMBERS:
            return f"{climber_type} doesn't exist in our register."
        if self.__find_climber_name(climber_name) is not None:
            return f"{climber_name} has been already registered."
        climber = ''
        if climber_type == 'ArcticClimber':
            climber = ArcticClimber(climber_name)
        elif climber_type == 'SummitClimber':
            climber = SummitClimber(climber_name)
        self.climbers.append(climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type:str, peak_name:str, peak_elevation:int):
        if peak_type not in self._VALID_PEAKS:
            return f"{peak_type} is an unknown type of peak."
        peak = ''
        if peak_type == 'SummitPeak':
            peak = SummitPeak(peak_name, peak_elevation)
        elif peak_type == 'ArcticPeak':
            peak = ArcticPeak(peak_name, peak_elevation)
        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name:str, peak_name:str, gear: list[str]):
        climber = self.__find_climber_name(climber_name)
        peak = self.__find_peak_name(peak_name)
        recommended = peak.get_recommended_gear()
        missing_gear = sorted([item for item in recommended if item not in gear])
        if not missing_gear:
            climber.is_prepared = True
            return f"{climber_name} is prepared to climb {peak_name}."
        climber.is_prepared = False
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(missing_gear)}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self.__find_climber_name(climber_name)
        peak = self.__find_peak_name(peak_name)
        if climber is None:
            return f"Climber {climber_name} is not registered yet."
        if peak is None:
            return f"Peak {peak_name} is not part of the wish list."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        if not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."
        climber.climb(peak)
        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

    def get_statistics(self):
        climbers_with_peaks = [c for c in self.climbers if c.conquered_peaks]
        sorted_climbers = sorted(climbers_with_peaks, key=lambda c: (-len(c.conquered_peaks), c.name))
        for c in sorted_climbers:
            c.conquered_peaks.sort()
        all_peaks = set()
        for c in sorted_climbers:
            all_peaks.update(c.conquered_peaks)
        result = []
        result.append(f"Total climbed peaks: {len(all_peaks)}")
        result.append("**Climber's statistics:**")
        for c in sorted_climbers:
            result.append(str(c))
        return "\n".join(result).strip()

# Create an instance of SummitQuestManagerApp
climbing_app = SummitQuestManagerApp()

# Register climbers
print(climbing_app.register_climber("ArcticClimber", "Alice"))
print(climbing_app.register_climber("SummitClimber", "Bob"))
print(climbing_app.register_climber("ExtremeClimber", "Dave"))
print(climbing_app.register_climber("ArcticClimber", "Charlie"))
print(climbing_app.register_climber("ArcticClimber", "Alice"))
print(climbing_app.register_climber("SummitClimber", "Eve"))
print(climbing_app.register_climber("SummitClimber", "Frank"))

# Add peaks to the wish list
print(climbing_app.peak_wish_list("ArcticPeak", "MountEverest", 4000))
print(climbing_app.peak_wish_list("SummitPeak", "K2", 3000))
print(climbing_app.peak_wish_list("ArcticPeak", "Denali", 2500))
print(climbing_app.peak_wish_list("UnchartedPeak", "MysteryMountain", 2000))

# Prepare climbers for climbing
print(climbing_app.check_gear("Alice", "MountEverest", ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]))
print(climbing_app.check_gear("Bob", "K2", ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]))
print(climbing_app.check_gear("Charlie", "Denali", ["Ice axe", "Crampons"]))

# Perform climbing
print(climbing_app.perform_climbing("Alice", "MountEverest"))
print(climbing_app.perform_climbing("Bob", "K2"))
print(climbing_app.perform_climbing("Kelly", "Denali"))
print(climbing_app.perform_climbing("Alice", "K2"))
print(climbing_app.perform_climbing("Alice", "MysteryMountain"))
print(climbing_app.perform_climbing("Eve", "MountEverest"))
print(climbing_app.perform_climbing("Charlie", "MountEverest"))
print(climbing_app.perform_climbing("Frank", "K2"))
print(climbing_app.perform_climbing("Frank", "Denali"))
print(climbing_app.perform_climbing("Frank", "MountEverest"))

# Get statistics
print(climbing_app.get_statistics())