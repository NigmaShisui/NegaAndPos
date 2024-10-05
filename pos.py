num1 = int(input("Repeated Times: "))
list1 = []

for x in range(num1):
    user = input("Numbers: ")
    list1.append(user) 

    for i in list1:
        if i > "0":
            print("Positive") 

        elif i < "0":
            print("Negative")
    
        else:
            print("Invalid")