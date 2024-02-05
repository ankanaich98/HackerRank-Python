import math
import os
import random
import re
import sys
import textwrap

# Write a Function
# def is_leap(year):
#     leap = False
    
#     if (year % 400 == 0):
#         leap = True
#     elif(year % 100 !=0 and year % 4 ==0):
#         leap = True
#     return leap

# sWAP cASE
# def swap_case(s):
#     string = ""

#     for i in s:
#         if i.isupper() == True:
#             string+=(i.lower())
#         else:

#             string+=(i.upper())

#     return string

# String Split and Join
# def split_and_join(line):
#     line = line.split(' ')
#     line = '-'.join(line)
#     return line

# What's your Name
# def print_full_name(first, last):
#     print("Hello " + first + " " + last + "! You just delved into python.")

# Mutations
# def mutate_string(string, position, character):
#     string =  list(string)
#     string [position] = character
#     string = ''.join(string)
#     return string

# Find a String
# def count_substring(string, sub_string):
#     total = 0

#     for i in range (len(string)):
#         if string[i:len(string)].startswith(sub_string):
#             total +=1
#     return total

# Text Wrap
# def wrap(string, max_width):
#     return textwrap.fill(string, max_width)

# String Formatting
# def print_formatted(number):
#     width = len(bin(number)[2:])
#     for i in range (1, number+1):
#         deci = str(i)
#         octa = oct(i)[2:]
#         hexa = hex(i)[2:].upper()
#         bina = bin(i)[2:]
#         print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))

    # your code goes here

# Capitalize!
# def solve(s):
#     s = s.split(' ')
#     answer = (i.capitalize() for i in s)
#     return ' '.join(answer)

# Minion Game
# def minion_game(string):
#     n = len(string)
#     comb = ((n)*(n+1))/2
#     count_kevin = 0
#     count_stuart = 0
#     count_kevin = sum([len(string[i:]) for i in range(len(string)) if string[i] in "AEIOU"])
#     count_stuart = comb - count_kevin
    
#     if count_stuart == count_kevin:
#         print("Draw")
#     elif count_stuart > count_kevin:
#         print("Stuart", int(count_stuart) )
#     else:
#         print("Kevin", int(count_kevin))

# Merge the Tools
# from collections import OrderedDict
# def merge_the_tools(string, k):
#     i = 0
#     while i < len(string):
#         word1 = "".join(OrderedDict.fromkeys(string[i: i+k]))      
#         print(word1)
#         i = i + k

# Introduction to sets
# def average(array):
#     unique_numbers = set(array)
#     return (sum(unique_numbers)/len(unique_numbers))

# Time delta
# from datetime import datetime
# def time_delta(t1,t2):
#     format = '%a %d %b %Y %H:%M:%S %z'
#     t1 = datetime.strptime(t1, format)
#     t2 = datetime.strptime(t2, format)
#     return str(int(abs((t1-t2).total_seconds()))) 

# Classes: Dealing with Complex Numbers
# import math
# class Complex(object):
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary
        
#     def __add__(self, no):
#         return Complex((self.real+no.real), self.imaginary+no.imaginary)
#     def __sub__(self, no):
#         return Complex((self.real-no.real), (self.imaginary-no.imaginary))
#     def __mul__(self, no):
#         r = (self.real*no.real)-(self.imaginary*no.imaginary)
#         i = (self.real*no.imaginary+no.real*self.imaginary)
#         return Complex(r, i)
#     def __truediv__(self, no):
#         conjugate = Complex(no.real, (-no.imaginary))
#         num = self*conjugate
#         denom = no*conjugate
#         try:
#             return Complex((num.real/denom.real), (num.imaginary/denom.real))
#         except Exception as e:
#             print(e)

#     def mod(self):
#         m = math.sqrt(self.real**2+self.imaginary**2)
#         return Complex(m, 0)

#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.real)
#         elif self.real == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.real, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#         return result

# Class 2 - Find the torsional Angle
# import math

# class Points(object):
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __sub__(self, no):
#         return  Points((self.x-no.x), (self.y-no.y), (self.z-no.z))
    
#     def dot(self, no):
#         return (self.x*no.x)+(self.y*no.y)+(self.z*no.z)
    
#     def cross(self, no):
#         return Points((self.y*no.z-self.z*no.y), (self.z*no.x-self.x*no.z), (self.x*no.y-self.y*no.x))
    
#     def absolute(self):
#         return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

# Map and lambda functions
# cube = lambda x: x**3

# def fibonacci(n):
#     List = [0, 1]
#     for i in range(2, n):
#         List.append(List[i-1] + List[i-2])
        
#     return(List[0:n])

# Re.split()
# regex_pattern = r"[.,]+"	

# Validating email addresses with filter
# import re
# def fun(s):
#     a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s)
#     return(a)

# def filter_mail(emails):
#     return list(filter(fun, emails))

# Reduce Function
# from fractions import Fraction
# from functools import reduce
# import operator
# def product(fracs):
#     t = reduce(operator.mul,fracs)
#     return t.numerator, t.denominator

#  Validating Roman Numerals
# import re
# digits = '(V?[I]{0,3}|I[VX])'
# tens = '(L?[X]{0,3}|X[LC])'
# hundreds = '(D?[C]{0,3}|C[DM])'
# thousands = 'M{0,3}'
# regex_pattern = thousands + hundreds + tens + digits +'$'

# Arrays
# import numpy 
# def arrays(arr):
#     return numpy.flipud(numpy.array(arr, float))

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
    # s = input()
    # minion_game(s)

    # Merge the Tools
    # string, k = input(), int(input())
    # merge_the_tools(string, k)

    # itertools.product()
    # from itertools import product
    # A = list(map(int,input().split()))
    # B = list(map(int,input().split()))
    # print(*list(product(A,B))) # * is the unpacking operator

    # collections.counter()
    # from collections import Counter
    # number_of_shoes = int(input())
    # stock = Counter(map(int,input().split()))
    # number_of_customers = int(input())
    # total = 0
    # for i in range (number_of_customers):
    #     size, rate = map(int, input().split())
    #     if stock[size]:
    #         stock[size]-=1
    #         total += rate
    # print(total)

    # itertools.permutations()
    # from itertools import permutations
    # string,p = input().split()
    # for i in sorted(permutations(string,int(p))):
    #     print(''.join(i))

    # Polar coordinates
    # import cmath
    # string_number = input()
    # string_number_to_complex= complex(string_number)
    # print(abs(string_number_to_complex))         # r = distance from the complex number to the origin
    # print(cmath.phase(string_number_to_complex)) # p = phase or the Counter clockwise angle measured from the positive x-axis to the line segment that joins the complex number to the origin.

    # Introduction to Sets
    # n = int(input())
    # arr = list(map(int, input().split()))
    # result = average(arr)
    # print(result)

    # DefaultDict Tutorial
    # from collections import defaultdict
    # input_n, input_m = map(int, input().split())
    # d = defaultdict(list)
    # for i in range(input_n):
    #     A = input()
    #     d[A].append(i+1)
    # for j in range(input_m):
    #     B = input()
    #     if B in d:
    #         print(*d[B])
    #     else:
    #         print(-1)

    # Calendar Module
    # import calendar
    # month,day,year = list(map(int,input().split()))
    # answer = calendar.weekday(year,month,day)
    # print(calendar.day_name[answer].upper())

    # Exceptions
    # for i in range (int(input())):
    #     try:
    #         A, B = map(int,input().split())
    #         print(A//B)
    #     except Exception as e:
    #         print ("Error Code:",e)

    # Collections.namedtuple()
    # from collections import namedtuple
    # total_rows = int(input())
    # column_names = input().split()
    # total_marks = 0
    # for _ in range(total_rows):
    #     students = namedtuple('student',column_names)
    #     MARKS, CLASS, NAME, ID = input().split()
    #     student = students(MARKS, CLASS, NAME, ID)
    #     total_marks += int(student.MARKS)
    # print(total_marks/total_rows)

    # Time Delta
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # t = int(input())
    # for t_itr in range(t):
    #     t1 = input()
    #     t2 = input()
    #     delta = time_delta(t1, t2)
    #     fptr.write(delta + '\n')
    # fptr.close()

    # Find Angle MBC
    # from math import degrees, atan2
    # AB = float(input())
    # BC = float(input())
    # MBC = round(degrees(atan2(AB, BC)))
    # print((str(MBC)), chr(176), sep='')

    # No Idea!
    # n, m = map(int, input().split())
    # elements_array = list(map(int, input().split()))
    # happiness = 0
    # A = set(map(int,input().split()))
    # B = set(map(int,input().split()))
    # for i in elements_array:
    #     if i in A:
    #         happiness +=1
    #     elif i in B:
    #         happiness -=1
    # print(happiness)

    #Collections.OrderedDict()
    # from collections import OrderedDict
    # times = int(input())
    # dictionary = OrderedDict()
    # for i in range (times):
    #     item, space, price = input().rpartition(' ') #This is useful for cases where you want to extract information from a string where the information is separated by a specific character (in this case, a space).
    #     dictionary[item] = dictionary.get(item, 0) + int(price) 
    # for item, price in dictionary.items():
    #     print(item, price)

    # Symmetric Difference
    # M = int(input())
    # set_A = set(map(int,input().split()))
    # N = int(input())
    # set_B = set(map(int,input().split()))
    # A = (set_A.difference(set_B))
    # B = (set_B.difference(set_A))
    # answer = A.union(B)
    # for i in sorted(answer):
    #     print(i)

    # itertools.combinations()
    # from itertools import combinations
    # word,c = input().split()
    # c = int(c)
    # for i in range (1,c+1):
    #     for j in combinations(sorted(word), i):
    #         print (''.join(j))

    # Incorrect Regex
    # import re
    # times = int(input())
    # for i in range(times):
    #     try:
    #         pattern = input()
    #         answer = (re.compile(pattern))
    #         print(bool(answer))
    #     except re.error:
    #         print('False')

    # Set.add()
    # total_stamps = int(input())
    # stamps = set()
    # for i in range(total_stamps):
    #     stamps.add(input())
    # print(len(stamps))

    # itertools.combinations_with_replacement()
    # from itertools import combinations_with_replacement
    # word , c = input().split()
    # c = int(c)
    # list = (combinations_with_replacement(sorted(word),c))
    # for l in list:
    #     print(''.join(l))

    # Word Order
    # from collections import Counter
    # times = int(input())
    # list = [input().strip() for i in range(times)]
    # answer = Counter(list)
    # print(len(answer))
    # print(*answer.values())

    # set.discard, remove, pop
    # total_numbers = int(input())
    # numbers = list(map(int,input().split()))
    # numbers.reverse()                        # pypy3 pop is different from python3, as pypy3 will pop the last element and python3 the first
    # numbers = set(numbers)
    # command_number = int(input())
    # for i in range (command_number):
    #     command = list(map(str,input().split()))
    #     if command[0] == "pop":
    #         numbers.pop()
    #     elif command[0] == "remove":
    #         try:
    #             numbers.remove(int(command[1]))
    #         except:
    #             continue
    #     elif command[0] == "discard":
    #         try:
    #             numbers.discard(int(command[1]))
    #         except:
    #             continue 
    # print(sum(numbers))

    # Collections.deque()
    # from collections import deque
    # times = int(input())
    # deque = deque()
    # for i in range(times):
    #     command = list(map(str,input().split()))
    #     if command[0] == 'append':
    #         deque.append(int(command[1]))
    #     elif command[0] == 'appendleft':
    #         deque.appendleft(int(command[1]))
    #     deque.reverse 
    #     if command[0] == 'pop':
    #         deque.pop()
    #     elif command [0] == 'popleft':
    #         deque.popleft()
    # print(' '.join(map(str,deque)))

    # Compress the string
    # from itertools import groupby
    # for k, c in groupby(input()):
    #     print("(%d, %d)" % (len(list(c)), int(k)), end=' ')

    # Company Logo - new concept
    # from collections import Counter, OrderedDict
    # class OrderedCounter(Counter, OrderedDict):
    #     pass
    # word = input()
    # [print(*c) for c in OrderedCounter(sorted(word)).most_common(3)]

    # Set.union() operation
    # english_subscriptions = int(input())
    # english_roles = set(map(int,input().split()))
    # french_subscriptions = int(input())
    # french_roles = set(map(int,input().split()))
    # answer_set = set(english_roles.union(french_roles))
    # print(len(answer_set))

    # Pilling Up!
    # ANS = []
    # times = int(input())
    # for _ in range(times):
    #     n = int(input())
    #     sl = list(map(int, input().split()))
    #     for _ in range(n-1):
    #         if sl[0] >= sl[len(sl)-1]:
    #             a = sl[0]
    #             sl.pop(0)
    #         elif sl[0] < sl[len(sl)-1]:
    #             a = sl[len(sl)-1]
    #             sl.pop(len(sl)-1)
    #         else:
    #             pass
    #         if len(sl) == 1:
    #             ANS.append("Yes")
    #         if((sl[0] > a) or (sl[len(sl)-1] > a)):
    #             ANS.append("No")
    #             break
    # print("\n".join(ANS))

    # Triangle Quest 2
    # for x in range(1,int(input())+1):
    #     print(((111111111)%(10**x))**2)

    # Iterables and Iterators
    # from itertools import combinations
    # list_size = int(input())
    # list_numbers = input().split()
    # c = int(input())
    # Combination = list(combinations(list_numbers,c))
    # Filtered = filter(lambda c: 'a' in c,Combination)
    # print((len(list(Filtered))/len(Combination)))

    # Set.intersection() Operation
    # english_subscriptions = int(input())
    # english_rolls = set(map(int,input().split()))
    # french_subscriptions = int(input())
    # french_rolls = set(map(int,input().split()))
    # print(len(english_rolls.intersection(french_rolls)))

    # Mod Divmod
    # a = int(input())
    # b = int(input())
    # print(a//b)
    # print(a%b)
    # print(divmod(a,b))

    # Power - Mod Power
    # a = int(input())
    # b = int(input())
    # m = int(input())
    # print(pow(a,b))
    # print(pow(a,b,m))

    # Maximize it!
    # from itertools import product
    # K,M = map(int,input().split())
    # N = (list(map(int, input().split()))[1:] for _ in range(K))
    # results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
    # print(max(results))

    # Set.difference() operation
    # english_subscriptions = int(input())
    # english_rolls = set(map(int,input().split()))
    # french_subscriptions = int(input())
    # french_rolls = set(map(int,input().split()))
    # print(len(english_rolls.difference(french_rolls)))

    # Integers come in all sizes
    # a = int(input())
    # b = int(input())
    # c = int(input())
    # d = int(input())
    # print(pow(a,b)+pow(c,d))

    # Set.symmetric.difference() operation
    # english_subscriptions = int(input())
    # english_rolls = set(map(int,input().split()))
    # french_subscriptions = int(input())
    # french_rolls = set(map(int,input().split()))
    # print(len(english_rolls.symmetric_difference(french_rolls)))

    # Set Mutations
    # element_number_A = input()
    # numbers = set(map(int,input().split()))
    # command_number = int(input())
    # for i in range (command_number):
    #     command = list(map(str,input().split()))
    #     if command[0] == "intersection_update":
    #         numbers.intersection_update(set(map(int,input().split())))
    #     elif command[0] == "update":
    #         numbers.update(set(map(int,input().split())))
    #     elif command[0] == "symmetric_difference_update":
    #        numbers.symmetric_difference_update(set(map(int,input().split())))
    #     elif command[0] == "difference_update":
    #        numbers.difference_update(set(map(int,input().split())))      
    # print(sum(numbers))

    # Triangle Quest
    # for i in range(1,int(input())): 
    #     print(int((i*(pow(10, i) - 1)) / 9 ))

    # Captains Room
    # k = int(input())
    # room_numbers = list(map(int,input().split()))
    # count_dict = {}
    # for room_num in room_numbers:
    #     count_dict[room_num] = count_dict.get(room_num,0)+1
    # captains_room = next(key for key, value in count_dict.items() if value == 1)
    # print(captains_room)

    # Check Subset
    # cases = int(input())
    # answers = list()
    # for i in range (cases):
    #     a_length = int(input())
    #     a = set(map(int,input().split()))
    #     b_length = int(input())
    #     b = set(map(int,input().split()))
    #     answer = a.issubset(b)
    #     answers.append(answer)
    # for answer in answers:
    #     print(''.join(str(answer)))

    # Check strict superset
    # A = set(map(int,input().split()))
    # N = int(input())
    # Answer = 'True'
    # for i in range (N):
    #     check = set(map(int,input().split()))
    #     if (check.issubset(A)) !=  True:
    #         Answer = 'False'
    # print(Answer)

    # Text Alignment
    # thickness = int(input()) #This must be an odd number
    # c = 'H'
    # for i in range(thickness):
    #     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
    # for i in range(thickness+1):  print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    # for i in range((thickness+1)//2):
    #     print((c*thickness*5).center(thickness*6))    
    # for i in range(thickness+1): print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
    # for i in range(thickness):  print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

    # Classes: Dealing with Complex Number -- very important
    # c = map(float, input().split())
    # d = map(float, input().split())
    # x = Complex(*c)
    # y = Complex(*d)
    # print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

    # Class 2 - Find the torsional Angle
    # points = list()
    # for i in range(4):
    #     a = list(map(float, input().split()))
    #     points.append(a)

    # a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    # x = (b - a).cross(c - b)
    # y = (c - b).cross(d - c)
    # angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    # print("%.2f" % math.degrees(angle))

    # Zipped
    # N, X = map(int, input().split()) 
    # scores = []
    # for i in range (int(X)):
    #     scores.append(map(float,input().split()))
    # for i in zip(*scores): 
    #     print( sum(i)/len(i) )

    # Input()
    # x,y = map(int,input().split())
    # func = input()
    # z = eval(func)
    # if (z == y):
    #     print ("True")
    # else:
    #     print ("False")

    # Python evaluation
    # action = input()
    # eval(action)

    # Athlete Sort
    # first_multiple_input = input().rstrip().split()
    # n = int(first_multiple_input[0])
    # m = int(first_multiple_input[1])
    # arr = []
    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))
    # k = int(input().strip())
    # arr.sort(key=lambda x: x[k])
    # for att_list in arr:
    #     print(*att_list)

    # Any or All
    # N,numbers = int(input()),input().split()
    # print(all([int(i)>0 for i in numbers]) and any([j == j[::-1] for j in numbers]))

    # ginortS
    # string = sorted(input())
    # lower = list(filter(lambda x: x.islower(),string))
    # upper = list(filter(lambda x: x.isupper(),string))
    # odd = list(filter(lambda x: x.isdigit() and int(x)%2==1,string))
    # even = list(filter(lambda x: x.isdigit() and int(x)%2==0,string))
    # print(*(lower + upper + odd + even),sep='')

    # Detect Floating Point Number
    # import re
    # for _ in range(int(input())):
    #     print(re.search(r'^([-\+])?\d*\.\d+$', input()) is not None)

    # Map and Lambda function
    # n = int(input())
    # print(list(map(cube, fibonacci(n))))

    # # Re.split()
    # import re
    # print("\n".join(re.split(regex_pattern, input())))

    # Validating email addresses with filter
    # n = int(input())
    # emails = []
    # for _ in range(n):
    #     emails.append(input())
    # filtered_emails = filter_mail(emails)
    # filtered_emails.sort()
    # print(filtered_emails)
    
    # Group(), Groups() & Groupdict()
    # import re
    # S = input()
    # answer = re.search(r'([a-zA-Z0-9])\1',S)
    # print(answer.group(1) if answer else -1)

    # Reduce Function
    # fracs = []
    # for _ in range(int(input())):
    #     fracs.append(Fraction(*map(int, input().split())))
    # result = product(fracs)
    # print(*result)

    # Re.findall() & Re.finditer()
    # import re
    # answer = re.findall(r"(?<=[^aeiou])([aeiou]{2,})(?=[^aeiou])", input(), re.IGNORECASE)
    # if answer:
    #     print(*answer, sep="\n")
    # else:
    #     print(-1)

    # Re.start() & Re.end()
    # import re
    # S = input()
    # k = input()
    # answer = list(re.finditer(r'(?={})'.format(k), S))
    # if answer:
    #     print('\n'.join(str((match.start(),match.start() + len(k) - 1)) for match in answer))
    # else:
    #     print('(-1, -1)')
    
    # Validating Roman Numerals
    # print(str(bool(re.match(regex_pattern, input()))))

    # Validating Phone Numbers
    # import re
    # cases = int(input())
    # answers = list()
    # pattern = re.compile(r'^[789]\d{9}$')
    # for i in range (cases):
    #     number = input()
    #     if pattern.match(number):
    #         answers.append("YES")
    #     else:
    #         answers.append("NO")
    # for answer in answers:
    #     print(answer)
    
    # Validating and Parsing Email Addresses
    # import email.utils
    # import re
    # cases = int(input())
    # for i in range (cases):
    #     string = input()
    #     parsed = email.utils.parseaddr(string)
    #     if parsed[1] and re.match(r'^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$',parsed[1]):
    #         print (email.utils.formataddr((parsed[0],parsed[1])))

    # Hex Color Code
    # import re
    # for i in range(int(input())): 
    #     match = re.findall(r"(\#[a-f0-9]{3,6})[\;\,\)]{1}", input(), re.I) 
    #     if match:
    #         for j in list(match):
    #             print(j)

    # Arrays
    # arr = input().strip().split(' ')
    # result = arrays(arr)
    # print(result)

    # Sum and Prod
    # import numpy
    # N,M = map(int,input().split())
    # my_array = []
    # for i in range (N):
    #     row = list(map(int,input().split()))
    #     my_array.append(row)
    # np_array = numpy.array(my_array)
    # added_array = numpy.sum(my_array, axis = 0)
    # print (numpy.prod(added_array, axis = 0))  

    # Array Mathematics
    # import numpy
    # N,M = map(int,input().split())
    # A, B = (numpy.array([input().split() for _ in range(N)], dtype=int) for _ in range(2))
    # print(A + B, A - B, A * B, A // B, A % B, A ** B, sep='\n')

    # Zeros and Ones
    # import numpy
    # dimensions = input().split()
    # dimensions = [int(i) for i in dimensions]
    # print(numpy.zeros(tuple(dimensions),dtype = numpy.int))
    # print(numpy.ones(tuple(dimensions),dtype = numpy.int))

    # Shape and Reshape
    # import numpy
    # my_array = numpy.array([input().split()],dtype=int)
    # print (numpy.reshape(my_array,(3,3)))

    # Concatenate
    # import numpy
    # N,M,P = map(int,input().split())
    # arr1 = []
    # arr2 = []
    # for i in range (N):
    #     arr1.append(list(map(int,input().split())))
    # for i in range (M):
    #     arr2.append(list(map(int,input().split())))
    # print (numpy.concatenate((arr1, arr2), axis = 1))

    # Eye and Identity
    # import numpy
    # numpy.set_printoptions(sign=' ')
    # N,M = map(int,input().split())
    # print(numpy.eye(N,M))

    # Min and Max
    # import numpy
    # N,M = map(int,input().split())
    # arr = []
    # for i in range (N):
    #     arr.append(list(map(int,input().split())))
    # print(max(numpy.min(arr,axis=1)))

    # Floor, Ceil and Rint
    # import numpy
    # numpy.set_printoptions(sign=' ')
    # array = list(map(float,input().split()))
    # print (numpy.floor(array)) 
    # print (numpy.ceil(array)) 
    # print (numpy.rint(array)) 

    # Transpose and Flatten
    # import numpy
    # N,M = map(int,input().split())
    # arr = []
    # for i in range (N):
    #     arr.append(list(map(int,input().split())))
    # print(numpy.transpose(arr))
    # arr_np = numpy.array(arr)
    # print(arr_np.flatten())

    # Mean Var and Std
    # import numpy
    # N,M = map(int,input().split())
    # arr = []
    # for i in range (N):
    #     arr.append(list(map(int,input().split())))
    # print (numpy.mean(arr, axis = 1))   
    # print (numpy.var(arr, axis = 0)) 
    # print (round(numpy.std(arr, axis = None),11))

    # Dot and Cross
    # import numpy
    # N = int(input())
    # A =[]
    # B =[]
    # for i in range (N):
    #     A.append(list(map(int,input().split())))
    # for i in range (N):
    #     B.append(list(map(int,input().split())))
    # A_np = numpy.array(A)
    # B_np = numpy.array(B)
    # print(numpy.dot(A_np,B_np))

    # Inner and Outer
    # import numpy
    # A =[]
    # B =[]
    # A.append(list(map(int,input().split())))
    # B.append(list(map(int,input().split())))
    # for answer in numpy.inner(A,B):
    #     print(answer[0])
    # print(numpy.outer(A,B))

    # Polynomials
    # import numpy
    # poly= list(map(float,input().split()))
    # val=float(input())
    # print (numpy.polyval(poly,val))

    # Linear Algebra
    import numpy
    N = int(input())
    A =[]
    for i in range (N):
        A.append(list(map(float,input().split())))
    print (round(numpy.linalg.det(A),2))

