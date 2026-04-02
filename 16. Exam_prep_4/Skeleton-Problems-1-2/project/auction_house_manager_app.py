from project.collectors.base_collector import BaseCollector
from project.artifacts.base_artifact import BaseArtifact

from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact

from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector

class AuctionHouseManagerApp:
    _VALID_ARTIFACT_TYPES = [
        "RenaissanceArtifact",
        "ContemporaryArtifact"
    ]

    _VALID_COLLECTOR_TYPES = [
        "Museum",
        "PrivateCollector"
    ]

    def __init__(self):
        self.artifacts: List[BaseArtifact] = []
        self.collectors: List[BaseCollector] = []

    def __find_artifact_by_name(self, artifact_name: str):
        return next((a for a in self.artifacts if a.name == artifact_name), None)

    def __find_collector_by_name(self, collector_name: str):
        return next((c for c in self.collectors if c.name == collector_name), None)

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type not in self._VALID_ARTIFACT_TYPES:
            raise ValueError("Unknown artifact type!")

        if self.__find_artifact_by_name(artifact_name):
            raise ValueError(f"{artifact_name} has been already registered!")

        artifact = ''
        if artifact_type == 'RenaissanceArtifact':
            artifact = RenaissanceArtifact(artifact_name, artifact_price, artifact_space)
        elif artifact_type == 'ContemporaryArtifact':
            artifact = ContemporaryArtifact(artifact_name, artifact_price, artifact_space)
        self.artifacts.append(artifact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in self._VALID_COLLECTOR_TYPES:
            raise ValueError("Unknown collector type!")
        if self.__find_collector_by_name(collector_name):
            raise ValueError(f"{collector_name} has been already registered!")

        collector = ''
        if collector_type == 'Museum':
            collector = Museum(collector_name)
        elif collector_type == 'PrivateCollector':
            collector = PrivateCollector(collector_name)
        self.collectors.append(collector)
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector = self.__find_collector_by_name(collector_name)
        artifact = self.__find_artifact_by_name(artifact_name)
        if collector is None:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")
        if artifact is None:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if collector.can_purchase(artifact.price, artifact.space_required):
            self.artifacts.remove(artifact)
            collector.purchased_artifacts.append(artifact)
            collector.available_money -= artifact.price
            collector.available_space -= artifact.space_required
            return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."
        else:
            return 'Purchase is impossible.'

    def remove_artifact(self, artifact_name: str):
        artifact = self.__find_artifact_by_name(artifact_name)
        if not artifact:
            return 'No such artifact.'
        else:
            self.artifacts.remove(artifact)
            return f"Removed {artifact.artifact_information()}"

    def fundraising_campaigns(self, max_money:float):
        counter = 0
        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                counter += 1
        return f"{counter} collector/s increased their available money."

    def get_auction_report(self):
        sold_artifacts = sum(len(c.purchased_artifacts) for c in self.collectors)
        available_artifacts = len(self.artifacts)
        sorted_collectors = sorted(
            self.collectors,
            key=lambda c: (-len(c.purchased_artifacts), c.name)
        )
        result = [
            "**Auction statistics**",
            f"Total number of sold artifacts: {sold_artifacts}",
            f"Available artifacts for sale: {available_artifacts}",
            "***"
        ]
        result.extend(str(c) for c in sorted_collectors)
        return "\n".join(result)
#
# # Create an instance of AuctionHouseManagerApp
# manager = AuctionHouseManagerApp()
# # Register artifacts
# print(manager.register_artifact("RenaissanceArtifact", "Kohinoor", 5000.0, 10))
# print(manager.register_artifact("RenaissanceArtifact", "Zelda", 5000.0, 10))
# print(manager.register_artifact("RenaissanceArtifact", "Mona Lisa", 10000.0, 100))
# print(manager.register_artifact("ContemporaryArtifact", "The Scream", 2000.0, 1000))
# print(manager.register_artifact("ContemporaryArtifact", "Untitled", 32000.0, 90))
# print()
# # Register collectors
# print(manager.register_collector("PrivateCollector", "Josh Smith"))
# print(manager.register_collector("Museum", "Louvre"))
# print(manager.register_collector("Museum", "Hermitage"))
# print()
# # Perform purchases
# print(manager.perform_purchase("Josh Smith", "Mona Lisa"))
# print(manager.perform_purchase("Louvre", "Kohinoor"))
# print(manager.perform_purchase("Josh Smith", "Zelda"))
# print(manager.perform_purchase("Josh Smith", "The Scream"))
# print(manager.perform_purchase("Josh Smith", "Untitled"))
# print()
# # Remove artifact
# print(manager.remove_artifact("The Scream"))
# print(manager.remove_artifact("Nonexistent"))
# print()
# # Start fund-raising campaigns
# print(manager.fundraising_campaigns(10000.0))
# print()
# # Get auction report
# print(manager.get_auction_report())
# print()
#
# # Remove artifact
# print(manager.remove_artifact("Untitled"))


