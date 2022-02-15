from typing import List

document_class = ' \\documentclass{article} '
document_begin = ' \\begin{document} '
document_end = ' \\end{document} '


def create_latex_file(header: str, document_content: str) -> str:
    return document_class + header + document_begin + document_content + document_end
