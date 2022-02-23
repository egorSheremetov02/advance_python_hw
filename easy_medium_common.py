from numpy import random

import medium.matrix
import easy.matrix

if __name__ == '__main__':
    parts = [
        ('medium', medium.matrix.Matrix),
        ('easy', easy.matrix.Matrix)
    ]

    np_a = random.randint(0, 10, (10, 10))
    np_b = random.randint(0, 10, (10, 10))

    for level, Matrix in parts:
        a = Matrix(np_a)
        b = Matrix(np_b)
        op_map = {
            '+': lambda m1, m2: m1 + m2,
            '*': lambda m1, m2: m1 * m2,
            '@': lambda m1, m2: m1 @ m2,
        }
        for op in ['+', '*', '@']:
            fun = op_map[op]
            with open(f'./artifacts/{level}/matrix{op}.txt', 'w') as file:
                file.write("Matrix a:\n")
                file.write(str(a) + '\n')
                file.write("Matrix b:\n")
                file.write(str(b) + '\n')
                file.write(f"Matrix a {op} b:\n")
                file.write(str(fun(a, b)))
