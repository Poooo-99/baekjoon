
# n = 9
# num = list()

# for i in range(0,n):
#         num.insert(i,input())
    
# max = num[0]

# for i in num[1:]:
#     if i> max:
#         max =i

# print(max)
# print(num.index(max)+1)

####위에 코드는 왜 안되는 거임?

num_list = []
for i in range(9):
    num_list.append(int(input()))
    
print(max(num_list))
print(num_list.index(max(num_list))+1)