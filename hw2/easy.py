from latex_table_generator import create_table
from latex_file_generator import create_latex_file
import os

if __name__ == '__main__':
    if not os.path.exists('artifacts/'):
        os.makedirs('artifacts')

    m_matrix = create_table([['adsfsdafdsfdsfdsfdsf', 'bs'], ['c', 'dasdsadsad']])
    if m_matrix.is_nothing():
        exit(-1)

    with open('artifacts/easy.tex', 'w+') as file:
        babel_package = ' \\usepackage[english]{babel} '
        file.write(create_latex_file(babel_package, m_matrix.value))
