from Task_9 import mult_matrix_1, mult_matrix_2, mult_matrix_3
from typing import List, Tuple
from os import remove
import numpy as np


NEED_CHECK = False
REPEAT = 100


def create_clean_file(num: int) -> None:
    f = open(f'tests/time_mult_{num}.txt', 'w')
    f.close()


def remove_file(num: int) -> None:
    name = f'tests/time_mult_{num}.txt'
    remove(name)


def checker(m_1: List[List[int]], m_2: List[List[int]], res: List[List[int]]) -> bool:
    array_1 = np.asarray(m_1)
    array_2 = np.asarray(m_2)
    res = np.asarray(res)
    result = np.dot(a, b)
    return np.array_equal(res, result)


def format_table(benchmarks: List[str], algos: List[str], results: Tuple[List[float], List[float], List[float]]) -> None:
    array = [str(elem) for part in results for elem in part]
    rows = len(max(*benchmarks, "Benchmark", key=len)) + 1
    cols = len(max(*algos, *array, key=len)) + 1
    print("| {0:<{4}}| {1:<{5}}| {2:<{5}}| {3:<{5}}|".format('Benchmark', *algos, rows, cols), "|" + "-" * (rows + (cols + 1) * 3 + 4) + "|", sep='\n')
    for i in range(len(benchmarks)):
        print("| {0:<{4}}| {1:<{5}}| {2:<{5}}| {3:<{5}}|".format(benchmarks[i], *results[i], rows, cols))


def calculations() -> Tuple[List[float], List[float], List[float]]:
    sample_mean = []
    standard_deviation = []
    geometric_mean = []

    for i in range(3):
        s = 0
        m = 1
        with open(f'tests/time_mult_{i+1}.txt', 'r') as f:
            for j in range(REPEAT):
                value = float(f.readline())
                s += value
                m *= value
        sample_m = s / REPEAT
        sample_mean.append(float('{:.5f}'.format(sample_m)))
        geometric_mean.append(float('{:.5f}'.format(m**(1/REPEAT))))

        s = 0
        with open(f'tests/time_mult_{i + 1}.txt', 'r') as f:
            for j in range(REPEAT):
                value = (float(f.readline()) - sample_m)**2
                s += value
        m = s / (REPEAT - 1)
        standard_deviation.append(float('{:.5f}'.format(m**0.5)))

    return sample_mean, standard_deviation, geometric_mean


for i in range(3):
    create_clean_file(i+1)


print("It's a tester for three matrix multiplication algorithms")
m_size = int(input("Enter the size of test data: "))

a = [[i] * m_size for i in range(m_size)]
b = [[i] * m_size for i in range(m_size)]


if NEED_CHECK:
    if checker(a, b, mult_matrix_1(a, b)) and checker(a, b, mult_matrix_2(a, b)) and checker(a, b, mult_matrix_3(a, b)):
        for i in range(3):
            create_clean_file(i + 1)
        print("All algorithms are correct. Start testing...")
    else:
        print("Something went wrong!")
else:
    print("Start testing...")
print()


for _ in range(REPEAT):
    mult_matrix_1(a, b)
    mult_matrix_2(a, b)
    mult_matrix_3(a, b)


format_table(["sample mean", "standard deviation", "geometric mean"],
["naive mult matrix", "quick mult matrix", "Strassen mult matrix"], calculations())


for i in range(3):
    remove_file(i+1)


