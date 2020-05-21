

def zeros_matrix(noRows, noCols):
    t = []

    for _ in range(noRows):
        t.append([0 for _ in range(noCols)])

    return t

def dif(A, B):
    C = zeros_matrix(len(A), len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] - B[i][j]
    return C

def transpose(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]


def multiply(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        return None

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            for k in range(rowsB):
                C[i][j] += A[i][k] * B[k][j]

    '''C = [[sum(a * b for a, b in zip(A_row, B_col))
          for B_col in zip(*B)]
         for A_row in A]'''

    return C


def det(X):
    n = len(X)
    AM = copy_matrix(X)

    for fd in range(n):
        for i in range(fd + 1, n):
            if AM[fd][fd] == 0:
                AM[fd][fd] = 1.0e-18  # aprox 0
            crScaler = AM[i][fd] / AM[fd][fd]
            for j in range(n):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]

    determinant = 1.0
    for i in range(n):
        determinant *= AM[i][i]

    return determinant


def add(A, B):
    C = []
    for index in range(0, len(A)):
        C.append(A[index] + B[index])
    return A


def inverse(X):
    if det(X) != 0:
        n = len(X)
        AM = copy_matrix(X)
        I = zeros_matrix(n, n)
        for i in range(0, n):
            I[i][i] = 1.0
        IM = copy_matrix(I)

        indices = list(range(n))
        for fd in range(n):
            fdScaler = 1.0 / AM[fd][fd]
            for j in range(n):
                AM[fd][j] *= fdScaler
                IM[fd][j] *= fdScaler
            for i in indices[0:fd] + indices[fd + 1:]:
                crScaler = AM[i][fd]
                for j in range(n):
                    AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                    IM[i][j] = IM[i][j] - crScaler * IM[fd][j]

        return IM


def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]

    return MC
