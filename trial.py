# def divide(x, y):
#     try:
#         # Floor Division : Gives only Fractional Part as Answer
#         result = x // y
#         print("Correct ! Your answer is :", result)
#     except ZeroDivisionError:
#         print("Sorry ! You are dividing by zero ")
 
# # Look at parameters and note the working of Program
# divide(3, 2)
  
  
from ossaudiodev import SOUND_MIXER_DIGITAL1


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
    tot=1
    for i in list:
        i%=tot 
        print(i)
divide_num([12,8])

def remove (a):
    a=[2,4,6,8]
    a.pop(2)
    return a
remove([2,4,6,8])

def smallest(a):
   a.sort()
   print(a[0])
   return smallest
smallest([3,6,8,2,4,5,7])


def divisible_by_seven():
    x=range(100,200)
    for i in range(100,200):
        if i%7==0:
            print(i)
divisible_by_seven()

  
      

