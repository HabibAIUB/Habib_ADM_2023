#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Hello World
if __name__ == '__main__':
    print("Hello, World!")


# In[2]:


# If-Else

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n%2 ==1:
    print("Weird")
elif n>=2 and n<=5:
    print("Not Weird")
elif n>=6 and n<=20:
    print("Weird")
elif n>20 and n<=100:
    print("Not Weird")


# In[4]:


# Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


# In[6]:


# Division
   
if __name__ == '__main__':
   a = int(input())
   b = int(input())
   print (a//b)
   print (a/b)


# In[7]:


# Loops

if __name__ == '__main__':
    n = int(input())
for i in range(n):
    print(i**2)


# In[8]:


# Write a function

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 ==0:
            if year % 400 ==0:
                leap = True 
            else: 
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))


# In[12]:


if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end="")

