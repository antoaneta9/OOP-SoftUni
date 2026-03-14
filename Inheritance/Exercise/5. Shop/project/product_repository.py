from project.product import Product

class ProductRepository:
    def __init__(self):
        self.products: list[Product] = []
    
    def add(self, product: Product):
        self.products.append(product)
    
    def find(self, product_name: str):
        for pr in self.products:
            if pr.name == product_name:
                return pr

    def remove(self, product_name: str):
        product = self.find(product_name)
        if product in self.products:
            self.products.remove(product)
    
    def __repr__(self):
        result = []
        for product in self.products:
            result.append(f"{product.name}: {product.quantity}")
        return "\n".join(result)
