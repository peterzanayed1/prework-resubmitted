# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

from operator import index
from tkinter import CURRENT


def hello_name(username):
    print("hello " + username + "!")

(hello_name('peter'))


# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing


def first_odds():
    for i in range (1,101,2):
            print(i)


first_odds()

# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

b_list = [1,2,3,4,88,6,7,8345345345,9]
def max_num_in_list(a_list):
    a_list.sort()
    print("the largest value in this list is", + a_list[-1])

max_num_in_list(b_list)

# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 400 == 0: 
        print(True)
    elif a_year % 4 == 0 and a_year % 100 != 0:
        print(True)
    else:
        print(False)

is_leap_year(2008)

# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

a_list = [1,2,3,4,5,6,7,8,9]
b_list = [1,4,6,7,9,0,44,5,7,33]

def is_consecutive(a_list):
    for i in range(1,len(a_list)):
        if a_list[i] - a_list[i-1] == 1:
            #print('true')
            pass 
        else:
            return False
    return True

print(is_consecutive(a_list))


