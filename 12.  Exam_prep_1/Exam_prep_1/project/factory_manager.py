from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in ["Chair", "HobbyHorse"]:
            raise Exception("Invalid product type!")
        if product_type == "Chair":
            product = Chair(model, price)
        else:
            product = HobbyHorse(model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in ["FurnitureStore", "ToyStore"]:
            raise Exception(f"{store_type} is an invalid type of store!")
        if store_type == "FurnitureStore":
            store = FurnitureStore(name, location)
        else:
            store = ToyStore(name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."
        suitable_products = []
        if store.store_type == "FurnitureStore":
            suitable_products = [p for p in products if p.sub_type == "Furniture"]
        elif store.store_type == "ToyStore":
            suitable_products = [p for p in products if p.sub_type == "Toys"]
        if not suitable_products:
            return "Products do not match in type. Nothing sold."
        for product in suitable_products:
            store.products.append(product)
            self.products.remove(product)
        store.capacity -= len(suitable_products)
        self.income += sum(product.price for product in suitable_products)
        return f"Store {store.name} successfully purchased {len(suitable_products)} items."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if store is None:
            raise Exception("No such store!")
        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."
        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str):
        filtered_products = [p for p in self.products if p.model == product_model]
        for product in filtered_products:
            product.discount()
        return f"Discount applied to {len(filtered_products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if store is None:
            return "There is no store registered under this name!"
        return store.store_stats()

    def statistics(self):
        result = [
            f"Factory: {self.name}",
            f"Income: {self.income:.2f}",
            "***Products Statistics***",
            f"Unsold Products: {len(self.products)}. Total net price: {sum(p.price for p in self.products):.2f}"
        ]
        products_by_model = {}
        for product in self.products:
            if product.model not in products_by_model:
                products_by_model[product.model] = 0
            products_by_model[product.model] += 1
        for model in sorted(products_by_model):
            result.append(f"{model}: {products_by_model[model]}")
        result.append(f"***Partner Stores: {len(self.stores)}***")
        for store in sorted(self.stores, key=lambda s: s.name):
            result.append(store.name)
        return "\n".join(result)
factory_manager = FactoryManager("Cool Factory")

# Produce some items
print(factory_manager.produce_item("Chair", "Classic", 80.0))
print(factory_manager.produce_item("Chair", "Modern", 100.0))
print(factory_manager.produce_item("Chair", "Modern", 200.0))
print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 120.0))
print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 100.0))
print()

# Register new stores
print(factory_manager.register_new_store("FurnitureStore", "Furniture Outlet", "SOF"))
print(factory_manager.register_new_store("ToyStore", "Toy World", "VAR"))
print()

# Sell products to stores
chair1 = factory_manager.products[0]
chair2 = factory_manager.products[1]
chair3 = factory_manager.products[2]
store1 = factory_manager.stores[0]
store2 = factory_manager.stores[1]
print(factory_manager.sell_products_to_store(store2, chair1, chair2))
print(factory_manager.sell_products_to_store(store1, chair1, chair2, chair3))
print()

# Unregister store
print(factory_manager.unregister_store("Furniture Outlet"))
print()

# Discount products
print(factory_manager.discount_products("Classic"))
print(factory_manager.discount_products("Rocking Horse"))
print()

# Request store statistics
print(factory_manager.request_store_stats("Furniture Outlet"))
print(factory_manager.request_store_stats("Toy World"))
print()

# Factory statistics
print(factory_manager.statistics())
print()

# Unregister store
print(factory_manager.unregister_store("Toy World"))

