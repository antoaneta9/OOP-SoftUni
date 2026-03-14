from project.product import Product

# BEVS IMPORTS
from project.beverage.beverage import Beverage
from project.beverage.hot_beverage import HotBeverage
from project.beverage.cold_beverage import ColdBeverage
from project.beverage.coffee import Coffee
from project.beverage.tea import Tea

# FOODS IMPORTS
from project.food.food import Food
from project.food.main_dish import MainDish
from project.food.dessert import Dessert
from project.food.starter import Starter
from project.food.salmon import Salmon
from project.food.cake import Cake
from project.food.soup import Soup




product = Product("coffee", 2.5)
print(product.__class__.__name__)
print(product.name)
print(product.price)

beverage = Beverage("coffee", 2.5, 50)
print(beverage.__class__.__name__)
print(beverage.__class__.__bases__[0].__name__)
print(beverage.name)
print(beverage.price)
print(beverage.milliliters)

soup = Soup("fish soup", 9.90, 230)
print(soup.__class__.__name__)
print(soup.__class__.__bases__[0].__name__)
print(soup.name)
print(soup.price)
print(soup.grams)