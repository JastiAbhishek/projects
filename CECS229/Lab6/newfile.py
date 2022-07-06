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
        c0 = Vec(m.colsp[0])
        largest_i = 0
        largest = 0
        for j in range (p, len(c0.elements)):
            if abs(c0.elements[j]) > largest:
                largest = c0.elements[j]
                largest_i = j
        if largest_i != 0:
            swaprow = m.rowsp[largest_i]
            m.rowsp[largest_i] = m.rowsp[p]
            m.rowsp[p] = swaprow

        m = Matrix(m.rowsp)    
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