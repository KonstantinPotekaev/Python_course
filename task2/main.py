import math


def myHex(num):
    d = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
         13: 'D',
         15: 'E'}
    s = ''
    while num > 0:
        s += d.get(num % 16)
        num //= 16
    s = s[::-1]
    return s


def cDenominator(a, b, c, d):
    g = math.gcd(b, d)
    cDen = b * d // g
    a *= cDen // b
    c *= cDen // d
    b *= cDen // b
    d *= cDen // d
    return a, b, c, d


def frac(f1, f2):
    a, b = map(int, f1.split('/'))
    c, d = map(int, f2.split('/'))
    prodA = a * c
    prodB = b * d
    a, b, c, d = cDenominator(a, b, c, d)
    sum = a + c
    return f'{sum}/{b}', f'{prodA}/{prodB}'


print(frac('1/2', '3/4'))
