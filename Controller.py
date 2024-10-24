from Customer import Customer
from Product import Product
from Order import Order
from OrderItem import OrderItem
from Payment import Payment
import readFile

class Controller:
    def __init__(self):
        self.customers = []
        self.products = []
        self.orders = []
        self.payments = []

    def loadData(self):
        # Reading customers and products from files
        self.customers = readFile.getCustomerList()
        self.products = readFile.getProductList()

    def createOrder(self, customer_name):
        # Create a new order for a selected customer
        customer = self.findCustomerByName(customer_name)
        if customer:
            new_order = Order(customer)
            self.orders.append(new_order)
            return new_order
        else:
            print("Customer not found.")
            return None

    def addOrderItem(self,order, product, quantity):
        if product:
            order_item = OrderItem(product, quantity)
            order.addOrderItem(order_item)
            print(f"Added {quantity} x {product.productName} to order.")
        else:
            print("Product not found.")

    def submitOrder(self, order):
        # Submit the order and update customer's balance
        totalPrice = order.calcTotal()
        customer = order.customer
        customer.update_balance(-totalPrice)
        print(f"Order submitted. Total: {totalPrice}.")
        return totalPrice

    def makePayment(self, customer_name, amount):
        # Make a payment and update the balance
        customer = self.findCustomerByName(customer_name)
        if customer:
            payment = Payment(customer, amount)
            self.payments.append(payment)
            customer.update_balance(amount)
            print(f"Payment of {amount} made. Updated balance: {customer.customerBalance}")
        else:
            print("Customer not found.")

    def displayCustomerOrders(self, customer_name):
        # Display all orders for a selected customer
        customerOrders = [order for order in self.orders if order.customer.customerName == customer_name]
        return customerOrders

    def displayCustomerPayments(self, customer_name):
        # Display all payments for a selected customer
        customer_payments = [payment for payment in self.payments if payment.customer.customerName == customer_name]
        return customer_payments

    def findCustomerByName(self, customer_name):
        # Helper function to find a customer by Name
        for customer in self.customers:
            if customer.customerName == customer_name:
                return customer
        return None

    def findProductByName(self, product_name):
        # Helper function to find a product by ID
        for product in self.products:
            if product.productName == product_name:
                return product
        return None
