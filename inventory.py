from product import Product

class Inventory:
    def __init__(self):
        self.products = []
        
    def add_product(self, product_name, price, initial_stock, category, manufacturer):
        if initial_stock >= 0:
            product_id = len(self.products) + 1
            product = Product(product_id, product_name, price, initial_stock, category, manufacturer)
            self.products.append(product)
            print(f'Product {product_name} Added Successfully.')
            return product
        else:
            print('Invalid Quantity.')
            
    def remove_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                return f"Product {product.product_name} removed successfully."
    
    def update_stock_(self, product_id, quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.update_stock(quantity)
                return f"Product quantity {product.product_name} updated successfully."
        
    def check_availability(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                if product.quantity_in_stock > 0:
                    return f"Product {product.product_name} Available with stock {product.quantity_in_stock}."
                else:
                    return "Product Available Soon."
                
    def display_products(self):
        print('Products')
        for product in self.products:
            print(f"Product ID : {product.product_id} -- Product Name : {product.product_name}")
        
    def record_sale(self, sale):
        pass
    
    def generate_report(self):
        pass

store = Inventory()
lux = store.add_product('Lux', 150, 300, 'Grocessory', 'Lux-Soap')
lays = store.add_product('Lays', 60, 500, 'Grocessory', 'Lays-Soap')
surf_excel = store.add_product('Surf Excel', 600, 100, 'Grocessory', 'Surf')
lays_masala = store.add_product('Lays Masala', 60, 500, 'Grocessory', 'Lays-Soap')

print()
print(store.remove_product(4))

surf_bonus = store.add_product('Surf Bonus', 650, 0, 'Grocessory', 'Surf')

# print()
# print(lays.display_details())

# print()
print(store.update_stock_(2, 50))

# print()
# print(lays.display_details())

# print()
# print(store.display_products())

# print()
# print(store.check_availability(3))