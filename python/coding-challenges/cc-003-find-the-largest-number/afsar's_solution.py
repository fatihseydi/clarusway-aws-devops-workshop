print("This program finds the largest of number among the 5 numbers without use max() function")
list1 = []  
for i in range(1, 6):
    list2 = int(input("Enter number please: "))
    list1.append(list2)

list1.sort() 
print(list1[-1])