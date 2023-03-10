def mult(x_0, y_0):
    def karatsuba(x, y, n):
        if n == 1:
            return x * y
        else:
            new_n = n // 2
            a, b, c, d = x // 10 ** new_n, int(x % 10 ** new_n), y // 10 ** new_n, int(y % 10 ** new_n)
            new_n = new_n if (new_n % 2 == 0 or new_n == 1) else new_n + 1
            ac = karatsuba(a, c, new_n)
            bd = karatsuba(b, d, new_n)
            for_ad_bc = karatsuba(a + b, c + d, new_n)
            ad_bc = for_ad_bc - ac - bd
            return 10 ** n * ac + 10 ** (n // 2) * ad_bc + bd

    m = max(map(len, map(str, [x_0, y_0])))
    m = m if (m % 2 == 0 or m == 1) else m + 1
    return karatsuba(x_0, y_0, m)


def solution(data: str) -> int:
    x, y = map(int, data.split())
    return mult(x, y)

