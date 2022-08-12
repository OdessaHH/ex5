# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


"""1"""
"""
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

sum = a + b + c
if a == b == c:
    print("the triple sum is: ")
    print(sum * 3)
else:
    print("the sum is: ")
    print(sum)
"""

"""2"""

"""
a = int(input("enter first number: "))
b = int(input("enter second number: "))

if a > b:
    print("the result of calculation is: ")
    print((a - b)* 2 )

if b >= a:
    print("the result of calculation is: ")
    print(abs(b-a))
"""


"""3"""

"""
num = int(input("number to check: "))
if num % 2 == 0:
    print("this number is even!!")
else:
    print("this number is odd")
"""


"""4"""


"""
import math

r = float(input("Input the radius of the circle: "))
A = round((math.pi * (r * r)),2)


print("The area of the circle with radius ",r, " is ", A)

#answer = str(round(answer, 2))
"""
"""5"""

"""
a = 8
inp = 0  #int(input("guess a number between 1 and 10."))

while a != inp:
    inp =  int(input("guess a number between 1 and 10: "))
    print("guess a number between 1 an 10 until you get it right!")

    if inp == a:
        print("you guessed it right!")
        break
"""










"""6"""
"""
inp1 = str(input("Input the scale shortcut you'd like to convert (F - Fahrenheit, C - Celsius: C)"))
inp2 = int(input("Input the value of temperature you'd like to convert  :"))

if inp1 == "C":
    print("The temperature in Fahrenheit is:", inp2 * (9/5)+32)

if inp1 == "F":
    print("The temperature in Celsius is:",(inp2 - 32)* (5/9))
"""


#(0 °C × 9/5) + 32 = 32 °F

#(32 °F − 32) × 5/9 = 0 °C



"""7"""
"""
print(" *\n","* "*2 ,"\n", "* " * 3,"\n","* " * 4,"\n", "* " *5)
print(" *"*4 ,"\n", "* " * 3,"\n","* " * 2,"\n", "* " )
"""

"""8"""



#fib = []
#for i in range(0,50):

"""
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f0 = 0
    f1 = 1
    for i in range(n-1):
        f = f0 + f1
        f0 = f1
        f1 = f
    return f
 
print(fibonacci(22))
"""


def fib(n):

    a = 0
    b = 1
    print(a)
    print(b)


    for i in range(2,n):
        c = a + b
        a = b
        b = c

        print(c)



fib(10)