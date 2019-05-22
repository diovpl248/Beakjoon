c = int(input())

for i in range(c):
    line = input()
    score = 1
    total_score = 0

    for char in line:
        if char == "O":
            total_score += score
            score += 1
        else:
            score = 1

    print(total_score)