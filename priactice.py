print("(1) create new file")
print("(2) print file")
print("(3) add new item in file")
choice = input("Enter your chlice: ")

if (choice == "1"):
    f = open("sample.txt", "w")    
elif (choice =="2"):
    f = open("sample.txt", "r")
    print(f.read())
    f.close()
elif (choice == "3"):
    item = input("enter your item: ")
    f = open("sample.txt", "a")
    f.write(item + "\n") 
    f.close()