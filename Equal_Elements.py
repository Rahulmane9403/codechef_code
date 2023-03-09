# # n=int(input())
# # for i in range(int(input())):
# #     a=int(input())
# #     for j in range(a):
# #         x = list(map(int, input().split()))
#         # print(x)
# import math
# for i in range(int(input())):
#     a = int(input())
#     x = list(map(int, input().split()))
#     # # print(x)  # do something with x here
#     arr_sum = sum(x)
#     # Calculate the average value of the array
#     avg = math.ceil(arr_sum / len(x))
#     # print(avg)
#     operations = 0
#     for i in range(len(x)):
#         if x[i] != avg:
#             operations += 1
#     print(operations)
#     # x.sort()
#     # counter = 0
#     # for i in x:
#     #      counter += abs(i-x[math.ceil(len(x)//2)])
#     # print(counter)
from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    C = Counter(arr)
    print(C)
    maxi = max(C.values())
    print(maxi)
    print(n - maxi)