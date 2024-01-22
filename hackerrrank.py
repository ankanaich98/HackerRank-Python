import math
import os
import random
import re
import sys

# Write a Function
def is_leap(year):
    leap = False
    
    if (year % 400 == 0):
        leap = True
    elif(year % 100 !=0 and year % 4 ==0):
        leap = True
    return leap

# sWAP cASE
def swap_case(s):
    string = ""

    for i in s:
        if i.isupper() == True:
            string+=(i.lower())
        else:

            string+=(i.upper())

    return string

if __name__ == '__main__':
    # Say "Hello, World!" with Python
    # print("Hello, World!") 

    # Arithmetic Operations
    # a = int(input())
    # b = int(input())
    # print(a+b)
    # print(a-b)
    # print(a*b)

    # Python Division
    # a = int(input())
    # b = int(input())
    # print(a//b) # integer division
    # print(a/b)  # float division

    # Loops
    # n = int(input())
    # for i in range (n):
    #     print(i*i)

    # Python if else
    # n = int(input().strip()) # strip removes whitespaces
    # if(n%2 !=0):
    #     print("Weird")  
    # elif(n%2==0 and n>=2 and n<=5) :
    #     print("Not Weird")
    # elif(n%2==0 and n>=6 and n<=20) :
    #     print("Weird")
    # elif(n%2==0 and n>20) :
    #     print("Not Weird")

    # Write a Function
    # year = int(input())
    # print(is_leap(year))

    # Python Print
    # n = int(input())
    # for i in range (1 ,n+1):
    #     print(i,end="")

    # List Comprehensions
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())
    # print(list([i,j,k] for i in range(x+1) for j in range (y+1) for k in range (z+1) if i+j+k != n))

    # Find the runner up score
    # n = int(input())
    # arr = list(map(int, input().split()))
    # remove_duplicates = set(arr)
    # sorted_array = sorted(remove_duplicates)
    # print(sorted_array[-2]) # Second last

    # Nested Lists
    # all_list = []
    # for i in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     all_list.append([name, score])
    # second_lowest = sorted(set([score for name, score in all_list]))[1]
    # print('\n'.join(sorted([name for name, score in all_list if score == second_lowest])))

    # Finding the Percentage 
    # n = int(input())
    # student_marks = {}

    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores

    # query_name = input()
    # student = list(student_marks[query_name]) 
    # addition = sum(student)
    # result = addition/len(student)
    # print('%.2f'% result)

    # Lists
    # N = int(input())
    # List = [] 
    # for i in range (N):
    #     command = input().split()

    #     if command[0] == "insert":
    #         List.insert(int(command[1]),int(command[2]))
        
    #     elif command[0] == "append":
    #         List.append(int(command[1]))
        
    #     elif command[0] == "pop":

    #         List.pop();

    #     elif command[0] == "print":

    #         print(List)

    #     elif command[0] == "remove":

    #         List.remove(int(command[1]))

    #     elif command[0] == "sort":

    #         List.sort();

    #     else:

    #         List.reverse();

    # Tuples
    # n = int(input())
    # integer_list = map(int, input().split())
    # t = tuple(integer_list)
    # print(hash(t))

    #sWAP cASE
    s = input()
    result = swap_case(s)
    print(result)

