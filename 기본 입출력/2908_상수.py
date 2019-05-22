a, b = input().split()

a = int(a)
b = int(b)

reversed_a = (a % 10) * 100
a //= 10
reversed_a += (a % 10) * 10
a //= 10
reversed_a += (a % 10) * 1

reversed_b = (b % 10) * 100
b //= 10
reversed_b += (b % 10) * 10
b //= 10
reversed_b += (b % 10) * 1

if reversed_a > reversed_b:
    print(reversed_a)
else:
    print(reversed_b)