str = input()

length = len(str)

for i in range(0,length//10):
    print(str[i*10:i*10+10])

print(str[(length/10)*10:len(str)])