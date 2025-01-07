# Slot Machine Project
MAX_LINES = 3 # conventional to keep in capitals

def deposit():
    while True:
        amount = input("What would you like to depost? $")
        if amount.isdigit(): # Check for valid number 
            amount = int(amount) # String converted to integer
        
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input("lines a number of lines you want to bet on (1 -:" + str(MAX_LINES) + ")? ") 
        if lines.isdigit(): # Check for valid number 
            lines = int(lines) # String converted to integer


            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("ERROR: Choose a number between 1 and 3.")
        else:
            print("Please enter a number.")
    
    return lines

def main():
    balance = deposit()
    lines = get_number_of_lines()

main()

