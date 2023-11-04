from customer import store_customers
from inventory import store
from prettytable import PrettyTable 

sales = []

class Sales:
    def __init__(self):
        self.store_customers = store_customers.customers
        self.total_price = 0
        self.buy_product = []
        
    def add_to_cart(self, product_id, quantity):
        for product in store.products:
            if product.product_id == product_id:
                self.buy_product.append([product.product_id,quantity])
                product.quantity_in_stock = product.quantity_in_stock - quantity
                return self.buy_product
    
    def calculate_total_price(self):
        for product in store.products:
            for buy_pro in self.buy_product:
                if product.product_id == buy_pro[0]:
                    self.total_price = self.total_price + (product.price * buy_pro[1])
        return self.total_price
    
    def checkout(self, customer_id):
        for customer in self.store_customers:
            for key in customer:
                if key == customer_id:
                    customer_name = customer[key]['name']
                    customer_email = customer[key]['email']
        sales_id = len(sales) + 1
        print()
        print("Here's your receipt...")
        print()
        print('----------------WELCOME TO ABC Shop----------------\n') 
        print(f"Invoice No. : {sales_id}\nCustomer Name : {customer_name}\nCustomer Email : {customer_email}")
        table = PrettyTable(['Product Name', 'Product Quantity','Price']) 
        for product in store.products:
            for buy_pro in self.buy_product:
                if product.product_id == buy_pro[0]:
                    table.add_row([product.product_name, buy_pro[1],(product.price * buy_pro[1])]) 
        sales_dict = {sales_id:{'customer name':customer_name, 'customer email':customer_email, 'buy products':self.buy_product}}
        sales.append(sales_dict)
                    
        print()
        table.add_row(['TOTAL', '--',self.total_price]) 
        print(table)
        print('\nThanks for shopping with us :)') 
        print('Your total bill amount is ', self.total_price, '/-\n')
        
        return 'Checkout completed.'
        
sale1 = Sales()
print("---------------------------------------------------")
print(store.display_products())
sale1.add_to_cart(1, 6)
sale1.add_to_cart(3, 2)
sale1.calculate_total_price()
print("---------------------------------------------------")
print(sale1.checkout(1))

print('\n\n\n\nOrder2\n\n\n')

sale2 = Sales()
print("---------------------------------------------------")
print(store.display_products())
sale2.add_to_cart(4, 2)
sale2.add_to_cart(2, 10)
sale2.add_to_cart(1, 1)
sale2.calculate_total_price()
print("---------------------------------------------------")
print(sale2.checkout(3))