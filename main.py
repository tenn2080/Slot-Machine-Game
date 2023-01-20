MAX_LINES = 3

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

def get_num_lines():
    while True:
        lines = input(f"How many lines do you want play? enter between 1 - {MAX_LINES} ") 
        if lines.isdigit(): 
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter an amount between 1-3")
        else:
            print("Enter a positive whole number. between 1-3")
    
    return lines

# calling the function
def main():
    balance = deposit_money()
    lines = get_num_lines()
    print(balance, lines)

main()