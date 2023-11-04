class Product:
    def __init__(self, product_id, product_name, price, quantity_in_stock, category, manufacturer):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.category = category
        self.manufacturer = manufacturer
        
    def update_stock(self, quantity):
        if quantity > 0:
            self.quantity_in_stock = self.quantity_in_stock + quantity
        else:
            print('Invalid Quantity')
        return self.quantity_in_stock
    
    def display_details(self):
        return f"Product Details \nProduct ID : {self.product_id}\nProduct Name : {self.product_name}\nPrice : {self.price}\nQuantity In Stock : {self.quantity_in_stock}\nCategory : {self.category}\nManufacturer : {self.manufacturer}"
    
    