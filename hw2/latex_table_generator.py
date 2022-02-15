from itertools import tee
from typing import List
from functools import partial
# from itertools import pairwise
from pymonad.maybe import Just, Nothing, Maybe

MatrixT = List[List[str]]

table_begin = '\\begin{tabular}'
table_end = ' \\end{tabular} '
newline = ' \\\\ '
hline = ' \\hline '
col_separator = ' & '


def create_table(matrix: MatrixT) -> Maybe[str]:
    row_length = len(matrix[0]) if matrix else None

    return Just(matrix) \
        .bind(check_dimension) \
        .map(to_latex_table_content) \
        .map(partial(wrap_in_table, row_length))


def check_dimension(matrix: MatrixT) -> Maybe[MatrixT]:
    row_pairs = list(pairwise(matrix))
    if not matrix or not matrix[0] or list(filter(lambda rs: len(rs[0]) == len(rs[1]), row_pairs)) != row_pairs:
        return Nothing
    return Just(matrix)


def generate_table_begin(row_length: int) -> str:
    return table_begin + '{' + 'l'.join(['|'] * (row_length + 1)) + '}'


def wrap_in_table(row_length: int, latex_matrix: str) -> str:
    return (' ' + latex_matrix + ' ').join([generate_table_begin(row_length), table_end])


def to_latex_table_content(matrix: MatrixT) -> str:
    return hline + (newline + hline) \
        .join(map(lambda str_list: col_separator.join(str_list), matrix)) + newline + hline


# unfortunately it is available only since python 3.10 in itertools and PyMonad isn't available for python 3.10
def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
