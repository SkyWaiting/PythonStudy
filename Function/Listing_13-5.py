__author__ = 'guorui'
# Trying to print a local variable

# Function to calculate tax and return the total
def calculateTax(price, tax_rate):
    total = price + (price * tax_rate)
    return total;

my_price = float(raw_input("Enter a price: "))

# Call the function and store and print the result
totalPrice = calculateTax(my_price, 0.06)
print "price = ", my_price, " Total price = ", totalPrice

# this line will cause an error
# print price