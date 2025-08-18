# #Task 1
# #a. Explaining each output for the program below
# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))

# # print(f"{num1} == {num2} : {num1==num2}")
# #My num1 =20
# #My num2 = 15
# # My Output gave 20 == 15: False
# #Explanation of this program: this shows that when the first and second number are equal or same it should give TRUE, and if they are different it should give FALSE : (This is a Comparision operator)

# print(f"{num1}!={num2}:{num1 != num2}")
# #My num1 =20
# #My num2 = 15
# # My Output gave 20!=15:True
# #This output is based on the NOT Equal to operator that was used, so when num 1 is not same as num 2 the output should give TRUE, if not the output will be FALSE

# print(f"{num1}> {num2}: {num1 > num2}")
# #My num1 =20
#My num2 = 15
# My Output gave 20> 15: True
#This output was as a result of the GREATER THAN operator used, so when num 1 is greater than num 2, the output should be TRUE if Not it will show FALSE: Mine was True

# print(f"{num1} < {num2}: {num1 < num2}")
#My num1 =20
#My num2 = 15
# My Output gave 20 < 15: False
#This output was as a result of the LESS THAN operator used, so when num 1 is less than num 2, the output should be TRUE if Not it will show FALSE: Mine was FALSE because my num 1 was greater  than num 2 not less than.

#b. Use Cases Where Comparison operator is used
#1. student result checker
#2. product price list comparison
#3. Staff salary check list comparision

#c. writing the code for  comparing two products in a shop
prod_1_Price = float(input("Enter your price:"))
prod_2_price = float(input("Enter your price: "))

print(f"{prod_1_Price}>{prod_2_price} : {prod_1_Price > prod_2_price}")
#This shows that price of product one is higher than product two even in the same shop