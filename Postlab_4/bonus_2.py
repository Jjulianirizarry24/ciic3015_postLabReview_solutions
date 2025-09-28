def calculate_markup(price, item_category, customer_type):
    if customer_type == "owner":
        return 0.0
    elif customer_type == "customer":
        price *= 1.10  
    # Employee case
    else:
        price *= 0.80  
    
    # If food, no need to calculate tax
    if item_category == "food":
        return price
    
    elif item_category == "supplied":
        price *= 1.20 

    price *= 1.15

    return round(price, 2)


def customer_input():
    price = float(input("Enter the item price: "))
    item_category = input("Enter the item category (inventory/supplied/food): ").lower()
    customer_type = input("Enter the customer type (customer/employee/owner): ").lower()

    final_price = calculate_markup(price, item_category, customer_type)

    print("Final price:", final_price)

