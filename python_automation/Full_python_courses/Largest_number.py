list1 =  []

num = int(input("Enter the number of list:"))

for i in range(1, num + 1):
    dell = int(input("Enter Next number:"))
    list1.append(dell)
print("Largest selement number is :", max(list1))