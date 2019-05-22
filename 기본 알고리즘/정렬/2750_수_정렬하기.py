n = int(input())

list = []

for i in range(n):
    a = int(input())
    list.append(a)

list.sort()

for num in list:
    print(num)