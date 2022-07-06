#!/usr/bin/env python
# coding: utf-8

# # CECS 229: Coding Assignment #1
# 
# #### Due Date: 
# 
# Sunday, 2/6 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment you must submit the following by the due date:
# 
# 1. **To the BB Dropbox Folder:** this completed .ipynb file
# 
# 2. **To CodePost:** this file converted to a Python script named `ca1.py`
# 
# #### Objectives:
# 
# 1. Compute the quotient and remainder of two numbers.
# 2. Apply numerical algorithms for computing the sum of two numbers in binary representation.
# 3. Apply numerical algorithms for computing the modular exponentiation of a positive integer.
# 
# 

# --------------------------------
# 
# #### Problem 1:
# 
# Program a function `div_alg(a, d)` that computes the quotient and remainder of two integers `a` and `d`, according to the Division Algorithm (THM 4.1.1).   
# 
# The function should satisfy the following:
# 
# 1. INPUT: 
#     * `a` - an integer representing the dividend
#     * `d` - positive integer representing the divisor
# 
#     
# 2. OUTPUT:
#     * a dictionary of the form `{'quotient' : q, 'remainder' : r}` where `q` and `r` are the quotient and remainder values, respectively.  The remainder should satisfy, $0 \leq r < d$.
# 
#  
# EXAMPLE: 
# 
# `>> div_alg( 101 , 11 )`
# 
# `{'quotient' : 9, 'remainder' : 2}`
# 
# 
# 

# In[1]:


def div_alg(a, d):
    quotient = int(a//d)
    remainder = (a-d*quotient)
    return {'quotient': quotient, 'remainder': remainder} 


# --------------------------------
# 
# #### Problem 2:
# 
# Program a function `binary_add(a, b)` that computes the sum of the binary numbers  $$a = (a_{i-1}, a_{i-2}, \dots, a_0)_2$$ and $$b = (b_{j-1}, b_{j-2}, \dots, b_0)_2$$ using the algorithm discussed in lecture.  No credit will be given to functions that employ any other implementation.  The function can not use built-in functions that already perform some kind of binary representation or addition of binary numbers.  For example, the function implementation can **not** use the functions `bin()` or `int(a, base=2)`.
# 
# The function should satisfy the following:
# 
# 1. INPUT: 
#     * `a` - a string of the 0's and 1's that make up the first binary number.  The string *may* contain spaces.
#     * `b` - a string of the 0's and 1's that make up the first binary number.  The string *may* contain spaces.
# 
#     
# 2. OUTPUT:
#     * the string of 0's and 1's that is the result of computing $a + b$.  The string must be separated by spaces into blocks of 4 characters or less, beginning at the end of the string.
# 
#  
# EXAMPLE: 
# 
# `>> binary_add( '10 1011' , '11011')`
# 
# `'100 0110'`
# 
# 
# 

# In[4]:


def binary_add(a,b):
    c=0
    a = a.replace(" ", "")
    b = b.replace(" ", "")

    max_length = max(len(a),len(b))

    s = ""

    if len(a) > len(b):
        zeros_to_add = len(a)-len(b)
        while zeros_to_add > 0:
            b = str(0)+b
            zeros_to_add -= 1
    elif len(b) > len(a):
        zeros_to_add = len(b)-len(a)
        while zeros_to_add > 0:
            a = str(0)+a
            zeros_to_add -=1

    count = 0
    i = max_length - 1
    while i>=0:
        bit_add = (int(a[i])+int(b[i])+c)%2
        s = str(bit_add) + s
        c = (int(a[i])+int(b[i])+c)//2      
        i -=1
        count += 1
        if(count%4==0):
            s = " " + s
    if(c == 1):
        s = str(c) + s

    return s


# --------------------------------
# 
# #### Problem 3:
# 
# Program a function `mod_exp(b, n, m)` that computes $$b^n \mod m$$ using the algorithm discussed in lecture.  No credit will be given to functions that employ any other implementation.  For example, if the function implementation simply consists of `b ** n % m`, no credit will be given.  
# 
# The function should satisfy the following:
# 
# 1. INPUT: 
#     * `b` - positive integer representing the base
#     * `n` - positive integer representing the exponent
#     * `m` - positive integer representing the modulo
# 
#     
# 2. OUTPUT:
#     * the computation of $b^n \mod m$ if b, n, m are positive integers, 0 otherwise.
# 
#  
# EXAMPLE: 
# 
# `>> mod_exp( 3 , 644, 645 )`
# 
# `36`
# 
# 
# 

# In[ ]:


def mod_exp(b, n, m):
    x = 1
    p = b%m
    if (b <= 0 or n <= 0 or m <= 0): return 0

    while(n>0):
        if ((n&1) == 1):
            x = (x*p)%m
        n = n >> 1
        p = (p*p)%m
    return x


# In[ ]:




