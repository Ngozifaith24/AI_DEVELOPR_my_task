# Task1:  Create and Display**

# - Ask the user to enter three favorite Nigerian dishes (one at a time).

#  - Store them in a tuple called dishes.

# - Print the tuple in a single line, separating items with commas.

# - Use the \n escape sequence to print each dish on a new line.

print("Ask the user for their favorite dish")
print("Store them in a tuple called dishes")
print("Print the tuple in a single line, separating items with commas")
print("Use the \n escape sequence to print each dish on a new line")
dishes = input("Enter Your Favourite dish: ").split()
dishes_tuple = tuple(dishes)
print(dishes_tuple)
for dish in dishes:
    print(dish)

    