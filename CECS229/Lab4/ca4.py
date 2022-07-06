## Abhishek Jasti
## ID: 016784623

import math
import cmath
# from plotting import plot
# import image

def translate(S, z0):
    T = set()
    for i in S:
        i = i + z0
        T.add(i)
    return T

# S = {2 + 2j, 3 + 2j , 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}
# print(translate(S,-3-2j))

def scale(S, k):
    if k <= 0 : raise ValueError
    T = set()
    for i in S:
        i = i*k
        T.add(i)
    return T

def rotate(S, theta):
    T = set()
    for i in S:
        i = i*math.e**(1j*theta)
        T.add(i)
    return T
# s = {2 + 2j, 3 + 2j , 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}
# print(rotate(s, -math.pi))

class Vec:
    def __init__(self, contents = []):
       self.elements = contents

    def __abs__(self):
        v = 0
        for i in self.elements:
            v += i**2
        return (math.sqrt(v))

    def __add__(self, other):
        #return Vec(self.elements + other)
        if(len(self.elements) == len(other.elements)):
            T = [None]*len(self.elements)
            for i in range(0,len(self.elements)):
                T[i] = self.elements[i] + other.elements[i]
        else:
            raise ValueError
        return Vec(T)
    def __sub__(self, other):
        if(len(self.elements) == len(other.elements)):
            T = [None]*len(self.elements)
            for i in range(0,len(self.elements)):
                T[i] = self.elements[i] - other.elements[i]
        else:
            raise ValueError
        return Vec(T)

    def __mul__(self, other):
        if type(other) == Vec:
            m = 0
            if(len(self.elements) == len(other.elements)):
                for i in range(0,len(self.elements)):
                    m += self.elements[i] * other.elements[i]
                return m
            else:
                raise ValueError        
        elif type(other) == float or type(other) == int:
            m = [None]*len(self.elements)
            for i in range(0,len(self.elements)):
                m[i] = self.elements[i]*other
        return Vec(m)

    def __rmul__(self, other):
        m = [None]*len(self.elements)
        for i in range(0,len(self.elements)):
            m[i] = self.elements[i]*other
        return Vec(m)

    def __str__(self):

        return str(self.elements)

# u = 10
# v = Vec([1, 2, 3])
# # #print(type(u.elements[0]))
# print(u*v)