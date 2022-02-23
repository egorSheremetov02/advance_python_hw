import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


class WriteToFileMixin:
    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(self.__str__())


class MatrixToStrMixin:
    def __str__(self):
        return self.matrix.__str__()


class GetMatrixMixin:
    def get_matrix(self):
        return self.matrix


class SetMatrixMixin:
    def set_matrix(self, m):
        self.matrix = np.matrix(m)


class Matrix(NDArrayOperatorsMixin, WriteToFileMixin, MatrixToStrMixin, GetMatrixMixin, SetMatrixMixin):
    def __init__(self, matrix):
        # in case of incorrect lengths numpy instantly says that it is deprecated and raises exception
        self.matrix = np.matrix(matrix)

    def __array_ufunc__(self, ufunc, method, *args, **kwargs):
        out = kwargs.get('out', ())
        for x in args + out:
            if not isinstance(x, Matrix):
                return NotImplemented
        args = tuple(x.matrix for x in args)
        if out:
            kwargs['out'] = tuple(x.matrix for x in out)
        return type(self)(getattr(ufunc, method)(*args, **kwargs))



