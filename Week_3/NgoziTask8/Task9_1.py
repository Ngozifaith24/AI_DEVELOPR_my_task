# USSD code
#*123#
usdcode_1 = "*123#"
usdcode_2 = "*131#"
usdcode_3 = "*312#"

textcode = input("Enter your  Ussd code: ")

if textcode == "*123#":
    print("1. Account info")
    print("2. Tarrif plan")
    print("3. Data service")
    print("4. Roaming")
    print("5. my services")
    print("6. Borrow airtime")
    print("7. Self services")
    print("8. Chat Zigi")

    textcode_123 = int(input("Enter your number: "))

    if textcode_123 == 1:             # 1. Account info"
        print("My Tools \n")
        print("1. My Number")
        print("2. My tarrif plan")
        print("3. My Account balance")
        print("4. My Data Balance")
        print("5. End of call Message")
        print("6. Sim Registration Status")
        print("7. Purchase History")
        print("0. Back")

        textcode_123_mytools = int(input("Enter your number: "))
        
        if textcode_123_mytools == 1: # 1. My Number
            print("MTN-NG Message\nYello! Your number is 2348137899155")
        elif textcode_123_mytools == 2: # 2. My tarrif plan"
            print("Yello! You are currently on MTN Pulse plan.\n Thank you!")
        elif textcode_123_mytools == 3: # 3. My Account balance"
            print("Yello! Your main account balance : 956.07N")
        elif textcode_123_mytools == 4: # 4. My Data Balance"
            print("MTN-NG Message\nYour balances:\nData Bundle3.52GB\nMore details via SMS")
        elif textcode_123_mytools == 5: # 5. End of call Message"
            print("1.Activate EOCN\n2.Deactivate EOCN")
            textEOCN = int(input("Enter Your number: "))
            if textEOCN == 1 : print("Activate your ECON")
            elif textEOCN == 2 : print("Deactivate your ECON")
            else : print("You are not following our instruction")
        elif textcode_123_mytools == 6: # 6. Sim Registration Status"
            print("MTN-NG Message\nsystem error")
        elif textcode_123_mytools == 7: # 7. Purchase History"
            print("1. Store Locator\n 2. SIM Swap\n3.Get your PUK number\n4. Block Stolen or lost sim\n0. Back")
            text_purchase = int(input("Enter your number"))
            if text_purchase == 1: print("This is your store location case for MTN")
            elif text_purchase ==2: print("This is were you swap your SIM")
            elif text_purchase ==3: print("This is were you get your PUK")
            elif text_purchase ==4: print("This is were you block your SIM")
            elif text_purchase ==0: print("Back")
        elif textcode_123_mytools == 0: # 0. Back"
            print("")
        else :
            print("Failure 3")
   
    elif textcode_123 == 2:           # 2. Tarrif plan
        print()
    elif textcode_123 == 3:           # 3. Data service
        print()
    elif textcode_123 == 4:           # 4. Roaming
        print()
    elif textcode_123 == 5:           # my services
        print()
    elif textcode_123 == 6:           # Borrow airtime
        print()
    elif textcode_123 == 7:           # Self services
        print()
    elif textcode_123 == 8:           # Chat Zigi
        print()
    else: 
        print("Failure 2")                # If user is not following the given instruction
elif textcode == "*131#":
    print("You are *131#")
elif textcode == "*312#":
    print("You are *312#")
else:
    print("Failure 1")                   # If user is not following the given instruction