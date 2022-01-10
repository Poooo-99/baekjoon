
n = int(input())

num = list(map(int, input().split()))

print(num)

max = num[0]
min = num[0]

for i in num[1:]:
    if i > max:
        max = i
    elif i< min:
        min = i

print(min ,max)


###### 파이썬 내장함수 min(), max() 사용

n = int(input())
num = list(map(int, input().split()))
print(min(num), max(num))