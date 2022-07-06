import string


def modinv(a,m):
    g = gcd(a,m)

    if(g[1]!= 1): 
        print("The given values are not relatively prime")
        raise ValueError
    
    for i in range(0, m, 1):
        if((a*i)%m == 1):
            break
    return i

    
def affineEncrypt(text, a, b):
    g = gcd(a,26)

    if(g[1]!=1):
        print("The given key is invalid. The gcd(a,26) must be 1.")
        raise ValueError
    e = letters2digits(text)
    #print(e)
    n = 2
    en = [(e[i:i+n]) for i in range(0, len(e), n)]
    #print(en)
    enc = [None]*(len(en))
    for i in range(0,len(en)):
        enc[i] = str((a*(int(en[i]))+b)%26)
        if int(enc[i]) < 10:
            enc[i] = "0" + enc[i]
    s = ""
    s = s.join(enc)
    return digits2letters(s)
        
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
        
def encryptRSA(m, n, e):
    en = letters2digits(m)
    enc = blocksize(n)
    b = [None]*(int((len(en)/enc)))
    c = ""
    for i in range(0,int(len(en)/enc)):
        b[i] = en[(i*enc):enc+(i*enc)]
    for i in b:
        i = (int(i)**e)%n
        if(len(str(i)) == 3):
            c += "0" + str(i) + " "
        elif(len(str(i)) == 2):
            c += "00" + str(i) + " "
        elif(len(str(i)) == 1):
            c += "000" + str(i) + " "
        else:
            c += str(i) +" "
    return c

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

# print(decryptRSA("2081 2182 1346", 43, 59, 13))
# print(encryptRSA("ATTACK", 2623, 89))
# print(bezout_coeffs(3,19))
# print(gcd(3,19))
# print(modinv(3,19))
# print(affineEncrypt("STOP POLLUTION", 7, 5))
# print(affineDecrypt("AGBCSGYVLDGE", 3, 16))