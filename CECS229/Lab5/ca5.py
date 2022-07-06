import math

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

    def norm(self, p):
        if not(isinstance(p, int)):
            raise ValueError
        n = 0.00
        for i in range(0,len(self.elements)):
            n += self.elements[i]**p
        return n**(1/p)

    def __str__(self):
        return str(self.elements)

class Matrix:
    
    def __init__(self):  
        self.colsp = []
        self.rowsp = []

    def __init__(self, rows):
        self.rowsp = rows
        self.colsp = [[None for i in range (0, len(self.rowsp))] for j in range(0, len(self.rowsp[0]))]
        for i in range(0, len(self.rowsp)):
            for j in range(0, len(self.rowsp[0])):
                self.colsp[j][i] = self.rowsp[i][j]

    def set_col(self, j, u):
        j -= 1
        
        if len(self.colsp[j]) != len(u):
            raise ValueError("Incompatible column length.")
        
        self.colsp[j] = u
        
        for i in range(len(self.rowsp)):
            self.rowsp[i][j] = self.colsp[j][i]
    
    def set_row(self, i, v):
        i -= 1
        
        if len(self.rowsp[i]) != len(v):
            raise ValueError("Incompatible row length.")
        
        self.rowsp[i] = v
        
        for j in range(len(self.colsp)):
            self.colsp[j][i] = self.rowsp[i][j]

    # def set_col(self, j , u):
    #     if(len(self.colsp[0]) != len(u)):
    #         print("Incompatible column length.")
    #         raise ValueError
    #     else:
    #         self.colsp.pop(j-1)
    #         self.colsp.insert(j-1,u)
    #         self.rowsp = [[None for i in range (0, len(self.colsp))] for j in range(0, len(self.colsp[0]))]
    #         for i in range(0, len(self.colsp)):
    #             for k in range(0, len(self.colsp[0])):
    #                 self.rowsp[k][i] = self.colsp[i][k]

    # def set_row(self, i , v):
    #     if(len(self.rowsp[0]) != len(v)):
    #         print("Incompatible row length.")
    #         raise ValueError
    #     else:
    #         self.rowsp.pop(i-1)
    #         self.rowsp.insert(i-1, v)
    #         self.colsp = [[None for i in range (0, len(self.rowsp))] for j in range(0, len(self.rowsp[0]))]
    #         for k in range(0, len(self.rowsp)):
    #             for j in range(0, len(self.rowsp[0])):
    #                 self.colsp[j][k] = self.rowsp[k][j]

    def set_entry(self, i, j, x):
        self.rowsp[i-1][j-1] = x
        self.colsp[j-1][i-1] = x

    def get_col(self, j):
        return self.colsp[j-1]

    def get_row(self, i):
        return self.rowsp[i-1]

    def get_entry(self, i, j):
        return self.rowsp[i][j]
    
    def col_space(self):
        return self.colsp

    def row_space(self):
        return self.rowsp
    
    def get_diag(self, k):
        diagonal = []
        k2 = 0
        matrix = self.rowsp
        length = len(matrix)

        if(k == 0):
            while k < length:
                diagonal.append(matrix[k][k])
                k += 1
        elif k > 0:
            while k < length:
                diagonal.append(matrix[k2][k])
                k2 += 1
                k += 1
        else:
            k = abs(k)
            while k < length:
                diagonal.append(matrix[k][k2])
                k2 += 1
                k += 1

        return diagonal

    def __str__(self):
        return '\n'.join([''.join([str(u) + " " for u in row]) for row in self.rowsp])


    def __add__(self, other):
        if not (isinstance(other, Matrix)):
            return ("Not of the same type.")
        
        if(len(self.rowsp) == len(other.rowsp) and len(self.colsp) == len(other.colsp)):
            result = [[None for i in range (0, len(self.colsp))] for j in range(0, len(self.colsp[0]))]
            for i in range (0, len(self.rowsp)):
                for j in range (0, len(self.colsp)):
                    result[i][j] = self.rowsp[i][j] + other.rowsp[i][j]
            M = Matrix(result)
            return M
        else:
            raise ValueError
        
    
    def __sub__(self, other):
        if not (isinstance(other, Matrix)):
            return ("Not of the same type.")
        
        if(len(self.rowsp) == len(other.rowsp) and len(self.colsp) == len(other.colsp)):
            result = [[None for i in range (0, len(self.colsp))] for j in range(0, len(self.colsp[0]))]
            for i in range (0, len(self.rowsp)):
                for j in range (0, len(self.colsp)):
                    result[i][j] = self.rowsp[i][j] - other.rowsp[i][j]
            M = Matrix(result)
            return M
        else:
            raise ValueError
        
        
    def __mul__(self, other):  
        if type(other) == float or type(other) == int:
            result = [[None for i in range (0, len(self.colsp))] for j in range(0, len(self.colsp[0]))]
            for i in range(0, len(self.rowsp)):
                for j in range(0, len(self.rowsp[0])):
                    result[i][j] = self.rowsp[i][j] * other
            M = Matrix(result)
            return M

        elif type(other) == Matrix:
            if(len(self.colsp) == len(other.rowsp)): 
                if(len(self.rowsp) > len(other.colsp)):
                    result = [[0 for i in range (0, len(self.colsp))] for j in range(0, len(other.rowsp))]
                else:
                    result = [[0 for i in range (0, len(other.colsp))] for j in range(0, len(self.rowsp))]
                for i in range(0, len(self.rowsp)):
                    for j in range(0, len(other.colsp)):
                        for k in range(0, len(self.colsp)):
                            result[i][j] += self.rowsp[i][k] * other.colsp[j][k]
                M = Matrix(result)
                return M
            else:
                raise ValueError

        elif type(other) == Vec:
            out = []
            for i in self.rowsp:
                out.append(other * Vec(i))
            return Vec(out)       
    
    def __rmul__(self, other):  
        if type(other) == float or type(other) == int:
            result = [[None for i in range (0, len(self.colsp))] for j in range(0, len(self.colsp[0]))]
            for i in range(0, len(self.rowsp)):
                for j in range(0, len(self.rowsp[0])):
                    result[i][j] = other * self.rowsp[i][j]
            M = Matrix(result)
            return M
        else:
            print("ERROR: Unsupported Type.")
            raise ValueError
        
    def __eq__(self, other):
        """overloads the == operator to return True if 
        two Matrix objects have the same row space and column space"""
        this_rows = self.row_space()
        other_rows = other.row_space()
        this_cols = self.col_space()
        other_cols = other.col_space()
        return this_rows == other_rows and this_cols == other_cols

    def __req__(self, other):
        """overloads the == operator to return True if 
        two Matrix objects have the same row space and column space"""
        this_rows = self.row_space()
        other_rows = other.row_space()
        this_cols = self.col_space()
        other_cols = other.col_space()
        return this_rows == other_rows and this_cols == other_cols


# A = Matrix([ [2, 0], [0, 2], [0, 0], [0, 0]])
# C = Matrix([ [2, 0], [0, 2], [0, 0], [0, 0]])

'''TESTER CELL FOR get_diag()'''
# B = Matrix([ [1, 2, 3, 4], [0, 1, 2, 3], [-1, 0, 1, 2], [-2, -1, 2, 3]])
# print("Matrix:")
# print(B)

# print("Main diagonal:",B.get_diag(0))
# print("Expected: [1, 1, 1, 3]")
# print()
# print("Diagonal at k = -1:", B.get_diag(-1))
# print("Expected: [0, 0, 2]")
# print()
# print("Diagonal at k = -2:", B.get_diag(-2))
# print("Expected: [-1, -1]")
# print()
# print("Diagonal at k = -3:", B.get_diag(-3))
# print("Expected: [-2]")
# print()
# print("Diagonal at k = 1:", B.get_diag(1))
# print("Expected: [2, 2, 2]")
# print()
# print("Diagonal at k = 2:", B.get_diag(2))
# print("Expected: [3, 3]")
# print()
# print("Diagonal at k = 3:", B.get_diag(3))
# print("Expected: [4]")

'''TESTER CELL FOR
row_space()
col_space()
get_row()
get_col()
set_row()
set_col()'''
# A = Matrix([[1, 2, 3], [4, 5, 6]])
# print("Original Row Space:", A.row_space())
# print("Original Column Space:", A.col_space())
# print("Original Matrix:")
# print(A)
# print()


# A.set_row(1, [10, 20, 30])
# print("Modification #1")
# print("Row Space after modification:", A.row_space())
# print("Column Space after modification:", A.col_space())
# print("Modified Matrix:")
# print(A)
# print()

# A.set_col(2, [20, 50])
# print("Modification #2")
# print("Row Space after modification:", A.row_space())
# print("Column Space after modification:", A.col_space())
# print("Modified Matrix:")
# print(A)
# print()

# A.set_row(2, [40, 50, 6])
# print("Modification #3")
# print("Row Space after modification:", A.row_space())
# print("Column Space after modification:", A.col_space())
# print("Modified Matrix:")
# print(A)
# print()

# A.set_entry(2, 3, 60)
# print("Modification #4")
# print("Row Space after modification:", A.row_space())
# print("Column Space after modification:", A.col_space())
# print("Modified Matrix:")
# print(A)
# print()


# print("The 2nd row is:", A.get_row(2))
# print("The 3rd column is:", A.get_col(3))
# print()


# print("Modification #5")
# A.set_row(2, [40, 50])
# A.set_col(2, [30, 4, 1])
# print(A)

"""-----------------------------------TESTER CELL------------------------------------------------"""
# "TESTING OPERATOR + "

# A = Matrix([[1, 2, 2],[3, 4, 4]])
# B = Matrix([[1, 2],[1, 2]])
# C = Matrix([[10, 20],[30, 40],[50, 60]])

# P = A + B # dimension mismatch
# Q = A + C 

# print("Matrix A")           
# print(A)
# print()

# print("Matrix C")           
# print(C)
# print()

# print("Matrix Q = A + C")           
# print(Q)
# print()

# print(P)

# "TESTING OPERATOR * "-----------------------------------------------

# # TESTING SCALAR-MATRIX MULTIPLICATION
# B = Matrix([[-3, -5], [-9, 1], [8, 0], [9, -4], [3, 10]])
#T = -0.5 * B     
# print("Matrix B")
# print(B)
# print()

# print("Matrix T = -0.5 * B")
# print(10.0*B)
# print()


# # TESTING MATRIX-MATRIX MULTIPLICATION
# U = A * C
# print("Matrix U = A * B")
# A = Matrix([[-9, -8], [-2, -10], [-6, 5], [-9, -3]])
# B = Matrix([[-2, -5, 0, 2, -10], [4, 1, 3, 10, 0]])
# print(A*C)
# print()


# TESTING MATRIX-VECTOR MULTIPLICATION
# x = Vec([0, 1])  # Vec object
# b = A * x   # b is a Vec data type
# print("Vector b = A * x")
# print(b) 