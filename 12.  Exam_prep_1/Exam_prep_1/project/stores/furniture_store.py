from project.stores.base_store import BaseStore

class FurnitureStore(BaseStore):
    CAPACITY = 50

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.CAPACITY)

    @property
    def store_type(self):
        return "FurnitureStore"

    def store_stats(self):
        result = [
            f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
            self.get_estimated_profit(),
            "**Furniture for sale:"
        ]
        models = {}
        for product in self.products:
            if product.model not in models:
                models[product.model] = {"count": 0, "total_price": 0}
            models[product.model]["count"] += 1
            models[product.model]["total_price"] += product.price
        for model in sorted(models):
            count = models[model]["count"]
            avg_price = models[model]["total_price"] / count
            result.append(f"{model}: {count}pcs, average price: {avg_price:.2f}")
        return "\n".join(result)
