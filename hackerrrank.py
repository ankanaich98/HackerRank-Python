import math
import os
import random
import re
import sys
import textwrap

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

# String Split and Join
def split_and_join(line):
    line = line.split(' ')
    line = '-'.join(line)
    return line

# What's your Name
def print_full_name(first, last):
    print("Hello " + first + " " + last + "! You just delved into python.")

# Mutations
def mutate_string(string, position, character):
    string =  list(string)
    string [position] = character
    string = ''.join(string)
    return string

# Find a String
def count_substring(string, sub_string):
    total = 0

    for i in range (len(string)):
        if string[i:len(string)].startswith(sub_string):
            total +=1
    return total

# Text Wrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

# String Formatting
def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range (1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))

    # your code goes here

# Capitalize!
def solve(s):
    s = s.split(' ')
    answer = (i.capitalize() for i in s)
    return ' '.join(answer)

# Minion Game
def minion_game(string):
    n = len(string)
    comb = ((n)*(n+1))/2
    count_kevin = 0
    count_stuart = 0
    count_kevin = sum([len(string[i:]) for i in range(len(string)) if string[i] in "AEIOU"])
    count_stuart = comb - count_kevin
    
    if count_stuart == count_kevin:
        print("Draw")
    elif count_stuart > count_kevin:
        print("Stuart", int(count_stuart) )
    else:
        print("Kevin", int(count_kevin))

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
    # s = input()
    # result = swap_case(s)
    # print(result)

    # String Split and Join
    # line = input()
    # result = split_and_join(line)
    # print(result)

    # What's your Name
    # first_name = input()
    # last_name = input()
    # print_full_name(first_name, last_name)

    # Mutations
    # s = input()
    # i, c = input().split()
    # s_new = mutate_string(s, int(i), c)
    # print(s_new)

    # Find a String
    # string = input().strip()
    # sub_string = input().strip()
    # count = count_substring(string, sub_string)
    # print(count)

    # String Validators
    # s = input()
    # print (any(i.isalnum() for i in s) )
    # print (any(i.isalpha() for i in s) )
    # print (any(i.isdigit() for i in s) )
    # print (any(i.islower() for i in s) )
    # print (any(i.isupper() for i in s) )

    # Text Alignment

    # Text Wrap
    # string, max_width = input(), int(input())
    # result = wrap(string, max_width)
    # print(result)

    # Designer Door Mat
    # n, m = map(int,input().split())
    # for i in range(n//2):
    #     j = int((2*i)+1)
    #     print(('.|.'*j).center(m, '-'))
    # print('WELCOME'.center(m,'-'))
    # for i in reversed(range(n//2)):
    #     j = int((2*i)+1)
    #     print(('.|.'*j).center(m, '-'))

    # String Formatting 
    # n = int(input())
    # print_formatted(n)

    # Capitalize!
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # s = input()
    # result = solve(s)
    # fptr.write(result + '\n')
    # fptr.close()

    # Minion Game
    s = input()
    minion_game(s)

