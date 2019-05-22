str = input()
counts = [0] * (ord("Z") - ord("A")+1)
str = str.upper()

max_count = 0
max_char = "?"

for char in str:
    index = ord(char) - ord("A")
    counts[index] += 1
    if counts[index] > max_count:
        max_count = counts[index]
        max_char = chr(ord("A")+index)
    elif counts[index] == max_count:
        max_char = "?"

print(max_char)





