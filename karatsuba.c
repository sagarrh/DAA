#include <stdio.h>

int strl(int a) {
    int count = 0;
    while (a) {
        a /= 10;
        count++;
    }
    return count;
}

int power(int a, int b) {
    if (b == 0)
        return 1;
    else if (b % 2 == 0)
        return power(a * a, b / 2);
    else
        return a * power(a * a, (b - 1) / 2);
}

int karatsuba(int x, int y) {
    if (x < 10 || y < 10)
        return x * y;
    else {
        int n = strl(x > y ? x : y);
        int half = n / 2;
        int a1 = x / power(10, half);
        int b1 = x % power(10, half);
        int a2 = y / power(10, half);
        int b2 = y % power(10, half);
        int a1a2 = karatsuba(a1, a2);
        int b1b2 = karatsuba(b1, b2);
        int ab = karatsuba(a1 + b1, a2 + b2);
        int minus = ab - a1a2 - b1b2;
        return a1a2 * power(10, 2 * half) + minus * power(10, half) + b1b2;
    }
}

int main() {
    int a = 12;
    int b = 13;
    int result = karatsuba(a, b);
    printf("Product: %d\n", result);
    return 0;
}
