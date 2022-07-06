#ca2.py
from math import remainder


def primes(a,b):
    if(a<1):raise ValueError
    if(b<a):raise ValueError
    p = set()
    trash = set()
    for i in range(0,b+1):
        p.add(i)
    for i in p:
        if((i%2 == 0 and i != 2) or (i%3 == 0 and i != 3) or (i%5 == 0 and i != 5) or (i%7 == 0 and i != 7) or (i == 1)):
            trash.add(i)
    p = p.difference(trash)     
    for i in p:
        for j in p:
            if (i%j == 0 and i!=j):
                trash.add(i)
    for i in p:
        if(i < a):
            trash.add(i)
    p = p.difference(trash)
    return(p)

# print(primes(43,157))

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

print(bezout_coeffs(414, 662))

def gcd(a,b):
    c = bezout_coeffs(a,b)
    s = c[a]
    t = c[b]
    d = (a*s)+(b*t)

    return abs(d)

#(print(gcd(-76, -184)))

