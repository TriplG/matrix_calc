from django.test import TestCase
import numpy as np

N, M = 3, 3


class TestObj:
    def test(self):
        global N, M
        N += 1
        M += 1
        print(N, M)


def test_func():
    global N, M
    print(N, M)

# print(N, M)
# a = TestObj()
# a.test()
# test_func()

arr_result = []
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [1, 2, 3, 4, 5, 6]
a = iter(arr1)
for i in range(N):
    arr = []
    for j in range(M):
        arr.append(next(a))
    arr_result.append(arr)

# print(arr_result)
def dict_test(dct):
    dct['tree'] = 4
    return dct
# print(dict_test({'one': 1, 'two': 2, 'tree': 3}))


def test1():
    if [1, 2, 3]:
        return True
    else:
        return False
# print(test1())

a, b = None, None
print(a, b)


