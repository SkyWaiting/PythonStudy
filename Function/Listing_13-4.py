__author__ = 'admin'
# Creating and using a function that returns a value
# Function to calculate tax and return the total

def calculateTax(price, tax_rate):
    total = price + (price * tax_rate)
    return total

my_price = float(raw_input("Enter a price: "))

# Call the function and store the result in totalPrice
totalPrice = calculateTax(my_price, 0.06)

print "price = ", my_price, " Total price = ", totalPrice
