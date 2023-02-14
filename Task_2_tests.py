import Task_2


def check(test_number: int):
    with open(f"./tests/{test_number}.txt", "r") as inp:
        for _ in range(50):
            data = inp.readline()
            x, y = map(int, data.split())
            result = Task_2.solution(data)
            assert result == x * y


def test1():
    check(1)

def test2():
    check(2)

def test3():
    check(3)