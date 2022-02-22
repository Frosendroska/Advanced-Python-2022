import numpy as np
import os


class MatrixException(Exception):
    def __init__(self, ln, lm, rn, rm, message="Matrices does not match"):
        self.ln = ln
        self.lm = lm
        self.rn = rn
        self.rm = rm
        self.message = message
        super().__init__(self.message)


class Matrix:
    def __init__(self, matrix):
        self.val = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])

    def __add__(self, other):
        try:
            if self.n != other.m:
                raise MatrixException(self.n, self.m, other.n, other.m)

            c = Matrix([[0 for _ in range(self.n)] for _ in range(self.m)])
            for i in range(self.n):
                for j in range(self.m):
                    c.val[i][j] = self.val[i][j] + other.val[i][j]
            return c
        except MatrixException as e:
            print(e)
            return None

    def __matmul__(self, other):
        try:
            if self.m != other.m or self.n != other.n:
                raise MatrixException(self.n, self.m, other.n, other.m)

            c = Matrix([[0 for _ in range(self.n)] for _ in range(self.m)])
            for i in range(self.n):
                for j in range(other.m):
                    for k in range(other.m):
                        c.val[i][j] += self.val[i][k] * other.val[k][j]
            return c
        except MatrixException as e:
            print(e)
            return None

    def __mul__(self, other):
        try:
            if self.m != other.m or self.n != other.n:
                raise MatrixException(self.n, self.m, other.n, other.m)

            c = Matrix([[0 for _ in range(self.n)] for _ in range(self.m)])
            for i in range(self.n):
                for j in range(self.m):
                    c.val[i][j] = self.val[i][j] * other.val[i][j]
            return c
        except MatrixException as e:
            print(e)
            return None

    def __str__(self) -> str:
        s = str()
        for r in range(len(self.val)):
            for c in range(len(self.val[r])):
                s += str(self.val[r][c]) + " "
            s += '\n'
        return s
