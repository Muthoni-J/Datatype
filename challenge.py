# from audioop import reverse
# from unicodedata import name


# var = "James Bond"
# print(var[2::-1])

# # sampleset = {"Joddi", "Eric", ""}
# var = "James" * 2 * 3
# print(var)
  
  
# for i in range(10,15,1):
#     print(i, end = ',')

# def calculate(num1, num2=4):
#     res = num1 * num2
#     print (res)
    
# calculate(5,6)
# for i in range (1,5):
#     print(i)
# else:
#     print("this is wrong" )

# salary = 8000

# def printSalary():
#     salary =12000
#     print("Salary", salary)

# print(Salary)

# print("Salary:", salary)


# x =36/4*(3+3)*4+2
# print(x)

# var1 = 1
# var2 = 2
# var3 = "3"
# print(var1 + var2 + var3)


# listOne = [20,40,60,80]
# listTwo = [20,40,60,80]
# print(listOne == listTwo)
# print(listOne is listTwo)
 
 
# for x in range(0.5, 5.5, 0.5):
#     print(x)

# any_string = "Oure"

# rev_string = any_string[::-1]

# print(rev_string)


 
# n=int(input("Enter number:"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")
    
    
# st = input("Please enter your own text : ")

# if(st == st[:: - 1]):
#    print("This is a Palindrome String")
# else:
#    print("This is Not")
   
   

# Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”   
    
# def checkSpeed(speed):
#     speedlimit = 70
#     demerit = (speed-speedlimit*1)//5
#     if speed <70:
#         print("OK") 
#     elif demerit>12 and speed>70:
#         print("License suspended")    
#     elif speed>70:
#             print(f"Your demerit points are {demerit}")

#     else:
#          print("None")
# checkSpeed(150)         
        
list = [1, 3, 5, 7, 9]
   
# Getting length of list
length = len(list)
i = 0
   
# Iterating using while loop
while i < length:
    print(list[i])
    i += 1