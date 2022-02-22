import numpy as np
from Matrix import Matrix
import unittest
import os


class TestMatrix(unittest.TestCase):
    def test_easy(self):
        np.random.seed(0)
        a = Matrix(np.random.randint(0, 10, (10, 10)))
        b = Matrix(np.random.randint(0, 10, (10, 10)))

        if not os.path.exists("artifacts"):
            os.mkdir("artifacts")

        if not os.path.exists("artifacts/easy"):
            os.mkdir("artifacts/easy")

        with open("artifacts/easy/matrix+.txt", 'w') as f:
            f.write((a + b).__str__())

        with open("artifacts/easy/matrix1.txt", 'w') as f:
            f.write((a * b).__str__())

        with open("artifacts/easy/matrix@.txt", 'w') as f:
            f.write((a @ b).__str__())

    def test_add(self):
        np.random.seed(0)
        a = Matrix(np.random.randint(0, 10, (10, 10)))
        b = Matrix(np.random.randint(0, 10, (10, 10)))
        c = np.array(a.val)
        d = np.array(b.val)
        ans1 = a + b
        ans2 = c + d
        for r in range(len(a.val)):
            for c in range(len(a.val[r])):
                self.assertEqual(ans1.val[r][c], ans2[r][c])

    def test_mul(self):
        np.random.seed(0)
        a = Matrix(np.random.randint(0, 10, (10, 10)))
        b = Matrix(np.random.randint(0, 10, (10, 10)))
        c = np.array(a.val)
        d = np.array(b.val)
        ans1 = a * b
        ans2 = c * d
        for r in range(len(a.val)):
            for c in range(len(a.val[r])):
                self.assertEqual(ans1.val[r][c], ans2[r][c])

    def test_matmul(self):
        np.random.seed(0)
        a = Matrix(np.random.randint(0, 10, (10, 10)))
        b = Matrix(np.random.randint(0, 10, (10, 10)))
        c = np.array(a.val)
        d = np.array(b.val)
        ans1 = a @ b
        ans2 = c @ d
        for r in range(len(a.val)):
            for c in range(len(a.val[r])):
                self.assertEqual(ans1.val[r][c], ans2[r][c])


if __name__ == "__main__":
    unittest.main()
