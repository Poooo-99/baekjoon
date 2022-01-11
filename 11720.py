
numnum = int(input())               ##numnum = 숫자의개수
num = int(input())              ##num = 숫자
    
sum = 0
temp =num
for i in range(numnum-1, 0,-1):
    sum += temp // (10**i)
    temp = temp % (10**i)
sum += temp
print(sum)


        
