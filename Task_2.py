def Karatsuba(x, y, n):
    if n == 1:
        return x*y
    else:
        new_n = n // 2
        a, b, c, d = x // 10 ** new_n, int(x % 10 ** new_n), y // 10 ** new_n, int(y % 10 ** new_n)
        new_n = new_n if (new_n % 2 == 0 or new_n == 1) else new_n + 1
        ac = Karatsuba(a, c, new_n)
        bd = Karatsuba(b, d, new_n)
        for_ad_bc = Karatsuba(a + b, c + d, new_n)
        ad_bc = for_ad_bc - ac - bd
        return 10**n * ac + 10**(n // 2) * ad_bc + bd


def solution(data: str) -> int:
    inp = data.split()
    n = max(map(len, inp))
    n = n if (n % 2 == 0 or n == 1) else n + 1
    x, y = map(int, inp)
    return Karatsuba(x, y, n)

