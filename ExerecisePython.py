# Exercise 1 (Character Input )
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''
name = input('Please enter your full name:')
age = int(input('Please enter your age:'))
year = 2024 - age + 100

print(f'Your name is  {name} ,and you are {age} years old.')
print(f'you will be 100 years old in the year ' + str(year))
'''

# Exercise 2 (Odd Or Even )
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
'''
num = int(input('Please enter a number:'))
if num %2 == 0:
    print('your number is even.')
else:
    print('your number is odd.')
'''

# Exercise 3 (List Less Than Ten )
# write a program that prints out all the elements of the list that are less than 5.
'''
list = [45, 68, 2, 8, 78, 3, 99,5]
LessNum = []
for i in list:
    if i < 5:
        LessNum.append(i)
print(LessNum)
'''

# Exercise 4 (Divisors)
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
"""lista=[]
numberr=int(input('enter a number: '))

for i in range(2,numberr+1):
   if numberr%i==0:
    lista.append(i)

print(lista)  """  
# Exercise 5 (List Overlap)
# write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
'''b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,89]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,89 ,89]
c=[]
for i in a:
    if i in b:
        c.append(i)

print(set(c))'''
# Exercise 6 (String Lists)
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
'''stringList=list(input('enter a name list: '))

print(stringList)
stringList.reverse()
print(stringList)

wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")'''

# Exercise 7 (List Comprehensions)
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes 
# a new list that has only the even elements of this list in it.
'''a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100,100]

EVEN=[x for x in a if x%2==0]
   
print(set(EVEN))'''

# Exerscise 8 (Rock Paper Scissors)
# Make a two-player Rock-Paper-Scissors game
'''def compare(u1,u2):
    if ((u1=='Rock')and(u2=='Rock')) or ((u1=='Scissor')and(u2=='Scissor')) or (u1=='papre')and(u2=='papre') :
        return('barabr')
    else:
        print('enter unvalid input!')


    if u1=='Rock':
        if u2=='Scissor':
            return('Rock win') 
        else:
            return('papre win') 
    elif u1=='papre':
        if u2=='Rock':
            return('papre win') 
        else:
            return('Scissor win')  
    elif u1== 'Scissor':
        if u2=='Paper':
            return('Scissor')
        else:
            return('Rock')   

while True:
    gamer1=input('do yo want to choose rock, paper or scissors? ')
    gamer2=input('do yo want to choose rock, paper or scissors?')
    print(compare(gamer1,gamer2))

    answer=input('Do you continue? (yes/no)')
    if answer =='yes':
        continue
    else:
        break'''
    

# Exercise 9 (Guessing Game One)
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
'''import random
numrandom=random.randint(2,9)
print(numrandom)


def compare(ueGuess):  
     if numrandom<int(ueGuess):
        print('geuss a lower number')
     elif numrandom>int(ueGuess):
        print('geuss a bigger number') 
     else:
            print('corrct')
            exit()
print('You can try 3 times')    
for i in range(1,4):
    userInput=input('Enter a guess number= ')
    compare(userInput)
    
    print('--------------------')
    print(f' The number of chances that you tried is {i} ' )

print('--------------------')
print('SRY ! YOU LOSE')'''

# Exercise 10 (List Overlap Comprehensions)
# This week’s exercise is going to be revisiting an old exercise (see Exercise 5),
#  except require the solution in a different way.
'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,13]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,13]
overlap=[x for x in a if x in b]
print(set(overlap))'''

#Exercise11
# intersection between  random number of (a and b)
'''import random
c=random.sample(range(1,30),10)
d=random.sample(range(1,30),16)
overlapran=[x for x in c if x in d]
"""result=[i for i in overlapran if ]
"""
#c-d
result=[]
for i in c:
    if i not in d:
        result.append(i)
print((overlapran)) 
print(result)'''
# Exercise 12 (Check Primality Functions)
# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).
'''num = int(input('Insert a number: '))
a = [x for x in range(2, num) if num % x == 0]
def is_prime(n):
	if num > 1:
		if len(a) == 0:
			print ('prime')
		else:
			print ('NOT prime')
	else:
		print ('NOT prime')
	
is_prime(num)'''
# Exercise 13 (List Ends)
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function

'''listt=[]
num = int(input('Insert a number: '))
for i in range(0,num):
    a=int(input())
    listt.append(a)

print(listt) 

def LastFirst(li):
    return  [li[0] , li[-1]]

print(LastFirst(listt))'''


#Exercise15
# Fibonacci    
'''num=int(input('How many numbers do you want to enter? '))  
def fib(x):
    if x== 1 or x==2:
        return 1
    else:
        return fib(x-2)+ fib(x-1)
 

seri=[fib(i) for i in range(1,num+1)]
print(seri)            
print(sum(seri)) '''       

#Exercise16
# .Write a program (function!) that takes a list and returns a new list 
# that contains all the elements of the first list minus all the duplicates.
'''a=int(input('Enter a number for lenght of List= '))
MainList=[]
for i in range(0,a):
    num=int(input())
    MainList.append(num) 

#with set
def duplicated(l):
    print(MainList)
    s=set(MainList)
    return list(s)


print(duplicated(MainList))

#with loop
newlist=[]
def duplicatedLoop(L):
    for i in MainList:
      if i not in newlist:
         newlist.append(i)

    print(newlist)       
                     


duplicatedLoop(MainList)'''

#Exercise 17
#List reverse 
'''MainList=['hanieh', 'is', 'my','name']
m=[1,2,3,4]
m.reverse()
print(m)

def Reverselist(a):
    a.reverse()
    print(a)

Reverselist(MainList)
#Word reverse with split and join
MainWord="My name is Hanieh"
def ReverseWords(a):
    ListNew=[]
    y=MainWord.split()
    y.reverse()
    return (" ".join(y))
print(ReverseWords(MainWord))'''
#Exercise 17
#Create a program that asks the user to enter their name and their age. Print out a message addressed 
# to them that tells them the year that they will turn 100 years old
'''import datetime

name=input('Enter your name= ')
age= int(input('Enter your age= '))
Date_time=datetime.datetime.now()
year=int(Date_time.year)
brith_year=year-age
print(f'Current yaer is {year}')
print(f'Dear {name}, you will be 100 years old in {brith_year+100}')'''
#Exercise 18
#Implement a function that takes as input three variables,
# and returns the largest of the three.
'''a= int(input('Enter fisrt number= '))
b= int(input('Enter second number= '))
c= int(input('Enter third number= '))
if a>b and a>c:
    print(f'Max is {a}')
elif b>a and b>c:
    print(f'Max is {b}')
elif c>a and c>b:
    print(f'Max is {c}')'''
# Exercise 19 (Password Generator)
# a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password.

'''import random
NumberPass=int(input('How many Password do you want?'))
NumberLen=int(input('How many Character do you want to have your password?'))
PassStrong='1234567890qwertyuiopasdfghjklxcvbnmQWERTYUIOPASDFGHJKLZCVBNM!@#$%^&*'
PassWeak='1234567890'
UserAskPass=input('Do you want stong or weak password? ')
if UserAskPass.lower()=='strong':
    for i in range(NumberPass):
        password=''
        for c in range(NumberLen):
            password+=random.choice(PassStrong)
        print(password) 
elif UserAskPass.lower()=='weak':
    for i in range(NumberPass):
        password=''
        for c in range(NumberLen):
            password+=random.choice(PassWeak)
        print(password)
'''
 
#Exercise 20 (Cows And Bulls)
'''
import random
number =str(random.randint(1000,9999))
print(number, type(number))

cows = 0
bulls = 0
guess = 0

digit = list(str(number))
print(digit, type(digit))

while True:
    cows = 0
    bulls = 0
    select_number = input('enter a number(1000,9999):')
    s_digit  = list(select_number)
    if select_number == number:
        print ('well done!')
        break
    else:
        for i in range(len(digit)):
            if digit[i] == s_digit[i]:
                cows += 1
            else:
                bulls += 1
        guess += 1
        print(f'{select_number}you have got {cows} cows and {bulls} bulls')
        print(f'you guess {guess} times.')
'''
#Exercise 21 liner search
'''listOrder=[1,2,3,4,5,6,7,8,9,10,11,12]

def Sreach(L,x):
    mid=(L[0]+L[-1])/2
    if x==mid:
        print("mid")   
    elif x<mid and x in listOrder:
           
           print('left')
    elif x>mid and x in listOrder:
    
           print('right')
    else:
           print('not found')    
  
    
Sreach(listOrder,2)
'''
#Exercise 22
# binary search
'''
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == x:
          return mid
        elif arr[mid] > x:
          return binary_search(arr, low, mid - 1, x)
        else:
          return binary_search(arr, mid + 1, high, x)
    else:   
        return -1
          
numbers = [1,2,3,4,5,6,7]
numbers.sort()
search_num = int(input("Enter your search number: "))
low = 0
high = len(numbers) - 1
result = binary_search(numbers, low, high, search_num)
if result != -1:
    print(f'search number is found at index {result}')
else:
    print('search number is not found')
'''

#Exercise 23
# File Overlap
'''
def prime():
    with open (r'E:\Untitled Folder\Python\listPrime.txt','r') as f:
     matn=list(f.read().split(","))
      
      return(matn)
def happy(): 
   with open (r'E:\Untitled Folder\Python\ListHappy.txt','r') as f:
      matnHappy=list(f.read().split(","))
      
      return(matnHappy)  

overlap=[x for x in  prime() if x in happy()] 
print(overlap)
'''

#Exercise24 
# Birthday Dictionaries
'''
Dictionary_Brith={'hanieh':'1999','hanna':'2000','ali':'2023'}

userName=input('Enter a name for searching the date of brith= ')


print( 'Brithday of '+userName  +'  is '+ Dictionary_Brith[userName])
'''
#Exercise 25
# Draw A Game Board
'''
def drawboard(kamal):
    kamal = int(kamal)
    i = 0
    ho = "--- "
    ve = "|   "
    ho = ho * kamal
    ve = ve * (kamal+1)
    while i < kamal+1:
        print(ho)
        if not (i == kamal):
            print(ve)
        i += 1
       
drawboard(3)    

print('{:' '<20}'.format('---'))
'''
#Exercise 26
#sum 1 -100
'''  
n=int(input()) 
for i in range (1,n):
    m=n*(n+1)/2
print (m)
'''




    









