store = {"noodles": 32, "salt": 13, "water":50, "chinchin": 40}
items_to_buy = input("Enter the item you want to buy:")
quantity_to_buy = int(input("Enter the quantity you want: "))
store[items_to_buy] -= quantity_to_buy
print("After Purchase:", store )