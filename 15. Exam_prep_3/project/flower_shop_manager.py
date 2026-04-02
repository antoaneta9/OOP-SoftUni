from project.plants.base_plant import BasePlant
from project.clients.base_client import BaseClient

from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant

from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.clients.base_client import BaseClient

class FlowerShopManager:
    _VALID_TYPE_PLANTS = [
        'Flower',
        'LeafPlant'
    ]

    _VALID_TYPE_CLIENTS = [
        'RegularClient',
        'BusinessClient'
    ]

    def __init__(self):
        self.income: float = 0.0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        if plant_type not in self._VALID_TYPE_PLANTS:
            raise ValueError('Unknown plant type!')
        if plant_type == 'Flower':
            plant = Flower(plant_name, plant_price, plant_water_needed, plant_extra_data)
            self.plants.append(plant)
        elif plant_type == 'LeafPlant':
            plant = LeafPlant(plant_name, plant_price, plant_water_needed, plant_extra_data)
            self.plants.append(plant)
        return f"{plant_name} is added to the shop as {plant_type}."


    def add_client(self, client_type:str, client_name:str, client_phone_number:str):
        if client_type not in self._VALID_TYPE_CLIENTS:
            raise ValueError('Unknown client type!')
        if any(c.phone_number == client_phone_number for c in self.clients):
            raise ValueError("This phone number has been used!")
        if client_type == 'BusinessClient':
            client = BusinessClient(client_name, client_phone_number)
            self.clients.append(client)
        elif client_type == 'RegularClient':
            client = RegularClient(client_name, client_phone_number)
            self.clients.append(client)
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = next((c for c in self.clients if c.phone_number == client_phone_number), None)
        if client is None:
            raise ValueError('Client not found!')
        matching_plants = [p for p in self.plants if p.name == plant_name]
        if not matching_plants:
            raise ValueError('Plants not found!')

        if len(matching_plants) < plant_quantity:
            return 'Not enough plant quantity.'
        plants_to_sell = matching_plants[:plant_quantity]
        total_price = sum(p.price for p in plants_to_sell)
        order_amount = total_price * (1-client.discount / 100)
        removed = 0
        for plant in self.plants[:]:
            if plant.name == plant_name and removed < plant_quantity:
                self.plants.remove(plant)
                removed += 1
        self.income += order_amount
        client.update_total_orders()
        client.update_discount()
        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"

    def remove_plant(self, plant_name:str):
        plant = next((p for p in self.plants if p.name == plant_name), None)
        if plant is None:
            return 'No such plant name.'
        self.plants.remove(plant)
        return f"Removed {plant.plant_details()}"

    def remove_clients(self):
        removed = 0
        for client in self.clients[:]:
            if client.total_orders == 0:
                self.clients.remove(client)
                removed += 1
        return f"{removed} client/s removed."

    def shop_report(self):
        result = ["~Flower Shop Report~"]
        result.append(f"Income: {self.income:.2f}")
        total_orders = sum(client.total_orders for client in self.clients)
        result.append(f"Count of orders: {total_orders}")
        plants_by_name = {}
        for plant in self.plants:
            if plant.name not in plants_by_name:
                plants_by_name[plant.name] = 0
            plants_by_name[plant.name] += 1

        result.append(f"~~Unsold plants: {len(self.plants)}~~")
        sorted_plants = sorted(
            plants_by_name.items(),
            key=lambda x: (-x[1], x[0])
        )
        for plant_name, count in sorted_plants:
            result.append(f"{plant_name}: {count}")
        result.append(f"~~Clients number: {len(self.clients)}~~")
        sorted_clients = sorted(
            self.clients,
            key=lambda c: (-c.total_orders, c.phone_number)
        )
        for client in sorted_clients:
            result.append(client.client_details())
        return "\n".join(result)

# Create an instance of FlowerShopManager
manager = FlowerShopManager()

# Add plants
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Tulip", 12.00, 150, "Spring"))
print(manager.add_plant("Flower", "Tulip", 12.00, 150, "Spring"))
print(manager.add_plant("Flower", "Lily", 20.00, 180, "Summer"))
print(manager.add_plant("LeafPlant", "Cactus", 8.00, 50, "M"))
print(manager.add_plant("LeafPlant", "Cactus", 8.00, 50, "M"))
print(manager.add_plant("LeafPlant", "Fern", 6.50, 100, "S"))
print(manager.add_plant("LeafPlant", "Fern", 6.50, 100, "S"))
print(manager.add_plant("LeafPlant", "Fern", 6.50, 100, "S"))
print(manager.add_plant("LeafPlant", "Snake Plant", 12.00, 200, "L"))
print(manager.add_plant("LeafPlant", "Snake Plant", 12.00, 200, "L"))
print()

# Add clients
print(manager.add_client("RegularClient", "Alice Johnson", "1234567890"))
print(manager.add_client("RegularClient", "Bob Smith", "0987654321"))
print(manager.add_client("BusinessClient", "Greenhouse Inc.", "5647382910"))
print(manager.add_client("BusinessClient", "CoolGarden Plc.", "9647382910"))
print(manager.add_client("RegularClient", "Peter Johnson", "382910"))
print()

# Perform sales
print(manager.sell_plants("1234567890", "Rose", 3))
print(manager.sell_plants("0987654321", "Tulip", 2))
print(manager.sell_plants("5647382910", "Cactus", 1))
print()

# Get shop report
print(manager.shop_report())
print()

# Perform sales
print(manager.sell_plants("1234567890", "Lily", 2))
print(manager.sell_plants("0987654321", "Fern", 1))
print(manager.sell_plants("5647382910", "Snake Plant", 2))
print()

# Remove a plant
print(manager.remove_plant("Nonexistent"))
print(manager.remove_plant("Cactus"))
print()

# Get shop report
print(manager.shop_report())
print()

# Remove clients who have no orders
print(manager.remove_clients())
print(manager.remove_clients())

