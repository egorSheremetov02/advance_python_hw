from ast_drawer_ses.ast_improved import draw_ast
from ast_drawer_ses.fib import fib
from latex_table_generator import create_table
from latex_file_generator import create_latex_file
from latex_image_generator import create_latex_image
import os
import subprocess

if __name__ == '__main__':
    if not os.path.exists('artifacts/middle_img.png'):
        draw_ast(fib)

    m_matrix = create_table([['adsfsdafdsfdsfdsfdsf', 'bs'], ['c', 'dasdsadsad']])
    if m_matrix.is_nothing():
        exit(-1)

    with open('artifacts/middle.tex', 'w+') as file:
        babel_package = ' \\usepackage[english]{babel} '
        graphicx_package = ' \\usepackage{graphicx} '
        graphics_path = ' \\graphicspath{ {./artifacts/} } '
        file.write(
            create_latex_file(header=graphicx_package + babel_package + graphics_path,
                              document_content=m_matrix.value + create_latex_image('middle_img.png')))

    cmd = ['pdflatex', '-interaction', 'nonstopmode', 'artifacts/middle.tex']
    proc = subprocess.Popen(cmd)
    proc.communicate()

    retcode = proc.returncode
    if not retcode == 0:
        os.unlink('artifacts/middle.tex')
        raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd)))

    os.unlink('artifacts/middle.tex')
    os.unlink('middle.log')


