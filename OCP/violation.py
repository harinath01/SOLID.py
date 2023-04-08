# Example 1
class Discount:
    """Demo customer discount class"""

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        """A discount method"""
        if self.customer == 'normal':
            return self.price * 0.2
        elif self.customer == 'vip':
            return self.price * 0.4


#
# This example is failed to pass the Open and Close Principle(OCP). Assume, we have a super VIP customer and we want to
# give a discount of 0.8 percentage. What would we do in this case? Maybe we will solve the problem this way
#

class Discounts:
    """Demo customer discounts class"""

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        """A discount method"""
        if self.customer == 'normal':
            return self.price * 0.2
        elif self.customer == 'vip':
            return self.price * 0.4
        elif self.customer == 'supvip':
            return self.price * 0.8
        

# Example 2
class PaymentProcessor:
    def process_payment(self, payment_method, amount):
        if payment_method == "credit_card":
            # Process credit card payment
            print(f"Processing credit card payment of {amount} dollars...")
        elif payment_method == "paypal":
            # Process PayPal payment
            print(f"Processing PayPal payment of {amount} dollars...")
        elif payment_method == "bitcoin":
            # Process Bitcoin payment
            print(f"Processing Bitcoin payment of {amount} dollars...")
        else:
            # Invalid payment method
            print("Invalid payment method")
