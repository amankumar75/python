print("Enter 1 -> For Conversion Of Rupees To Doller.")
print("Enter 2 -> For Conversion Of Dollar To Rupees.")

choice = int(input("Enter Choice :"))
if choice == 1 :
    rupees = float(input("Enter Indian Rupees :"))
    doller = rupees/89.25
    print(rupees,"indian rupees in doller will be",doller,"USD")
elif choice == 2 :
    doller = float(input("Enter Doller :"))
    rupees = doller*89.25 
    print(doller,"USD in indian rupees will be ₹",rupees,)
else :
    print("Invalid Choice")
    print("Try Again")

