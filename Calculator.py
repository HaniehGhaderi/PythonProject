class Calculator:
    #constructor Method
    def __init__(self,x,y):
      self.x=x
      self.y=y
     #Method for calculating (+,/, *, -)   
    def add(self):
     print(f'{x}+{y}={x+y}') 
    def subtract(self):
     print(f'{x}-{y}={x-y}') 
    def multiply(self):
     print(f'{x}*{y}={x*y}')        
    def divide(self):
     print(f'{x}/{y}={x/y}')

        
 
class Pi():
    
    pa=4
    #No one can change the pi number because it is a private instance variable
    def setter_Pi(self,pi,pa):
        self.__pi=3.14
        self.pa=pa

    def getter_Pi(self):
        print(f'The number of Pi is {self.__pi}, and no one can change it.') 
        print(f' The pa ({self.pa}) is a public instance , and eveyone can modify it.')

#User enter two numbers and an operator
x=int(input('Please Enter first number='))
y=int(input('Please Enter second number='))
s=input('Please choose one operator:( + , - , * , / ) ')

#create an object from Calculator class and give the x and y numbers as its arguman
Result=Calculator(x,y)

#call the methods via their operator
if s == '+':
    Result.add()
elif s == '-':
    Result.subtract() 
elif s == '*':
    Result.multiply()   
elif s == '/':
    Result.divide()  

#create an object from Pi class
p=Pi()
p.setter_Pi(3,2)
# print the changeless pi number. pi is a pivate instance variable, and it is 
# imposible to change it;however, pa is public instance variable, and can be modified esily.  
p.getter_Pi()                


