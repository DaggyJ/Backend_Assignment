
import sys
print("WELCOME TO JDO BANK KENYA\n")
#Variables
chances = 3
Bal = 1000.65
minBal = 0
pin = 9185

def userSelect(case, Bal):
#Confirming balance  
    if case == 1:
        print(f"Your A/C Balance is: KSH.  {Bal}\n")
#Initializing deposit
    elif case == 2:
        depositAmount = float(input("Enter amount to deposit: KSH. "))
        Bal += depositAmount
        print(f"You have successfully deposited: KSH. {depositAmount}\n")
        print(f"Your new A/C Balance: KSH. {Bal}\n")
#Initializing withdrawal
    elif case == 3:
        withdrawalAmount = float(input("Enter your Amount: KSH. "))
        if withdrawalAmount <= Bal and withdrawalAmount != minBal:
            Bal -= withdrawalAmount
            print(f"You have successfully withdrawn: KSH. {withdrawalAmount}")
            print(f"Your new A/C Balance: KSH. {Bal}\n")
#Transaction rejected            
        else:
            print(f"Your withdrawal of KSH. {withdrawalAmount} was diclined due to Insufficient funds in your A/C")
            print(f"Your A/C Balance is: KSH.  {Bal}\n")

#Exit transaction    
    elif case == 4:
        print("THANK YOU FOR YOUR SERVICES")

        sys.exit()  
    else:
        print("Invalid option selected\n")
    return Bal
#Pin Initialization
while chances > 0:
    userPin = int(input("EnTER PIN: "))
    if userPin == pin:
        print("Correct Pin.\n")
#Transaction Menu       
        while True:
            print("---CHOOSE YOUR SERVICE.---")
            print("1 : Check balance")
            print("2 : Deposit money")
            print("3 : Withdraw money")
            print("4 : Exit")
            userChoice = int(input("ENTER YOUR CHOICE: "))
            Bal = userSelect(userChoice, Bal)
#Exit If all tries are met are are wrong
    else:
        print("Incorrect PIN. Please Try again\n")
        chances -= 1
        print(f"You have {chances} tries remaining")
        if chances == 0:
            print("No more tries left. Exiting.")
            sys.exit()
