import numpy as np
from Interfaces import Queue



def left(i : int):
    return (2*i + 1)

def right(i: int):
    return 2*(i+1)

def parent(i : int):
    return (i - 1)//2

class BinaryHeap(Queue):
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) ->np.array:
        return np.zeros(n, np.object)

    def resize(self):
        b = self.new_array(max(1, 2*self.n))
        i = 0
        while(i < self.n):
            b[i] = self.a[i]
            i += 1
        self.a = b

    def add(self, x : object):
        if len(self.a) == self.n:
            self.resize()
        self.a[self.n] = x
        self.n = self.n + 1
        self.bubble_up(self.n-1)

    def bubble_up(self, i):
        if i < 0 or i >= self.n:
            raise IndexError()
        p_idx = parent(i)
        while i>0 and self.a[i] < self.a[p_idx]:
            temp = self.a[i]
            self.a[i] = self.a[p_idx]
            self.a[p_idx] = temp
            i = p_idx
            p_idx = parent(i)

    def remove(self):
        if self.n == 0:
            raise IndexError()
        temp = self.a[0]
        self.a[0] = self.a[self.n-1]
        self.n = self.n - 1
        self.trickle_down(0)
        if len(self.a) == 3*self.n:
            self.resize()
        return temp 

    def trickle_down(self, i):
        while i >= 0:
            s = -1
            r = right(i)
            l = left(i)
            if r < self.n and self.a[r] < self.a[i]:
                if self.a[l] < self.a[r]:
                    s = l
                else:
                    s = r
            else:
                if l < self.n and self.a[l] < self.a[i]:
                    s = l
            if s >= 0:
                temp = self.a[i]
                self.a[i] = self.a[s]
                self.a[s] = temp
            i = s

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i  < self.n-1:
                s += ","
        return s + "]"


