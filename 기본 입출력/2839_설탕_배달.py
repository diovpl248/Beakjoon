n = int(input())

five_count = 1
total_count = -1

if n%3 == 0:
    total_count = n//3

while five_count <= n/5:
    if (n - 5*five_count) % 3 == 0:
        total_count = five_count + (n - 5*five_count) // 3
    five_count += 1

print(total_count)