a = input("file transfer (yes/no): ")

if a == "yes":
    fileloc = input("Enter source file path: ")
    newfileloc = input("Enter destination file path: ")

    try:
        with open(fileloc, "rb") as file1:
            data = file1.read()

        with open(newfileloc, "wb") as file2:
            file2.write(data)

        print("File transferred successfully!")

    except FileNotFoundError:
        print("File not found! Check the path again.")
    except Exception as e:
        print("Error:", e)
    else:
        print(".................close...................")

else:
    print("Transfer cancelled.")
