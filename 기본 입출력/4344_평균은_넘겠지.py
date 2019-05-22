c = int(input())

for i in range(c):
    scores = list(map(int,input().split(" ")))
    avg = sum(scores[1:]) / scores[0]
    avg_upper_cnt = 0
    for j in range(scores[0]):
        if scores[j+1] > avg:
            avg_upper_cnt += 1
    print(format(avg_upper_cnt/scores[0]*100,"0.3f")+"%")