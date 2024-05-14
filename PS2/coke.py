total_amount_of_coke = 50
print(f"Amount Due: {total_amount_of_coke}")
while total_amount_of_coke >= 0:
    user_amount = int(input("Insert Coin: "))
    due_amount = total_amount_of_coke - user_amount
    if user_amount == total_amount_of_coke :
        total_amount_of_coke -= user_amount
        print(f"Change Owed: {due_amount}")
        break
    elif user_amount > total_amount_of_coke:
        remaining_amount = user_amount - total_amount_of_coke
        print(f"Change Owed: {remaining_amount}")
        break
    elif total_amount_of_coke == 0 :
        print("Change Owed: 0")
    elif user_amount == 30:
        print(f"Amount Due: {total_amount_of_coke}")
    else:
        total_amount_of_coke -= user_amount
        print(f"Amount Due: {total_amount_of_coke}")
