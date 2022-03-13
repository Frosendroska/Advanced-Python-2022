import os


def integrate(f, step, interval, log):
    if log:
        print("Integrate range {} in process {}".format(interval, os.getpid()))
    left = interval[0]
    res = 0
    while left < interval[1]:
        res += f(left) * min(interval[1] - left, step)
        left += step
    return res
