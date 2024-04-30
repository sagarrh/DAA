def karatsuba(a, b):
    if a < 10 or b < 10:
        return a * b
    else:
        n = max(len(str(a)), len(str(b)))
        half = n // 2
        a1 = a // (10 ** half)
        a2 = a % (10 ** half)
        b1 = b // (10 ** half)
        b2 = b % (10 ** half)
        a1b1 = karatsuba(a1, b1)
        a2b2 = karatsuba(a2, b2)
        a1b2_minus_a2b1 = karatsuba(a1 + a2, b1 + b2) - a1b1 - a2b2
        return a1b1 * (10 ** (2 * half)) + (a1b2_minus_a2b1) * (10 ** half) + a2b2

print(karatsuba(121323, 11212))
