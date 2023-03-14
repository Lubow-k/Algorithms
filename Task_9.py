from typing import List, Tuple
import time
import functools


def function_time(func, time_results):
    def inner(*args):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter() - start
        with open(time_results, "a") as f:
            f.write(str(end) + '\n')
        return result
    return inner


@functools.partial(function_time, time_results='tests/time_mult_1.txt')
def mult_matrix_1(m_a: List[List[int]], m_b: List[List[int]]) -> List[List[int]]:
    assert len(m_a) == len(m_a[0]) == len(m_b) == len(m_b[0])
    n = len(m_a)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += m_a[i][k] * m_b[k][j]
    return res


def add_matrix(m_1: List[List[int]], m_2: List[List[int]], start_i: int, start_j: int, res: List[List[int]]) -> None:
    assert len(m_1) == len(m_2), len(m_1[0]) == len(m_2[0])
    for i in range(len(m_1)):
        for j in range(len(m_1[0])):
            res[start_i + i][start_j + j] = m_1[i][j] + m_2[i][j]


def mult(m_x: List[List[int]], m_y: List[List[int]], top_a: Tuple[int, int], bottom_a: Tuple[int, int], top_b: Tuple[int, int], bottom_b: Tuple[int, int]) -> List[List[int]]:
    assert bottom_a[1] - top_a[1] == bottom_b[0] - top_b[0]
    m = bottom_a[0] - top_a[0]
    n = bottom_b[1] - top_b[1]
    result = [[0] * n for _ in range(m)]

    if bottom_a[0] - top_a[0] == 1 or bottom_a[1] - top_a[1] == 1 or bottom_b[0] - top_b[0] == 1 or bottom_b[1] - top_b[1] == 1:
        s = bottom_a[1] - top_a[1]
        for i in range(m):
            for j in range(n):
                for k in range(s):
                    result[i][j] += m_x[top_a[0] + i][top_a[1] + k] * m_y[top_b[0] + k][top_b[1] + j]
    else:
        middle_a = (top_a[0] + (bottom_a[0] - top_a[0]) // 2, top_a[1] + (bottom_a[1] - top_a[1]) // 2)
        middle_b = (top_b[0] + (bottom_b[0] - top_b[0]) // 2, top_b[1] + (bottom_b[1] - top_b[1]) // 2)

        a = [top_a, middle_a]
        b = [(top_a[0], middle_a[1]), (middle_a[0], bottom_a[1])]
        c = [(middle_a[0], top_a[1]), (bottom_a[0], middle_a[1])]
        d = [middle_a, bottom_a]

        e = [top_b, middle_b]
        f = [(top_b[0], middle_b[1]), (middle_b[0], bottom_b[1])]
        g = [(middle_b[0], top_b[1]), (bottom_b[0], middle_b[1])]
        h = [middle_b, bottom_b]

        a_e = mult(m_x, m_y, *a, *e)
        a_f = mult(m_x, m_y, *a, *f)
        c_e = mult(m_x, m_y, *c, *e)
        c_f = mult(m_x, m_y, *c, *f)
        b_g = mult(m_x, m_y, *b, *g)
        b_h = mult(m_x, m_y, *b, *h)
        d_g = mult(m_x, m_y, *d, *g)
        d_h = mult(m_x, m_y, *d, *h)

        add_matrix(a_e, b_g, 0, 0, result)
        add_matrix(a_f, b_h, 0, len(a_e[0]), result)
        add_matrix(c_e, d_g, len(a_e), 0, result)
        add_matrix(c_f, d_h, len(a_e), len(a_e[0]), result)

    return result


@functools.partial(function_time, time_results='tests/time_mult_2.txt')
def mult_matrix_2(m_a: List[List[int]], m_b: List[List[int]]) -> List[List[int]]:
    assert len(m_a) == len(m_a[0]) == len(m_b) == len(m_b[0])
    n = len(m_a)
    return mult(m_a, m_b, (0, 0), (n, n), (0, 0), (n, n))


def add(matrix: List[List[int]], top_a: Tuple[int, int], bottom_a: Tuple[int, int], top_b: Tuple[int, int], bottom_b: Tuple[int, int]) -> Tuple[List[List[int]], List[Tuple[int, int]]]:
    assert bottom_a[0] - top_a[0] == bottom_b[0] - top_b[0], bottom_a[1] - top_a[1] == bottom_b[1] - top_b[1]
    n = bottom_a[0] - top_a[0]
    m = bottom_a[1] - top_a[1]
    res = [[0]*m for i in range(n)]

    for i in range(n):
        for j in range(m):
            res[i][j] = matrix[top_a[0] + i][top_a[1] + j] + matrix[top_b[0] + i][top_b[1] + j]
    return res, [(0, 0), (n, m)]


def sub(matrix: List[List[int]], top_a: Tuple[int, int], bottom_a: Tuple[int, int], top_b: Tuple[int, int], bottom_b: Tuple[int, int]) -> Tuple[List[List[int]], List[Tuple[int, int]]]:
    assert bottom_a[0] - top_a[0] == bottom_b[0] - top_b[0], bottom_a[1] - top_a[1] == bottom_b[1] - top_b[1]
    n = bottom_a[0] - top_a[0]
    m = bottom_a[1] - top_a[1]
    res = [[0]*m for i in range(n)]

    for i in range(n):
        for j in range(m):
            res[i][j] = matrix[top_a[0] + i][top_a[1] + j] - matrix[top_b[0] + i][top_b[1] + j]
    return res, [(0, 0), (n, m)]


def merge_matrix(matrix: List[List[int]], start_i: int, start_j: int, res: List[List[int]]) -> None:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res[start_i + i][start_j + j] = matrix[i][j]


def add_m(*args: List[List[int]]) -> List[List[int]]:
    m_1 = args[0]
    res = [[0] * len(m_1[0]) for _ in range(len(m_1))]
    for i in range(len(m_1)):
        for j in range(len(m_1[0])):
            r = 0
            for matrix in args:
                assert len(m_1) == len(matrix), len(m_1[0]) == len(matrix[0])
                r += matrix[i][j]
            res[i][j] = r
    return res


def sub_m(m_1: List[List[int]], m_2: List[List[int]]) -> List[List[int]]:
    assert len(m_1) == len(m_2), len(m_1[0]) == len(m_2[0])
    res = [[0] * len(m_1[0]) for _ in range(len(m_1))]
    for i in range(len(m_1)):
        for j in range(len(m_1[0])):
            res[i][j] = m_1[i][j] - m_2[i][j]
    return res


def strassen(m_x: List[List[int]], m_y: List[List[int]], top_a: Tuple[int, int], bottom_a: Tuple[int, int], top_b: Tuple[int, int], bottom_b: Tuple[int, int]) -> Tuple[List[List[int]], List[Tuple[int, int]]]:
    assert bottom_a[1] - top_a[1] == bottom_b[0] - top_b[0]
    n = bottom_a[0] - top_a[0]
    m = bottom_b[1] - top_b[1]
    result = [[0] * m for _ in range(n)]

    if bottom_a[0] - top_a[0] == 1 or bottom_a[1] - top_a[1] == 1 or bottom_b[0] - top_b[0] == 1 or bottom_b[1] - top_b[1] == 1:
        s = bottom_a[1] - top_a[1]
        for i in range(n):
            for j in range(m):
                for k in range(s):
                    result[i][j] += m_x[top_a[0] + i][top_a[1] + k] * m_y[top_b[0] + k][top_b[1] + j]
    else:
        middle_a = (top_a[0] + (bottom_a[0] - top_a[0]) // 2, top_a[1] + (bottom_a[1] - top_a[1]) // 2)
        middle_b = (top_b[0] + (bottom_b[0] - top_b[0]) // 2, top_b[1] + (bottom_b[1] - top_b[1]) // 2)

        a = [top_a, middle_a]
        b = [(top_a[0], middle_a[1]), (middle_a[0], bottom_a[1])]
        c = [(middle_a[0], top_a[1]), (bottom_a[0], middle_a[1])]
        d = [middle_a, bottom_a]

        e = [top_b, middle_b]
        f = [(top_b[0], middle_b[1]), (middle_b[0], bottom_b[1])]
        g = [(middle_b[0], top_b[1]), (bottom_b[0], middle_b[1])]
        h = [middle_b, bottom_b]

        f_h = sub(m_y, *f, *h)
        a_b = add(m_x, *a, *b)
        c_d = add(m_x, *c, *d)
        g_e = sub(m_y, *g, *e)
        a_d = add(m_x, *a, *d)
        e_h = add(m_y, *e, *h)
        b_d = sub(m_x, *b, *d)
        g_h = add(m_y, *g, *h)
        a_c = sub(m_x, *a, *c)
        e_f = add(m_y, *e, *f)

        p1 = strassen(m_x, f_h[0], *a, *f_h[1])[0]
        p2 = strassen(a_b[0], m_y, *a_b[1], *h)[0]
        p3 = strassen(c_d[0], m_y, *c_d[1], *e)[0]
        p4 = strassen(m_x, g_e[0], *d, *g_e[1])[0]
        p5 = strassen(a_d[0], e_h[0], *a_d[1], *e_h[1])[0]
        p6 = strassen(b_d[0], g_h[0], *b_d[1], *g_h[1])[0]
        p7 = strassen(a_c[0], e_f[0], *a_c[1], *e_f[1])[0]

        q1 = sub_m(add_m(p5, p4, p6), p2)
        q2 = add_m(p1, p2)
        q3 = add_m(p3, p4)
        q4 = sub_m(sub_m(add_m(p1, p5), p3), p7)

        merge_matrix(q1, 0, 0, result)
        merge_matrix(q2, 0, len(q1[0]), result)
        merge_matrix(q3, len(q1), 0, result)
        merge_matrix(q4, len(q1), len(q1[0]), result)

    return result, [(0, 0), (n, m)]


@functools.partial(function_time, time_results='tests/time_mult_3.txt')
def mult_matrix_3(m_a: List[List[int]], m_b: List[List[int]]) -> List[List[int]]:
    assert len(m_a) == len(m_a[0]) == len(m_b) == len(m_b[0])
    n = len(m_a)
    return strassen(m_a, m_b, (0, 0), (n, n), (0, 0), (n, n))[0]
