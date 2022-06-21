#1.Write a python function that takes one argument as a list a=[2,4,6,8]and remove the second last item from that list and returns the whole list without the removeed item
from os import remove


a = [2,4,6,8]
def remove_item(list):
    list.remove(list[-2])
    return list
listb=[2,4,6,8]
print(remove_item(list=listb))
       
# 2.Write a python program that has a list days=["Monday","Tuesday","Friday","Monday"]and counts the number occurrences of MONDAY
# week_days=["Monday","Tuesday","Friday","Monday"]
def week_days(list):
    list=['Monday','Tuesday','Friday','Monday']
    day=list.count('Monday')
    print(day)



# 3.Write a program functio named smallest that accepts a list of unsorted intergers and returns the smallet nummber in the list.Example:
#     a.smallest([3,6,8,2,4,1,5,7])return 1
a=[3,6,8,2,4,1,5,7]
def smallest(list):
    print(min(list))
list=[3,6,8,2,4,1,5,7]
smallest(list)

# 4.Write a function name divsible_by_seven that;using the range function and a for loop returns alist containing all the number between 100 and 200 that are divisible by 7

def divisible_by_seven():
    y=[]
    for i in range [100,200]:
        if i % 7==0:
         y.append(i) 
        print (y)

# 5.Write a python program that takes two input (as integers) from a user and adds
# the 2 numbers,check if the sum is greater than 10 ,less than 10 or equals 10 and prints a statement after eah check)
def number(a,b):
    sum = a+b
    if sum > 10:
        print("sum is greater than 10")
    elif sum <10:
        print("sum is less than 10")
    
    else:
        print ("sum is equal to  10")
number(4,6)
        
    
# 6.Write a function that takes one argument which is a list,a=[1,2,3,4,5]and returns True if 4 is present in the list and False is 4 is not in the list
def num(list):
    y=[3,5,6,7,8,9,12,]
    if 4 in a:
        return True
    else:
        False
# 7.Write a function that takes one argument which is alist fruits=["apples","grapes""pineaple"]and removes the last fruit from the list then returns the list without thee removed fruit
fruits=["apples","grapes""pineaple"]
def crops():
  fruits.pop()
print(fruits)
#  8.Write a python program tha take s in a list of cars,cars=['Ford','BMW','Volvo']and return a sorted list
cars=['Ford','BMW','Volvo']
cars.sort()
print(cars)
