super_market_prices = {} 
items = ["bread","burger", "rice", "garri", "milk"]
super_market_prices["bread"] = float(input("Enter the price: "))
super_market_prices["burger"] = float(input("Enter the price: "))
super_market_prices["rice"] = float(input("Enter the price: "))
super_market_prices["garri"] = float(input("Enter the price: "))
super_market_prices["milk"] = float(input("Enter the price: "))
print(f"Bread: {super_market_prices["bread"]}")
print(f"Burger: {super_market_prices["burger"]}")
print(f"Bread: {super_market_prices["rice"]}")
print(f"Bread: {super_market_prices["garri"]}")
print(f"Bread: {super_market_prices["milk"]}")
print("\nAvailable Items: ", list(super_market_prices.keys()))
items_to_update = input("Enter the name of the item you want to update the price for :")
while items_to_update not in super_market_prices:
    print("invalid item.please chose from:", list(super_market_prices.keys()))
    items_to_update = input("Enter the name of the item you want to update the price for :")
new_price = input(f" Enter the new price for {items_to_update}:")
super_market_prices.update({items_to_update:new_price})
print("\nUpdated pricelist:")
for item,price in super_market_prices.items():
    print(f"{item}:{price}")