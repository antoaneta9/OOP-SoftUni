from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak

class ArcticClimber(BaseClimber):
    _STRENGTH = 200
    def __init__(self, name: str):
        super().__init__(name, self._STRENGTH)

    def can_climb(self):
        if self.strength >= 100:
            return True
        else:
            return False

    def climb(self, peak: BasePeak):
        if self.can_climb():
            if peak.difficulty_level== 'Extreme':
                self.strength -= 20 * 2
            else:
                self.strength -= 20 * 1.5
            self.conquered_peaks.append(peak.name)


