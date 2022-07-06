#!/usr/bin/env python
# coding: utf-8

# # CECS 229 Coded HW #3
# 
# #### Due Date: 
# 
# Sunday, 3/6 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment you must submit the following by the due date:
# 
# 1. **To the BB Dropbox Folder:** this completed .ipynb file
# 
# 2. **To CodePost:** this file converted to a Python script named `ca3.py`
# 
# #### Objectives:
# 
# 1. Find the inverse of a given integer under a given modulo m.
# 2. Encrypt and decrypt text using an affine transformation.
# 3. Encrypt and decrypt text using the RSA cryptosystem.
# 
# 
# 
# 
# ### Programming Tasks
# 
# You may use the utility functions at the end of this notebook to aid you in the implementation of the following tasks:

# -------------------------------------------
# 
# #### Problem 1: 
# Create a function `modinv(a,m)` that returns the smallest, positive inverse of `a` modulo `m`.  If the gcd of `a` and `m` is not 1, then you must raise a `ValueError` with message `"The given values are not relatively prime"`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `ca3.py` file.

# In[ ]:


def modinv(a,m):
    g = gcd(a,m)

    if(g[1]!= 1): 
        print("The given values are not relatively prime")
        raise ValueError
    
    for i in range(0, m, 1):
        if((a*i)%m == 1):
            break
    return i

def bezout_coeffs(a,b):
    s = 1
    t = 0
    new_s = s
    new_t = t
    remainder = 0
    quotient = 0
    afinal = a
    bfinal = b

    quotient = b//a
    remainder = b-(quotient*a)
    new_b = a
    a = remainder
    b = new_b        
    s1 = -quotient
    t1 = 1    

    if(a != 0):
        quotient = b//a
    remainder = b-(quotient*a)

    if(remainder == 0):
        new_s = s1
        new_t = t1

    while (remainder != 0):
        new_b = a
        a = remainder
        b = new_b        
        new_s = s-quotient*s1
        new_t = t-quotient*t1        
        s = s1
        s1 = new_s
        t = t1
        t1 = new_t        
        quotient = b//a        
        remainder = b-quotient*a

    a = afinal
    b = bfinal
    s = new_s
    t = new_t
    
    return {a: s, b: t}

def gcd(a,b):
    c = bezout_coeffs(a,b)
    s = c[a]
    t = c[b]
    d = (a*s)+(b*t)

    return {1:abs(d), a:s, b:t}


# ------------------------------------
# 
# #### Problem 2: 
# Create a function `affineEncrypt(text, a,b)` that returns the cipher text encrypted using key  (`a`, `b`).  You must verify that the gcd(a, 26) = 1 before making the encryption.  If this is not the case, the function must raise a `ValueError` with message `"The given key is invalid. The gcd(a,26) must be 1."`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `ca3.py` file.

# In[ ]:


def affineEncrypt(text, a, b):
    g = gcd(a,26)

    if(g[1]!=1):
        print("The given key is invalid. The gcd(a,26) must be 1.")
        raise ValueError
    e = letters2digits(text)
    n = 2
    en = [(e[i:i+n]) for i in range(0, len(e), n)]
    enc = [None]*(len(en))
    for i in range(0,len(en)):
        enc[i] = str((a*(int(en[i]))+b)%26)
        if int(enc[i]) < 10:
            enc[i] = "0" + enc[i]
    s = ""
    s = s.join(enc)
    
    return digits2letters(s)
 
def digits2letters(digits):
    letters = ""
    start = 0  #initializing starting index of first digit
    while start <= len(digits) - 2:
        digit = digits[start : start + 2]  # accessing the double digit
        letters += chr( int(digit) +65)   # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    return letters

def letters2digits(letters):
    digits = ""
    for c in letters:
        if c.isalpha():
            letter = c.upper()  #converting to uppercase  
            d = ord(letter)-65
            if d < 10:
                digits += "0" + str(d)  # concatenating to the string of digits
            else:
                digits += str(d)
    return digits

def bezout_coeffs(a,b):
    s = 1
    t = 0
    new_s = s
    new_t = t
    remainder = 0
    quotient = 0
    afinal = a
    bfinal = b

    quotient = b//a
    remainder = b-(quotient*a)
    new_b = a
    a = remainder
    b = new_b        
    s1 = -quotient
    t1 = 1    

    if(a != 0):
        quotient = b//a
    remainder = b-(quotient*a)

    if(remainder == 0):
        new_s = s1
        new_t = t1

    while (remainder != 0):
        new_b = a
        a = remainder
        b = new_b        
        new_s = s-quotient*s1
        new_t = t-quotient*t1        
        s = s1
        s1 = new_s
        t = t1
        t1 = new_t        
        quotient = b//a        
        remainder = b-quotient*a

    a = afinal
    b = bfinal
    s = new_s
    t = new_t
    
    return {a: s, b: t}

def gcd(a,b):
    c = bezout_coeffs(a,b)
    s = c[a]
    t = c[b]
    d = (a*s)+(b*t)

    return {1:abs(d), a:s, b:t}


# #### Problem 3: 
# Create a function `affineDecrypt(ciphertext, a,b)` that returns the cipher text encrypted using key  (`a`, `b`). You must verify that the gcd(a, 26) = 1.  If this is not the case, the function must raise `ValueError` with message `"The given key is invalid. The gcd(a,26) must be 1."`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `ca3.py` file.

# In[ ]:


def affineDecrypt(ciphertext, a, b):
    g = gcd(a,26)
    if(g[1] != 1):
        print("The given key is invalid. The gcd(a,26) must be 1.")
        raise ValueError

    e = letters2digits(ciphertext)
    n = 2
    en = [(e[i:i+n]) for i in range(0, len(e), n)]
    enc = [None]*(len(en))
    ainv = modinv(a,26)
    for i in range(0, len(en)):
        enc[i] = str((ainv*(int(en[i])-b)%26))
        if int(enc[i]) < 10:
            enc[i] = "0" + enc[i]
    s = ""
    s = s.join(enc)
    return digits2letters(s)
        
def digits2letters(digits):
    letters = ""
    start = 0  #initializing starting index of first digit
    while start <= len(digits) - 2:
        digit = digits[start : start + 2]  # accessing the double digit
        letters += chr( int(digit) +65)   # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    return letters

def letters2digits(letters):
    digits = ""
    for c in letters:
        if c.isalpha():
            letter = c.upper()  #converting to uppercase  
            d = ord(letter)-65
            if d < 10:
                digits += "0" + str(d)  # concatenating to the string of digits
            else:
                digits += str(d)
    return digits

def modinv(a,m):
    g = gcd(a,m)

    if(g[1]!= 1): 
        print("The given values are not relatively prime")
        raise ValueError
    
    for i in range(0, m, 1):
        if((a*i)%m == 1):
            break
    return i


# -----------------------------------
# 
# #### Problem 4:
# 
# Implement the function `encryptRSA(m, n, e)` which encrypts a string `m` using RSA key `(n = p * q, e)`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented for previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `ca3.py` file.

# In[ ]:


def encryptRSA(m, n, e):
    en = letters2digits(m)
    enc = blocksize(n)
    b = [None]*(int((len(en)/enc)))
    c = ""
    for i in range(0,int(len(en)/enc)):
        b[i] = en[(i*enc):enc+(i*enc)]
    for i in b:
        i = (int(i)**e)%n
        if(len(str(i)) != 4):
            c += "0" + str(i) + " "
        else:
            c += str(i) +" "
    return c

def letters2digits(letters):
    digits = ""
    for c in letters:
        if c.isalpha():
            letter = c.upper()  #converting to uppercase  
            d = ord(letter)-65
            if d < 10:
                digits += "0" + str(d)  # concatenating to the string of digits
            else:
                digits += str(d)
    return digits

def blocksize(n):
    """returns the size of a block in an RSA encrypted string"""
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2
    


# In[ ]:


"""--------------------- ENCRYPTION TESTER CELL ---------------------------"""
encrypted1 = encryptRSA("STOP", 2537, 13)
encrypted2 = encryptRSA("HELP", 2537, 13)
encrypted3 = encryptRSA("STOPS", 2537, 13)
print("Encrypted Message:", encrypted1)
print("Expected: 2081 2182")
print("Encrypted Message:", encrypted2)
print("Expected: 0981 0461")
print("Encrypted Message:", encrypted3)
print("Expected: 2081 2182 1346")


"""--------------------- TEST 2 ---------------------------"""
encrypted = encryptRSA("UPLOAD", 3233, 17)
print("Encrypted Message:", encrypted)
print("Expected: 2545 2757 1211")


# -------------------------------------------------------
# 
# #### Problem 5:
# 
# Complete the implementation of the function `decryptRSA(c, p, q, m)` which depends on `modinv(a,m)` and the given functions `digits2letters(digits)` and `blockSize(n)`.  When you are done, you can test your function against the given examples.

# In[2]:


def decryptRSA(c, p, q, e):
    m = (p-1)*(q-1)
    einv = modinv(e, m)
    d = c.split(" ")
    a = ""
    n = 2
    
    for i in d:
        i = mod_exp(int(i), einv, (p*q))
        if len(str(i)) == 3:
            a += "0" + str(i)
        elif len(str(i)) == 2:
            a += "00" + str(i)
        elif len(str(i)) == 1:
            a += "000" + str(i)
        else:
            a += str(i)
    return(digits2letters(a))

def modinv(a,m):
    g = gcd(a,m)

    if(g[1]!= 1): 
        print("The given values are not relatively prime")
        raise ValueError
    
    for i in range(0, m, 1):
        if((a*i)%m == 1):
            break
    return i

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

def digits2letters(digits):
    letters = ""
    start = 0  #initializing starting index of first digit
    while start <= len(digits) - 2:
        digit = digits[start : start + 2]  # accessing the double digit
        letters += chr( int(digit) +65)   # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    return letters


# In[3]:


"""--------------------- TESTER CELL ---------------------------"""
decrypted1 = decryptRSA("2081 2182", 43, 59, 13)
decrypted2 = decryptRSA("0981 0461", 43, 59, 13)
decrypted3 = decryptRSA("2081 2182 1346", 43, 59, 13)
print("Decrypted Message:", decrypted1)
print("Expected: STOP")
print("Decrypted Message:", decrypted2)
print("Expected: HELP")
print("Decrypted Message:", decrypted3)
print("Expected: STOPSX")

"""--------------------- TEST 2---------------------------"""
decrypted = decryptRSA("0667 1947 0671", 43, 59, 13)
print("Decrypted Message:", decrypted)
print("Expected: SILVER")


# ------------------------------------------
# ##### Utility functions (NO EDITS NECESSARY)

# In[ ]:


def digits2letters(digits):
    letters = ""
    start = 0  #initializing starting index of first digit
    while start <= len(digits) - 2:
        digit = digits[start : start + 2]  # accessing the double digit
        letters += chr( int(digit) +65)   # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    return letters
    


# In[ ]:


def letters2digits(letters):
    digits = ""
    for c in letters:
        if c.isalpha():
            letter = c.upper()  #converting to uppercase  
            d = ord(letter)-65
            if d < 10:
                digits += "0" + str(d)     # concatenating to the string of digits
            else:
                digits += str(d)
    return digits


# In[ ]:


def blocksize(n):
    """returns the size of a block in an RSA encrypted string"""
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2

