import Task_2


def check(test_number: int):
    with open(f"./tests/{test_number}.in", "r") as inp:
        with open(f"./tests/{test_number}.out", "r") as out:
            for _ in range(50):
                data = inp.readline()
                expected = int(out.readline())

                result = Task_2.solution(data)
                assert result == expected


def test1():
    check(1)


def test2():
    check(2)

def test3():
    check(3)