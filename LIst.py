
# Use the list function reverse()
# inbuilt function
from multiprocessing.reduction import duplicate


list1=[100,200,300,400,500]
list1.reverse()
print(list1)
 
x=[100,200,300,400,500]  
reverse_list=x[::-1]
print(reverse_list) 
list1=[100,200,300,400,500]
list1[0],list1[-1]=list1[-1],list1[0]
print(list1)

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i+j for i,j in zip(list1, list2)]
# list comprehession
numbers = [1, 2, 3, 4, 5, 6, 7]
number1 = [i**2 for i in numbers]
print(number1)
# print in a new list
numbers = [1, 2, 3, 4, 5, 6, 7]
b=[]
for i in numbers:
   b.append(i**2)
print(b)

# printing numbers
numbers = [1, 2, 3, 4, 5, 6, 7]
for i in numbers:
    i**2
    print(i)
    
    
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers.pop()
print(numbers)
#   pop removes index in a list  
# remove removes an assigned item
numbers = [1, 2, 3, 4, 5, 6, 7]
# numbers.remove(4)
numbers.pop(4)
print(numbers)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = [a+b for a,b in zip(list1,list2)]
print(list3)

#  Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for i in list1:
    if(len(i))==0:
        list1.remove(i)
print(list1)

# numbers = [1, 2, 2, 4, 5, 5, 7]
# numbers1 = set(numbers)
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1=[2][2].append(7000)
# print(list2)
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))

def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2]))

def multiply_list(items):
    numbers=1
    for y in items:
     numbers*= y
    return numbers
print(multiply_list([5,2]))

def largest_list(items):
    nums=0
    for x in items:
        if x >x:
          max=x
        return nums
    print(largest_list([3,8,1,5]))
    
def largest_num(list):
    
    max =list[0]
    for x in list:
      if x>max:
        max=x
      return max
print(largest_num([5,3,6,1]))
    
def divide_num(list):
    div=1
    for y in list:
        div%=y
        return div
    print(divide_num([8,2]))




    