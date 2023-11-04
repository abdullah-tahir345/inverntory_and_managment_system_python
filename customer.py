class Customer:
    def __init__(self):
        self.customers = []
    
    def create_customers(self, name, email):
        customer_id = len(self.customers) + 1
        customer = {customer_id:{'name':name,'email':email}}
        self.customers.append(customer)
        return customer
    
    def update_customer_info(self, customer_id, name, email):
        for customer in self.customers:
            for key in customer:
                if key == customer_id:
                    customer[key]['name'] = name
                    customer[key]['email'] = email
    
    def view_purchase_history(self):
        pass
    
store_customers = Customer()
store_customers.create_customers('Abdullah', 'abdullah.tahir341@gmail.com')
store_customers.create_customers('Hamza', 'hamza.tahir@gmail.com')
store_customers.create_customers('Usman', 'usman.tahir@gmail.com')
store_customers.update_customer_info(1, 'Abdullah', 'abdullah.tahir3451@gmail.com')
