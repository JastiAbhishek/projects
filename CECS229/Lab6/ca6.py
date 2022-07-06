import math
import enum

class GaussSolvers(enum.Enum):
    np = 0
    pp = 1
    tp = 2

            
    def solve(A, b, solver = GaussSolvers.np):
        if solver == GaussSolvers.np:
            return solve_np(A, b)
        elif solver == GaussSolvers.pp:
            return solve_pp(A, b)
        elif solver == GaussSolvers.tp:
            return solve_tp(A, b)

def _rref(A, b):
    # build augmented matrix
    lastCol = len(A.col_space()) + 1
    rows = A.row_space()
    for i in rows:
        i.append(0)
    m = Matrix(rows)
    m.set_col(lastCol, b.elements)

    # swap if [0][0] is 0
    if m.colsp[0][0] == 0:
        c0 = Vec(m.colsp[0])
        largest_i = 0
        largest = 0
        for j in range (0, len(c0.elements)):
            if abs(c0.elements[j]) > largest:
                largest = c0.elements[j]
                largest_i = j
        if largest_i != 0:
            swaprow = m.rowsp[largest_i]
            m.rowsp[largest_i] = m.rowsp[0]
            m.rowsp[0] = swaprow

        m = Matrix(m.rowsp)

    # start gaussian elimination
    numRows = len(m.row_space())
    numCols = len(m.col_space())
    iterate = 0
    if numRows < numCols:
        iterate = len(m.row_space()) - 1
    else:
        iterate = len(m.col_space()) - 1
    for p in range(iterate):

        if m.col_space()[p][p] == 0:
            a = m.row_space()[p]
            b = m.row_space()[-1]
            # print(m.get_row(p))
            m.set_row(p + 1, b)
            m.set_row(numRows, a)
            # print(m.get_row(p))
        pivot = m.col_space()[p][p]
        # print("PIVOT:", pivot)
        if pivot != 0:
            for i in range(p + 1, len(m.row_space())):
                first = m.row_space()[i][p]
                for j in range(len(m.row_space()[0])):
                    top = m.row_space()[p][j]
                    curr = m.row_space()[i][j]
                    # print("first:", first, "top:", top, " curr:", curr)
                    m.row_space()[i][j] = curr - ((first / pivot) * top)
        m = Matrix(m.row_space())
    return Matrix(m.row_space())

#rank(A) < rank(Ag) == No solution
#rank(A) = rank(Ag) = number of variables == Unique solution
#rank(A) = rank(Ag) < number of variables == Infinitely many solutions
def solve_np(A,b):
    m = A.rank()
    print(m)
    Ag = _rref(A,b)
    rank = Ag.rank()
    print(rank)
    sol = Vec(m.colsp[len(m.rowsp[0])-1])
    for i  in range(len(sol.elements)-1, -1, -1):
        sol.elements[i] = m.rowsp[i][len(sol.elements)] / m.rowsp[i][i]
        # print(Ag.rowsp[i])
    # a = Vec(Ag.colsp[len(Ag.rowsp[0])-2])
    return None #sol

def _rref_pp(A, b):
    # build augmented matrix
    lastCol = len(A.col_space()) + 1
    rows = A.row_space()
    for i in rows:
        i.append(0)
    m = Matrix(rows)
    m.set_col(lastCol, b.elements)

 # start gaussian elimination
    numRows = len(m.row_space())
    numCols = len(m.col_space())
    iterate = 0
    if numRows < numCols:
        iterate = len(m.row_space()) - 1
    else:
        iterate = len(m.col_space()) - 1
    for p in range(iterate):
        # c0 = Vec(m.colsp[0])
        # largest_i = 0
        # largest = 0
        # for j in range (p, len(c0.elements)):
        #     if abs(c0.elements[j]) > largest:
        #         largest = c0.elements[j]
        #         largest_i = j
        # if largest_i != 0:
        #     swaprow = m.rowsp[largest_i]
        #     m.rowsp[largest_i] = m.rowsp[p]
        #     m.rowsp[p] = swaprow

        m = Matrix(m.rowsp)    
        if m.col_space()[p][p] == 0:
            a = m.row_space()[p]
            b = m.row_space()[-1]
            m.set_row(p + 1, b)
            m.set_row(numRows, a)
        pivot = m.col_space()[p][p]
        if pivot != 0:
            for i in range(p + 1, len(m.row_space())):
                first = m.row_space()[i][p]
                for j in range(len(m.row_space()[0])):
                    top = m.row_space()[p][j]
                    curr = m.row_space()[i][j]
                    m.row_space()[i][j] = curr - ((first / pivot) * top)
        m = Matrix(m.row_space())
    return Matrix(m.row_space())

    def solve_pp(A, b):
        pass

def _rref_tp(A, b):
    # build augmented matrix
    lastCol = len(A.col_space()) + 1
    rows = A.row_space()
    for i in rows:
        i.append(0)
    m = Matrix(rows)
    m.set_col(lastCol, b.elements)

 # start gaussian elimination
    numRows = len(m.row_space())
    numCols = len(m.col_space())
    iterate = 0
    if numRows < numCols:
        iterate = len(m.row_space()) - 1
    else:
        iterate = len(m.col_space()) - 1
    for p in range(iterate):
        # c0 = Vec(m.colsp[0])
        # largest_i = 0
        # largest = 0
        # for j in range (p, len(c0.elements)):
        #     if abs(c0.elements[j]) > largest:
        #         largest = c0.elements[j]
        #         largest_i = j
        # if largest_i != 0:
        #     swaprow = m.rowsp[largest_i]
        #     m.rowsp[largest_i] = m.rowsp[p]
        #     m.rowsp[p] = swaprow

        m = Matrix(m.rowsp)    
        if m.col_space()[p][p] == 0:
            a = m.row_space()[p]
            b = m.row_space()[-1]
            m.set_row(p + 1, b)
            m.set_row(numRows, a)
        pivot = m.col_space()[p][p]
        if pivot != 0:
            for i in range(p + 1, len(m.row_space())):
                first = m.row_space()[i][p]
                for j in range(len(m.row_space()[0])):
                    top = m.row_space()[p][j]
                    curr = m.row_space()[i][j]
                    m.row_space()[i][j] = curr - ((first / pivot) * top)
        m = Matrix(m.row_space())
    return Matrix(m.row_space())

    def solve_tp(A, b):
        pass
            

def is_independent(S):
    # linearly independent vectors iff the rank is equal to the number of vectors
    # create a Matrix
    vec_list = list(S)
    Ag = []
    for i in range(len(vec_list)):
        temp_list = []
        temp_list.append(vec_list[i])
        Ag.append(temp_list)

    # rref
    for i in range(len(Matrix(Ag).colsp[0]) - 1):
        if Matrix(Ag).colsp[i][i] != 0:
            for j in range(len(Matrix(Ag).colsp[0]) - 1 - i):
                r0 = Matrix(Ag).rowsp[i]
                pivot = -(Matrix(Ag).colsp[i][1 + i +
                                              j]) / Matrix(Ag).colsp[i][i]
                r = Vec(Ag.rowsp[i + 1 + j])
                r = r0 * pivot + r
                Ag.set_row(2 + i + j, r.elements)

    # find rowsp / basis

    # if dimension of the basis of the set equals the dimension of the set, the set is linearly independent

    return Matrix(Ag)


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
            n += abs(self.elements[i])**p
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
 
    def __str__(self):
        s = ""
        for i in range(len(self.rowsp)):
            for j in range(len(self.rowsp[0])):
                if j==0:
                    s += "["+str(self.rowsp[i][j])+", "
                elif j==len(self.rowsp[0])-1:
                    s += str(self.rowsp[i][j])+"]"
                else:
                    s += str(self.rowsp[i][j])+", "
            s+="\n"
        return s 

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

    def rank(self):
        rank = 0
        z = 0
        k = []
        for i in range(len(self.colsp[0])):
            k.append(0)
        b = Vec(k)

        m = Matrix(self.rowsp)
        for i in range(len(b.elements)):
            m.rowsp[i].append(b.elements[i])

        # swap if [0][0] is 0
        if m.colsp[0][0] == 0:
            c0 = Vec(m.colsp[0])
            largest_i = 0
            largest = 0
            for j in range (0, len(c0.elements)):
                if abs(c0.elements[j]) > largest:
                    largest = c0.elements[j]
                    largest_i = j
            if largest_i != 0:
                swaprow = m.rowsp[largest_i]
                m.rowsp[largest_i] = m.rowsp[0]
                m.rowsp[0] = swaprow

            m = Matrix(m.rowsp)

        # start gaussian elimination
        numRows = len(m.row_space())
        numCols = len(m.col_space())
        iterate = 0
        if numRows < numCols:
            iterate = len(m.row_space()) - 1
        else:
            iterate = len(m.col_space()) - 1
        for p in range(iterate):
            if m.col_space()[p][p] == 0:
                a = m.row_space()[p]
                b = m.row_space()[-1]
                # print(m.get_row(p))
                m.set_row(p + 1, b)
                m.set_row(numRows, a)
                # print(m.get_row(p))
            pivot = m.col_space()[p][p]
            # print("PIVOT:", pivot)
            if pivot != 0:
                for i in range(p + 1, len(m.row_space())):
                    first = m.row_space()[i][p]
                    for j in range(len(m.row_space()[0])):
                        top = m.row_space()[p][j]
                        curr = m.row_space()[i][j]
                        # print("first:", first, "top:", top, " curr:", curr)
                        m.row_space()[i][j] = curr - ((first / pivot) * top)
            m = Matrix(m.row_space())
        
        for i in range(len(m.rowsp)):
            for j in range(len(m.rowsp[0])):
                if i == j:
                    if m.rowsp[i][j] == 0:
                        for k in range(len(m.rowsp[0])):
                            if m.rowsp[i][k] == 0:
                                z += 1
                    else:
                        rank += 1
                    if z == len(m.rowsp[0]):
                        rank -= 1
                        z = 0
        return rank

A = Matrix([[1, 2, -1, 1],[-1, 1, 2, -1],[2, -1, 2, 2], [1, 1, -1, 2]])
x = Vec([6, 3, 14, 8])
# print(A)
# v = Vec( [9.975, -8.443, -9.417, 5.956, 9.176, 5.704, 3.638])
## Answer = [1, 2, 3, 4]
# A = Matrix([[1, 2],[3, 4],[5, 6]])
# x = Vec([0, 1, 5])

# '''6x7 Matrix'''
# A = Matrix(
# [[5, 6, 15, -18, -10, 19, -5],
# [-2, 8, 20, -18, 18, 7, 5],
# [-18, 10, 4, -17, -15, 15, -20],
# [-1, -6, 2, -15, -18, -16, 15],
# [15, 10, 1, -3, -13, -3, -11],
# [-14, -1, 13, 8, 14, -17, -16]])

'''6x6 Matrix'''
# A = Matrix(
# [[5, 6, 15, -18, -10, 19],
# [-2, 8, 20, -18, 18, 7],
# [-18, 10, 4, -17, -15, 15],
# [-1, -6, 2, -15, -18, -16],
# [15, 10, 1, -3, -13, -3],
# [-14, -1, 13, 8, 14, -17]])

'''7x6 Matrix'''
# A = Matrix(
# [[5, 6, 15, -18, -10, 19],
# [-2, 8, 20, -18, 18, 7],
# [-18, 10, 4, -17, -15, 15],
# [-1, -6, 2, -15, -18, -16],
# [15, 10, 1, -3, -13, -3],
# [-14, -1, 13, 8, 14, -17]
# [10, 20, 30, 40, 50, 60]])


# b = Vec([-27, 151, -55, 381, -179, -32])
# print(_rref(A, x))
print(_rref_pp(A, x))
print(_rref_tp(A, x))
# print(A.rank())
# print(solve_np(A,b))
# print(v.norm(9))

"""RANK TESTER CELL"""
# A = Matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# print(A)
# print("Rank:", A.rank(), "\nExpected: 2\n")

# B = Matrix([[1, 2], [-1, -2]])
# print(B)
# print("Rank:", B.rank(), "\nExpected: 1\n")

# C = Matrix([[0, -1, 5], [2, 4, -6], [1, 1, 5]])
# print(C)
# print("Rank:", C.rank(), "\nExpected: 3\n")

# D = Matrix([[5, 3, 0], [1, 2, -4], [-2, -4, 8]])
# print(D)
# print("Rank:", D.rank(), "\nExpected: 2\n")

# E = Matrix([[1, 2, -1, 3], [2, 4, 1, -2], [3, 6, 3, -7]])
# print(E)
# print("Rank:", E.rank(), "\nExpected: 2\n")

# A = Matrix([[-13 , -1,  14,  -9, -20], [-15,   1,  -5,   0,  17], [ 14,  10,  -6,  13,  -3], [ 14,  -9,   9,   4 ,  1], [-14 ,-15 ,-11,   2,   1]])
# print(A)
# print("Rank:", A.rank(), "\nExpected: 5\n")


# A =Matrix([
# [0, -12, 13, 1],
# [-18, 7, -13, 13],
# [19, -6, 4, -1],
# [10, 14, -5, -16]])

# b =Vec( [7, 79, -134, -46])

# print(_rref(A,b))

"""TESTER CELL #1 FOR GENP"""
# A = Matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# b = Vec([9, 10, 11])
# sol = solve_np(A, b)
# print("Result:", sol)
# print("Expected: 1")

# """TESTER CELL #2 FOR GENP"""
# A = Matrix([[1, 0, 5], [0, 1, 2], [3, 2, 0]])
# b = Vec([6, 3, 5])
# sol = solve_np(A, b)
# print("Returned:", sol)
# print("Expected: [1.0, 1.0, 1.0]")

# """TESTER CELL #3 FOR GENP"""
# A = Matrix([[1, 1, 5], [2, 2, 10]])
# b = Vec([6, 3])
# sol = solve_np(A, b)
# print("Returned:", sol)
# print("Expected: None")