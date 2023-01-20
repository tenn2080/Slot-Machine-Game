def deposit_money():
    while True:
        # this is string
        amount = input("How much would you like to deposit? $") 
        # check if the input is digit(whole number)
        if amount.isdigit(): 
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter an amount greater than 0.")
        else:
            print("Enter a positive whole number.")
    # amount is returned after breaking out of while loop
    return amount

# calling the function
deposit_money() 