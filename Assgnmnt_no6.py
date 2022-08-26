#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignement no 6
#python program to display fibonacci sequence 
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
    
nterms = 10
if nterms <= 0:
    print("please enter the positive number")
    
else:
    print("fibonacci sequence")
    for i in range(nterms):
        print(recur_fibo(i))

#Answer no 2
#program to find factorial number using recursion
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
    
num = 7 

if num < 0:
    print("sorry factorial does not exist for negative number")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    print("the factorial of", num, "is ",recur_factorial(num))

#Answer no 3
#program to find body mass index
height = float(input("Enter your height(m):"))
weight = float(input("Enter your weight(kg):"))
print("your BMI is ",round(weight/(height*height),2))

#Answer no 4
#program to find logarithm of any natural number
import math

print(math.log(math.e))
print(math.log(1))
print(math.log(10))

#Answer no 5
#program to find cube sum of first n natural numbers
num = int(input("Enter value of num:"))
sumVal= 0
for i in range(1,num+1):
    sumVal += (i*i*i)
    
print("sum of cubes =", sumVal)

