#1.

import math
import numpy

def func_fm(x):
    C=50
    H=30
    Q=[ math.sqrt((2*C*D)/H)  for D in x ]
    print(Q)

func_fm([20,30])


#2. 
class Shape(object):
    def __init__(self):
       pass

    def func_area(self):
        return 0

class Square (Shape):
    def __init__(self,l):
        self.length = l

    def func_area(self):
        print("Area of the square :"+ str(self.length*self.length))


class Rectangle (Shape):
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

    def func_area(self):
        print("Area of the rectangle :"+ str(self.length*self.breadth))

x= Square(7)
x.func_area()

y=Rectangle(7,9)
y.func_area()


#3.

class ddd(object):

        def __init__(self,x):
            result= []
            for i in range(len(x)):
               if i[0]+i[1]+i[2]==0:
                   print(i)

t= [-25,-10,-7,-3,2,4,8,10]
a= ddd(t)


#4. What is the output of the following code? Explain your answer as well.


class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x,b.y)
main()

#there will be an "AttributeError" error, since Derived_Test object has no attribute 'x' but only 'y'

class A:
    def __init__(self, x= 1):
        self.x = x
class der(A):
    def __init__(self,y = 2):
        super().__init__()
        self.y = y
def main():
    obj = der()
    print(obj.x, obj.y)
main()


#Output will be (1 2) since  "der" class is using  the super() function to inherit the init function from the A class ( here x = 1 and y=2)

class A:
    def __init__(self,x):
        self.x = x

    def count(self,x):
        self.x = self.x+1

class B(A):

    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y

    def count(self):
        self.y += 1

def main():
    obj = B()
    obj.count()
    print(obj.x, obj.y)

main()


# Output will be (3 1) since B class inherits the x value from the class A , but the count function in class B adds a count to y making it 1

class A:
    def __init__(self):
        self.multiply(15)
        print(self.i)

    def multiply(self, i):
        self.i = 4 * i;


class B(A):
    def __init__(self):
        super().__init__()

    def multiply(self, i):
        self.i = 2 * i;


obj = B()

# output will be 30 since the value i(15) is  inherited from a function in Class A and later multiplied with 2.



#5.
class Time():
    def __init__(self, hours, mins):
        self.hours = hours
        self.mins = mins

    def addTime(time1, time2):
        time3 = Time(0, 0)
        if time1.mins + time2.mins > 60:
            time3.hours = (time1.mins + time2.mins) / 60
        time3.hours = time3.hours + time1.hours + time2.hours
        time3.mins = (time1.mins + time2.mins) - (((time1.mins + time2.mins) / 60) * 60)
        return time3

    def displayTime(self):
        print("Time is: ", round(self.hours), "hours and", round(self.mins), "minutes.")

    def displayMinute(self):
        print("Total mins in time: ",round((self.hours * 60)))


x = Time(2,50)
y = Time(1,20)
z = Time.addTime(x,y)
z.displayTime()
z.displayMinute()


#6.

class Person:
    def __init__(self,age):
        self.age=age

        if self.age<0:
            print("Age is not valid , setting age to 0")

            self.age=0

    def yearPasses(self):
        self.age += 1

    def amIOld(self):

        if (self.age<10):
            print("You are young")

        elif(10<self.age<20):
            print("You are a teenager")
        else:
            print("You are old")



sf=Person(15)

sf.amIOld()







