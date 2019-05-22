def get_next(n):
    next = n

    if n >= 10000:
        next += n // 10000
        n = n % 10000
    if n >= 1000:
        next += n // 1000
        n = n % 1000
    if n >= 100:
        next += n // 100
        n = n % 100
    if n >= 10:
        next += n // 10
        n = n % 10

    next += n

    return next


check_list = [False]*10001
check_list[0] = True

for i in range(10001):

    if check_list[i] == False:
        print(i)

    next = get_next(i)

    if next <= 10000:
        check_list[next] = True

