balance = 20000
pin_no = 6969
user_pin = int(input("Enter A 4 Digit Pin :"))


if user_pin == pin_no :
    amount = int(input("Enter amount :"))
    if amount <= balance :
        print("Tranjection Successful")
        print("Your Remaining Balance is :",balance-amount)
        print("Please Remove Your ATM Card :) ")

    else :
        print("Insufficient Balance !")
        print("Tranjection Unsuccessful")
else :
    print("wrong pin entered")
    print("Try Again")
