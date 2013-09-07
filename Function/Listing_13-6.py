__author__ = 'admin'

# Using a global variable inside a function

# Define function calculateTax
def calculateTax(price, tax_rate):
    total = price + (price * tax_rate)
    print my_price      # try to print my_price
    return total

# Main program calls the function
my_price = float(raw_input("Enter a price: "))

totalPrice = calculateTax(my_price, 0.06)
print "price = ", my_price, " Total price = ", totalPrice
