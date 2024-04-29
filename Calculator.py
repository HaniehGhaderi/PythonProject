
def add(x,y):
    print(f'{x}+{y}={x+y}') 
def subtract(x,y):
    print(f'{x}-{y}={x-y}') 
def multiply(x,y):
    print(f'{x}*{y}={x*y}')        
def divide(x,y):
    print(f'{x}/{y}={x/y}') 


print('Please Enter first number=')
x=int(input())
print('Please Enter second number=')
y=int(input())
print('Please choose one operator:( + , - , * , / ) ')
s=input()
if s == '+':
    add(x,y)
elif s == '-':
    subtract(x,y) 
elif s == '*':
    multiply(x,y)   
elif s == '/':
    divide(x,y)              


