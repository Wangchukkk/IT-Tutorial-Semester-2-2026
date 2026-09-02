print("Welcome to the Python Coffee Shop!")
 
customer_name = input("What is your name? ")
print("Hello, " + customer_name + "! Let's order some coffee.")
 
price_coffee = 3.50
price_latte = 4.00
price_mocha = 4.50
 
print("Coffee: $" + str(price_coffee))
print("Latte: $" + str(price_latte))
print("Mocha: $" + str(price_mocha))

total_cost = 0

while True:
    choice = input("What would you like to order? (coffee/latte/mocha or type No): ").lower()

    if choice == 'no':
        break
    
    if choice == "coffee":
        cost = price_coffee
    elif choice == "latte":
        cost = price_latte
    elif choice == "mocha":
        cost = price_mocha
    else:
        print("Sorry, we do not have that.")
        continue

    quantity = int(input("How many cups would you like? "))

    order_cost = cost * quantity
     
    if quantity > 1:
        print("You get a discount of $1.00!")
        order_cost -= 1.00
        
    student = input("Are you a student? (yes/no): ")
    
    if student == "yes":
        order_cost = order_cost * 0.90
        print("You received a 10% student discount!")

    total_cost = total_cost + order_cost
    
    print("Your total is: $" + str(round(order_cost, 2)))
    print("Thank you, " + customer_name + "! Please come again.")
