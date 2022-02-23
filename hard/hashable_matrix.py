from easy.matrix import Matrix
from functools import cache
from numpy import random


class MatHashMixin:
    def __hash__(self):
        hs = int(0)
        for rc in range(self.r):
            for cc in range(self.c):
                hs += self.mat[rc][cc]
        return int(hs)


class HashableMatrix(Matrix, MatHashMixin):
    __matmul__ = cache(Matrix.__matmul__)
    __hash__ = MatHashMixin.__hash__

    def __eq__(self, other):
        if self.c != other.c or self.r != other.r:
            return False
        for rc in range(self.r):
            for cc in range(self.c):
                if self.mat[rc][cc] != other.mat[rc][cc]:
                    return False
        return True


if __name__ == '__main__':
    def random_mat_gen(left=0, right=4):
        return HashableMatrix(random.randint(left, right, (2, 2)))


    run = True

    while run:
        B = D = random_mat_gen()
        for i in range(20000):
            A = random_mat_gen()
            C = random_mat_gen()
            if (hash(A) == hash(C)) and (hash(B) == hash(C)) and (A @ B != C @ D):
                to_be_written = [
                    ('A', str(A)),
                    ('B', str(B)),
                    ('C', str(C)),
                    ('D', str(D)),
                    ('AB', str(A @ B)),
                    ('CD', str(C @ D)),
                    ('hash', str(hash(A @ B)) + ' ' + str(hash(C @ D))),
                ]
                for filename, content in to_be_written:
                    with open(f'../artifacts/hard/{filename}.txt', 'w') as file:
                        file.write(content)
                        file.write('\n')
                run = False
                break
