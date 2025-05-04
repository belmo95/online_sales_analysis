from product import Product
from product_manager import ProductManager

pm = ProductManager()
pm.add_product(Product("Laptop", 80000, 5))
pm.add_product(Product("Mis", 1000, 20))
pm.add_product(Product("Tastatura", 2500, 15))

pm.display_products()
print(f"Ukupna vrednost inventara: {pm.total_value()} RSD")