days = [31,28,31,30,31,30,31,31,30,31,30,31]
week = ["MON","TUE","WED","THU","FRI","SAT","SUN"]

x, y = input().split()
x = int(x)
y = int(y)

total_day = y

for i in range(1,x):
    total_day += days[i-1]

print(week[((total_day-1)%7)])