#Movie Ticket Booking
age = int(input("Enter your age : "))
ticket = True
if age > 18 :
    print("you can watch movie")
    if ticket == True :
        print("you can go inside")
elif age < 15 :
    print("Watcch with your parent")
else :
    print("not Allowed")
