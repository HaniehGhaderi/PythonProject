class Calculator:
    def __init__(self,x,y):
      self.x=x
      self.y=y
    def add(self):
     print(f'{x}+{y}={x+y}') 
    def subtract(self):
     print(f'{x}-{y}={x-y}') 
    def multiply(self):
     print(f'{x}*{y}={x*y}')        
    def divide(self):
     print(f'{x}/{y}={x/y}')
 


x=int(input('Please Enter first number='))
y=int(input('Please Enter second number='))
s=input('Please choose one operator:( + , - , * , / ) ')
Result=Calculator(x,y)
if s == '+':
    Result.add()
elif s == '-':
    Result.subtract() 
elif s == '*':
    Result.multiply()   
elif s == '/':
    Result.divide()              


