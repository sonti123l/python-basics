food_Items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


sum = 0.0
is_order_taking = True
while is_order_taking:
    try:
        user_input = input("Item: ").title()
        for i in food_Items:
            if user_input == i:
                price = food_Items[user_input]
                sum = sum + price
                print(f"Total: ${sum:.2f}")
            elif user_input != i:
                is_order_taking = True
    except EOFError:
        break

