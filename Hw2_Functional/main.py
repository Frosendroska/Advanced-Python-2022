from GeneratorOfFibAST import main

from datetime import datetime
import os
import sys
import functools

from typing import List


def make_latex_from_array(array: list) -> str:
    return ("\\begin{tabular}{|" +
            functools.reduce(lambda l, _: l + " l |", array[0], "") +
            "}" +
            "\\hline\n" +
            functools.reduce(
                lambda l, r: l + " \\hline\n" + r,
                map(lambda line: functools.reduce(lambda l, r: l + " & " + r, line) + " \\\\", array)
            ) +
            "\n\\hline\n" +
            "\\end{tabular}\n"
            )


def generate_latex_header(title: str, author: str, date: str) -> str:
    return ("\\documentclass{article}\n"
            "\\usepackage[utf8]{inputenc}\n"
            "\\usepackage{graphicx}\n\n"
            f"\\title{{{title}}}\n"
            f"\\author{{{author}}}\n"
            f"\\date{{{date}}}\n"
            "\\begin{document}\n\n"
            "\\maketitle\n\n")


def make_image(img_path, scale) -> str:
    return f"\\includegraphics[scale={scale}]{{{img_path}}}\n"


def generate_latex_footer():
    return "\\end{document}"


in_file_with_table = str(sys.argv[1])

# открываем файл
with open(in_file_with_table, 'r') as sourse:
    # пишем файл в массив
    lines = [line.split() for line in sourse]
    # создаем папку
    if not os.path.exists("artifacts"):
        os.mkdir("artifacts")
    # делаем латех файл
    with open('artifacts/your-table.tex', 'w') as f:
        f.write(generate_latex_header("Here you can see the array in latex", "Braun Kate", str(datetime.now().date())))
        f.write(make_latex_from_array(lines))
        main.main()
        f.write(make_image("artifacts/AstTree.png", 0.22))
        f.write(generate_latex_footer())

        sourse.close()
        f.close()
        if not os.path.exists("artifacts/out"):
            os.mkdir("artifacts/out")
        os.system(
            'pdflatex -file-line-error -interaction=nonstopmode -synctex=1 -output-format=pdf -output-directory=/Users/katya/Desktop/University/Coding/Python/AdvancedPython-2022/Hw2_Functional/artifacts/out artifacts/your-table.tex')
