print("Catalog for Lovely Loveseats for Neat Suites")
print("********")

lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
print(lovely_loveseat_description)

lovely_loveseat_price = 254.00
print("Price: $",  "%.2f" % lovely_loveseat_price)
print("********")

stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high
x 54.75 inches wide x 28 inches deep. Black.
"""
print(stylish_settee_description)

stylish_settee_price = 180.50
print("Price: $",  "%.2f" % stylish_settee_price)
print("********")

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with
cream shade.
"""
print (luxurious_lamp_description)

luxurious_lamp_price = 52.15
print("Price: $",  "%.2f" % luxurious_lamp_price)
print("********")
print("\n" * 3) 

sales_tax = .088

customer_one_total = 0

customer_one_itemization = ''
print("Customer One Receipt")
print("------------------")

customer_one_total += lovely_loveseat_price


customer_one_itemization += lovely_loveseat_description


customer_one_total += luxurious_lamp_price


customer_one_itemization += luxurious_lamp_description
print("Customer One Items:")
print(customer_one_itemization)

print("Subtotal: $", "%.2f" % customer_one_total)
customer_one_tax = customer_one_total * sales_tax
print("Sales Tax: $", "%.2f" % customer_one_tax)
customer_one_total += customer_one_tax


print("Total: $", "%.2f" % customer_one_total)
