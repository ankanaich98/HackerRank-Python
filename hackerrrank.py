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

# Merge the Tools
from collections import OrderedDict
def merge_the_tools(string, k):
    i = 0
    while i < len(string):
        word1 = "".join(OrderedDict.fromkeys(string[i: i+k]))      
        print(word1)
        i = i + k

# Introduction to sets
def average(array):
    unique_numbers = set(array)
    return (sum(unique_numbers)/len(unique_numbers))

# Time delta
from datetime import datetime
def time_delta(t1,t2):
    format = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, format)
    t2 = datetime.strptime(t2, format)
    return str(int(abs((t1-t2).total_seconds()))) 

# Classes: Dealing with Complex Numbers
import math
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex((self.real+no.real), self.imaginary+no.imaginary)
    def __sub__(self, no):
        return Complex((self.real-no.real), (self.imaginary-no.imaginary))
    def __mul__(self, no):
        r = (self.real*no.real)-(self.imaginary*no.imaginary)
        i = (self.real*no.imaginary+no.real*self.imaginary)
        return Complex(r, i)
    def __truediv__(self, no):
        conjugate = Complex(no.real, (-no.imaginary))
        num = self*conjugate
        denom = no*conjugate
        try:
            return Complex((num.real/denom.real), (num.imaginary/denom.real))
        except Exception as e:
            print(e)

    def mod(self):
        m = math.sqrt(self.real**2+self.imaginary**2)
        return Complex(m, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

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
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')



