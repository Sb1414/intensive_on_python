from itertools import tee
from random import choices
from time import monotonic
from multiply import mul as cython_mul


def mul_python(a, b):
    b_iter = tee(zip(*b), len(a))
    return [
        [
            sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
            for col_b in b_iter[i]
        ] for i, row_a in enumerate(a)
    ]


def create_random_matrix(rows, columns):
    return [choices(range(1, 100), k=columns) for _ in range(rows)]


def test(matrix_size):
    print(f'Test Matrix[{matrix_size},{matrix_size}]')
    first = create_random_matrix(matrix_size, matrix_size)
    second = create_random_matrix(matrix_size, matrix_size)

    start = monotonic()
    mul_python(first, second)
    finish = monotonic()
    print(f'Python function: {finish - start:.5f} seconds')

    start = monotonic()
    cython_mul(first, second)
    finish = monotonic()
    print(f'Cython function: {finish - start:.5f} seconds')


if __name__ == '__main__':
    matrix_sizes = [30, 50, 100, 200, 300]
    for size in matrix_sizes:
        test(size)
