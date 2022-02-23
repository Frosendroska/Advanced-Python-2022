import numpy as np
from Matrix import Matrix
from MatrixMixin import MatrixNumpy
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
            f.write(str(a + b))

        with open("artifacts/easy/matrix*.txt", 'w') as f:
            f.write(str(a * b))

        with open("artifacts/easy/matrix@.txt", 'w') as f:
            f.write(str(a @ b))

    def test_add(self):
        np.random.seed(10)
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
        np.random.seed(20)
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
        np.random.seed(30)
        a = Matrix(np.random.randint(0, 10, (10, 10)))
        b = Matrix(np.random.randint(0, 10, (10, 10)))
        c = np.array(a.val)
        d = np.array(b.val)
        ans1 = a @ b
        ans2 = c @ d
        for r in range(len(a.val)):
            for c in range(len(a.val[r])):
                self.assertEqual(ans1.val[r][c], ans2[r][c])

    def test_medium(self):
        np.random.seed(40)
        a = MatrixNumpy(np.random.randint(0, 10, (10, 10)))
        b = MatrixNumpy(np.random.randint(0, 10, (10, 10)))

        if not os.path.exists("artifacts"):
            os.mkdir("artifacts")

        if not os.path.exists("artifacts/medium"):
            os.mkdir("artifacts/medium")

        with open("artifacts/medium/matrix+.txt", "w") as file:
            file.write(str(a + b))

        with open("artifacts/medium/matrix*.txt", "w") as file:
            file.write(str(a * b))

        with open("artifacts/medium/matrix@.txt", "w") as file:
            file.write(str(a @ b))

    def test_add2(self):
        np.random.seed(50)
        a = MatrixNumpy(np.random.randint(0, 10, (10, 10)))
        b = MatrixNumpy(np.random.randint(0, 10, (10, 10)))
        c = np.array(a.val)
        d = np.array(b.val)
        ans1 = a + b
        ans2 = c + d
        for r in range(len(a.val)):
            for c in range(len(a.val[r])):
                self.assertEqual(ans1.val[r][c], ans2[r][c])

    def test_mul2(self):
        np.random.seed(60)
        a = MatrixNumpy(np.random.randint(0, 10, (10, 10)))
        b = MatrixNumpy(np.random.randint(0, 10, (10, 10)))
        c = np.array(a.val)
        d = np.array(b.val)
        ans1 = a * b
        ans2 = c * d
        for r in range(len(a.val)):
            for c in range(len(a.val[r])):
                self.assertEqual(ans1.val[r][c], ans2[r][c])

    def test_matmul2(self):
        np.random.seed(70)
        a = MatrixNumpy(np.random.randint(0, 10, (10, 10)))
        b = MatrixNumpy(np.random.randint(0, 10, (10, 10)))
        c = np.array(a.val)
        d = np.array(b.val)
        ans1 = a @ b
        ans2 = c @ d
        for r in range(len(a.val)):
            for c in range(len(a.val[r])):
                self.assertEqual(ans1.val[r][c], ans2[r][c])

    def test_collision(self):
        if not os.path.exists("artifacts"):
            os.mkdir("artifacts")

        if not os.path.exists("artifacts/hard"):
            os.mkdir("artifacts/hard")

        Matrix.invalidate_caches()
        i = 0
        np.random.seed(62)
        while True:
            a = Matrix(np.random.randint(0, 5, (2, 2)))
            b = Matrix(np.random.randint(0, 5, (2, 2)))
            c = Matrix(np.random.randint(0, 5, (2, 2)))
            d = b
            ab = a @ b
            Matrix.invalidate_caches()
            cd = c @ d
            Matrix.invalidate_caches()
            if hash(a) == hash(c) and (a != c) and (ab != cd):
                print(f"Collision on {i} iteration!")
                with open("artifacts/hard/A.txt", "w") as f1:
                    f1.write(str(a))
                with open("artifacts/hard/B.txt", "w") as f2:
                    f2.write(str(b))
                with open("artifacts/hard/C.txt", "w") as f3:
                    f3.write(str(c))
                with open("artifacts/hard/D.txt", "w") as f4:
                    f4.write(str(d))
                with open("artifacts/hard/AB.txt", "w") as f5:
                    f5.write(str(ab))
                with open("artifacts/hard/CD.txt", "w") as f6:
                    f6.write(str(cd))

                with open(f"artifacts/hard/hash.txt", "w") as f:
                    f.write(f"Hash AB and hash CD are equal to {hash(ab)}")
                break
            i += 1


if __name__ == "__main__":
    unittest.main()
