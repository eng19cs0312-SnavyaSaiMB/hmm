#!/usr/bin/env python
# coding: utf-8

# In[ ]:


A=int(input("Enter a value"))

B=int(input("enter a value"))
C=int(input("enter a value"))


# In[ ]:


if((A>B) and (A>C)):
    print("LARGEST A")
elif((B>A) and (B>C)):
     print("LARGEST B")
else:
            print("LARGEST B")
            


# In[ ]:


3*9


# In[ ]:


"*"*4


# In[ ]:


name="john smith"


# In[ ]:


name[1]


# In[ ]:


name[-2]


# In[ ]:


name[1:-1]


# In[ ]:


len(name)


# In[ ]:


{2+2}


# In[ ]:


{10%3}


# In[ ]:


{2+2}+{10%3}


# In[ ]:


name="john smith"
name.title()


# In[ ]:


name.strip()


# In[ ]:


name.find("john")


# 10/3

# In[ ]:


105//3


# In[ ]:


10 ** 3


# In[ ]:


x=1


# In[ ]:


print(x)


# In[ ]:


x+=2


# In[ ]:


round(4.444)


# In[ ]:


float(1)


# In[ ]:


bool("False")


# In[ ]:


10 == "10"


# In[ ]:


"bag" =="apple"


# In[ ]:


not(True or False)


# In[ ]:


age=12
18<=age<65


# In[ ]:


x=range(1,10,2)


# In[ ]:


print(x)


# In[ ]:


x = range(6)

for n in x:
    print(n)


# In[1]:


range(1,4,1)


# In[5]:


for i in range(1,10,2):
    print (i)


# In[1]:


#Write a function that returns the maximum of two numbers.
def max(a,b):
    
    if a>b:
        print("max is a:",a)
    else:
        print("max is b:",b)
a=int(input("enter 1st no"))
b=int(input("enter 2nd no"))
max(a,b)


# In[2]:


def fizz_buzz(n):
    if (n%3==0 and n%5==0):
        print("FizzBuzz")
    elif n%5==0:
        print("Buzz")
    elif n%3==0:
        print("Fizz")
n=int(input("Enter a number"))
fizz_buzz(n)


# In[3]:


def drivers(speed):
    if speed<70:
        print("Ok")
    elif speed>70:
        d = (speed-70)/5
        print("demerit is:",d)
        if d>12:
            print("License suspended")
speed = int(input("Enter speed"))
drivers(speed)


# In[12]:


def sum(limit):
    for n in range(1,limit+1):
        if n%3==0 or n%5==0:
            print (n)
limit=int(input("enter the value of n "))
print(sum(limit))


# In[6]:


def show_numbers(limit):
    for n in range(0,limit+1):
        if n%2==0:
            print("even",n)
        else:
            print("odd",n)
n=int(input("enter the value of n"))
show_numbers(n)


# In[13]:


def show_stars(rows):
    for i in range(1,rows+1):
        for j in range(1,i+1):
            print("*",end="")
        print("\n")
r= int(input("Enter the number of rows"))
show_stars(r)


# In[3]:


file=input("ener");
inputfile=open(file,"r")
for line in inputfile:
    print(line)


# In[ ]:




