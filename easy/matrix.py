from numpy import random


def gen_matrix(rows: int, cols: int):
    return [[0 for _ in range(cols)] for _ in range(rows)]


class Matrix:
    def __init__(self, array2d):
        if not len(array2d):
            raise Exception("Expected nonempty matrix")

        if not len(array2d[0]):
            raise Exception("Expected nonempty matrix")

        expected_methods = ['__mul__', '__add__']

        for i in range(len(array2d) - 1):
            if len(array2d[i]) != len(array2d[i + 1]):
                raise Exception("Matrix rows are expected to have same number of elements")

        def can_be_matrix_element(el):
            return all(hasattr(el, method) for method in expected_methods)

        all_elements_ok = all([all([can_be_matrix_element(el) for el in l]) for l in array2d])

        if not all_elements_ok:
            raise TypeError("Expected elements of matrix that have '+', '*' operators")

        self.mat = array2d
        self.r = len(array2d)
        self.c = len(array2d[0])

    def __add__(self, other):
        if self.c != other.c or self.r != other.r:
            raise Exception("can't add matrices with different dimensions")

        nmat = gen_matrix(self.r, self.c)

        for i in range(self.r):
            for j in range(self.c):
                nmat[i][j] = self.mat[i][j] + other.mat[i][j]

        return Matrix(nmat)

    def __mul__(self, other):
        if self.c != other.r:
            raise Exception(f"can't multiply matrices A that has {self.c} columns and B that has {other.r} rows")

        nmat = gen_matrix(other.c, self.r)

        for i in range(other.c):
            for j in range(self.r):
                for k in range(self.c):
                    # for cache efficiency it would be better to transpose second matrix first,
                    # but I will go with the simplest possible approach
                    nmat[i][j] += self.mat[i][k] * other.mat[k][j]

        return Matrix(nmat)

    def __matmul__(self, other):
        if self.c != other.c or self.r != other.r:
            raise Exception("can't add matrices with different dimensions")

        nmat = gen_matrix(self.r, self.c)

        for i in range(self.r):
            for j in range(self.c):
                nmat[i][j] = self.mat[i][j] * other.mat[i][j]

        return Matrix(nmat)

    def __str__(self):
        return '\n'.join([' '.join([str(el) for el in row]) for row in self.mat])


if __name__ == '__main__':
    a = Matrix(random.randint(0, 10, (10, 10)))
    b = Matrix(random.randint(0, 10, (10, 10)))
    op_map = {
        '+': lambda m1, m2: m1 + m2,
        '*': lambda m1, m2: m1 * m2,
        '@': lambda m1, m2: m1 @ m2,
    }
    for op in ['+', '*', '@']:
        fun = op_map[op]
        with open(f'../artifacts/easy/matrix{op}.txt', 'w') as file:
            file.write("Matrix a:\n")
            file.write(str(a) + '\n')
            file.write("Matrix b:\n")
            file.write(str(b) + '\n')
            file.write(f"Matrix a {op} b:\n")
            file.write(str(fun(a, b)))
