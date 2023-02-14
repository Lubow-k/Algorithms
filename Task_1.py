def division(a, b):
    if b == 0:
        raise ZeroDivisionError
    digits = []
    while a > 0:
        digits.append(a % 10)
        a = a // 10
    digits = digits[::-1]

    res = []
    buf = 0
    lght = len(digits)
    for i in range(lght):
        buf += digits[i]
        whole_count = 0
        if buf >= b:
            whole = 0
            while whole + b <= buf:
                whole += b
                whole_count += 1
            buf -= whole
        res.append(whole_count)

        if i != lght - 1:
            buf *= 10

    size = len(res)
    k = size - 1
    num = 0
    for i in range(size):
        num += res[i] * 10 ** k
        k -= 1
    return num, buf


x, y = map(int, input().split())
try:
    result, remainder = division(x, y)
    print(f'Dividing {x} by {y}: quotient {result}, remainder {remainder}')
except ZeroDivisionError:
    print("Division by zero")





