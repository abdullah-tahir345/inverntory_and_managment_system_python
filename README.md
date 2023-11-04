# inverntory_and_managment_system_python

I've created a comprehensive project involving four main modules: product.py, inventory.py, customer.py, and sales.py. These modules interact to simulate an inventory management and sales system. Here is a summary of each module:

<br>1. product.py:
<br>This module defines the Product class, representing individual products in the inventory. Each product has attributes like product ID, name, price, quantity in stock, category, and manufacturer. It provides methods for updating stock and displaying product details.

<br>2. inventory.py:
<br>The Inventory class manages the products available in the inventory. It allows adding products, removing products, updating stock, checking availability, and displaying the list of products. It uses the Product class to manage product-related information.

<br>3. customer.py:
<br>The Customer class manages customer information. Customers can be created with a name and email, and their information can be updated. It maintains a list of customers.

<br>4. sales.py:
<br>The Sales class simulates the sales process. Customers can add products to their cart and then proceed to checkout. The class calculates the total price, generates a receipt, and records the sale. It uses the Customer and Inventory classes to manage customer and product information.
<hr>
Key Features:

<br>--Creating, updating, and displaying product details.
<br>--Managing product inventory and checking availability.
<br>--Managing customer information.
<br>--Simulating the sales process with a shopping cart.
<br>--Generating receipts with the PrettyTable library.
<br>--Recording sales and maintaining a list of customers.
<hr>

Challenges Faced:

<br>--Ensuring data consistency across modules.
<br>--Creating a structured sales process.
<br>--Developing a detailed receipt with PrettyTable.
<hr>

Learning during this project:

<br>--How to work with different class.
<br>--How to store data as an object in List and then use this object for data fetching.
<br>--Use of '<i>self</i>' keyword.
<br>--How to use prettytables for receipt.
<br>--Learn more about attributes/variables, instance/objects, parameters/arguments and methods.
<br>--How to use one class in another class.
<br>--How to import modules in python.
<br>--What is library and module? Here in my project 'prettytable' is the library and product.py or anyother .py file that's imported in another file is a module.
<br>--How to use one class methods in another class.
<hr>

Future Plans:

I can further enhance this project by adding more advanced features like user authentication, different product categories, and a database for persistent data storage. Additionally, I can expand the sales module to manage returns and refunds.
<hr>

