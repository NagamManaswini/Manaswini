'''
credit 
debit
mini statement
exit
'''
name = input("Enter your name: ")
password = input("Enter your password: ")
print(f"Welcome {name} to the ATM service!")
balance = 10000  # Initial balance
while True:
    print("\nATM Menu:")
    print("1. Credit")
    print("2. Debit")
    print("3. Mini Statement")
    print("4. Exit")
    
    choice = input("Please select an option (1-4): ")
    
    if choice == '1':
        amount = float(input("Enter amount to credit: "))
        balance += amount
        print(f"Amount credited successfully! New balance: {balance}")
        
    elif choice == '2':
        amount = float(input("Enter amount to debit: "))
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"Amount debited successfully! New balance: {balance}")
            
    elif choice == '3':
        print(f"Your current balance is: {balance}")
        
    elif choice == '4':
        print("Thank you for using the ATM service!")
        break
        
    else:
        print("Invalid choice, please try again.")