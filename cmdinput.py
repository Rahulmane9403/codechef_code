# # # input = [6,12,65,22,626955,2398,898,8,65,32,9,2321,1,2,3,4,98,81]
# # # input.sort()
# # # list1=[]
# # # # list1.append(input)
# # # # list1.sort()
# # # # print(list1)
# # # # for i in range(int(input())):
# # # #     n=int(input())
# # # #     l=[]
# # # #     c=0
# # # #     for j in range(n):
# # # #         a , b = map(int,input().split())
# # # #         l.append([b, a])
# # # #     l.sort()
# # # #     print(l)
# # # #     d = {j[1] : j[0] for j in l}
# # # #     print(d)
# # # #     for j in d.keys():
# # # #         if j <= 8:
# # # #             c = c + d[j]
# # # #     print(c)

# # # import pickle
# # # with open('model_pickle_nameof file','wb') as f:
# # #     pickel.dump(model,f)
# # # with open('model_pickle','rb') as f:
# # #     mp = pickle.load(f)
# # #     mp.predict()

# # #     from sklearn.externals import joblib
# # # #     joblib.dump(model,"model_joblib")
# # # #     mj = joblib.load('model_joblib')
# # # #     mj.predict

# # # n=int(input())
# # # for i in range(n):
# # #     p=int(input())
# # #     x,y=input()
# # # #     if x.count('0') == y.count('0') and x.count('1') == y.count('1'):
# # # #         print('YES')
# # # #         else:
# # # #             print("NO") 
# # # n=int(input())
# # # for _ in range(n):
# # #     a,b=map(int,input().split())
# # #     s= input()
# # #     l = [b]
# # #     for j in s:
# # #         if j =='L':
# # #             b+=1
# # #         else:
# # #             b-=1
# # #         l.append(b)
# # #     s= set(l)
# # #     print(len(s))
# # # from collections import Counter as Cn
# # # n=int(input())
# # # for i in range(n):
# # #     a=int(input().strip())
# # #     types = list(map(int, input().strip().split()))
    
# # #     d = Cn(types)
# # #     for i in d:
# # #         if d[i]&1:
# # #             f = 0
# # #             break
# # #     print("Yes")
# # # else:
# # #     print("No")
# # # for _ in range(int(input())):
# # #     p = list(map(int,input().split()))
# # #     a = input()
# # #     s = 0
# # #     l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# # #     # print(p)
# # #     # print(a)
# # #     for i in range(len(l)):
# # #         if(l[i] not in a):
# # #             s += p[i]
# # # #             print(p[i])
# # # #             # print(s)
# # # #     print(s)
# # # for _ in range(int(input())):
# # #     # list1=list(map(int,input().split()))
# # #     list1=[1,2,3,4,5,6,7,8,910 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26]
# # #     list2=input()
# # #     sum=0
# # #     abc="abcdefghijklmnopqrstuvwxyz"
# # #     for x in range(26):
# # #         if abc[x] not in list2:
# # #             k=list1[x]
# # #             sum+=k
# # #     print(sum)
# # # n=int(input())
# # # # for i in range(n):
# # # #     l=input()
# # # #     p=len(l)
# # # #     print(l)
# # # #     if p % 2 == 1:
# # # #         middle = p // 2
# # # #         l = l[:middle] + l[middle+1:]
# # # #     half1 = l[:n//2]
# # # #     half2 = l[n//2:]
# # # #     print(half1)
# # # #     print(half2)
# # # #     count1 = {}
# # # #     count2 = {}
# # # #     for c in half1:
# # # #         count1[c] = count1.get(c, 0) + 1
# # # #     for c in half2:
# # # #         count2[c] = count2.get(c, 0) + 1

# # # #     # Compare the frequency of each character in each half
# # # # # return count1 == count2
# # # # print((l))

# # #     # Find the length of the string
# # # j=int(input())
# # # for i in range(j):
# # #     s=(input())
# # # def is_lapindrome(s):
# # #     n = len(s)
    

# # #     # If the length of the string is odd, ignore the middle character
# # #     if n % 2 == 1:
# # #         middle = n // 2
# # #         s = s[:middle] + s[middle+1:]

# # #     # Split the string in two halves
# # #     half1 = s[:n//2]
# # #     half2 = s[n//2:]

# # #     # Count the frequency of each character in each half
# # #     count1 = {}
# # #     count2 = {}
# # #     for c in half1:
# # #         count1[c] = count1.get(c, 0) + 1
# # #     for c in half2:
# # #         count2[c] = count2.get(c, 0) + 1
# # #         if count1 == count2:
# # #             print('Yes')
# # #     else:
# # #      print('No')
# # # print(is_lapindrome())
# # # cook your dish here
# # # for i in range(int(input())):
# # #     s= input().strip()
# # #     str1=list(s[:len(s)//2])
# # #     print(str1)
# # #     s=s[::-1]
# # #     print(s)
# # #     str2= list(s[:len(s)//2])
# # #     print(str2)
# # #     str1.sort()
# # #     print(str1)
# # # #     str2.sort()
# # # #     print(str2)
# # # #     if str1==str2:
# # # #         print("YES")
# # # #     else:
# # # #         print("NO")
# # # import math

# # # # def largest_mega_square(N, A):
# # # p=int(input())
# # # for i in range(p):
# # #     N,A=list(map(int,input().split()))
# # #     # Calculate the area of all N squares
# # #     # total_area = N * A * A
    
# # #     # Find the side length of the largest square that can be obtained
# # #     side_length = math.floor(math.sqrt(N))
    
# # #     # Check if the side length is greater than A, if not, return A
# # #     if p>0:
# # #         print(side_length*A)
# # # cook your dish here
# # # n=int(input())
# # # for i in range(n):
# # # #     p = input()
# # # #     w1, w2, x1, x2, m=map(int,input().split())
# # # #     # w1, w2, x1, x2, m = int(w1), int(w2), int(x1), int(x2), int(m)
# # # #     w = w2-w1
# # # #     a = x1*m
# # # #     b = x2*m
# # # #     if w not in range(a,b+1):
# # # #         print(0)
# # # #     else:
# # # #         print(1)
    
# # # w = [1,2,3]
# # # a = 5
# # # b = 3
# # # if w in range(a, b + 1):
# # #         print(0)
# # # else:
# # # #         print(1)
# # # for _ in range(int(input())):
# # #     a = int(input())
# # #     p = list(map(int, input().split()))
# # #     def count_misheard_players(p):
# # #         n = len(p)
# # #         misheard_players = 0
# # #         for i in range(1, n):
# # #             if p[i] != p[i-1]:
# # #                 misheard_players += 1
# # #         return misheard_players
# # #     print(count_misheard_players(p))

# # # for _ in range(int(input())):
# # #     #print(j+1)
# # #     e=int(input())
# # #     l=list(map(str,input().split()))
# # #     l1=[]
# # #     for i in range(0,e-1):
# # #         if(l[i]!=l[i+1]):
# # #         #    print(l[i]!=l[i+1])
# # #            l1.append(i) 
# # #            l1.append(i+1)
# # #     count=0
# # #     count=len(l1)
# # # #     print(count)
# # #     print(count if(count) else 0)
# # # # cook your dish here
# # # t=int(input())
# # # for _ in range(t):
# # #     n=int(input())
# # #     a=list(map(int,input().split()))
# # #     d={}
# # #     for i in a:
# # #         if i not in d:
# # #             d[i]=1
# # #             # print(d[i])
# # #         else:
# # #             d[i]+=1
# # #             # print(d[i])
# # #     count=list(d.values())
# # #     print(count)
# # #     l=count.count(max(d.values()))
# # #     print(l)
# # #     if (l==1):
# # #         print("YES")
# # #     else:
# # #         print("NO")
# # # cook your dish here

# # def solve(valN, val):
# #     if val[:int(valN/2)] == val[int(valN/2):]:
# #         return "YES"
# #     else:
# #         return "NO"
# # print(solve)
    

# # n = int(input())

# # for _ in range(n):
# #     valN = int(input())
# #     val = input()
# #     print(solve(valN, val))
# # for _ in range(int(input())):
# #     n=int(input())
# #     l=list(map(int,input().split()))
# #     x = set(l)
# #     if(0 in x):
# #         x.remove(0)
# # #     print(leRahuln(x))
# # birth = str(input())
# # c = int(input())
# # # d = (birth == c)
# # print(birth + c)
# # a = int(input())
# # b = int(input())
# # c = a + b
# # print('c = ' + str(c))
# # cook your dish here
# # n=int(input())
# # for i in range(int(input())):
# #     a = int(input())
# #     b = list(map(int,input().split()))
# #     c = int(input())   
# #     b.sort()
# #     uj = b[c-1]
# #     print(b.index(uj)+1)
#     # store = b[c]
#     # print(type(str(store)))
#     # print(b[c])
#     # for i in range(a):
#     #     if (b[c] == b[i]):
#     #         print(i+1)
#             # break
# #     # print(b) 
#     # print(b[c])
#          # else:
#             #     print(len(b))
#         # if b[i] == b[i+1]:
#         #     s = b.pop()
#         #     print(s)
# # function to solve the problem for a single test case
# # def solve():
# #     # read input
# #     n = int(input())
# #     a = list(map(int, input().split()))
# #     k = int(input())

# #     # sort the array
# #     a.sort()

# #     # find the position of Uncle Johny
# #     for i in range(n):
# #         if a[i] == a[k-1]:
# #             print(i+1)
# #             break

# # # read the number of test cases
# # t = int(input())

# # # solve each test case
# # for i in range(t):
# #     solve()
# # from itertools import takewhile
# for i in range(int(input())):
#     N = int(input())
#     A = list(map(int, input().split()))
#     for i in range(A):
#         if 
#     A[-1] = 
#     # a.sort()
#     # N=8
#     # temp = a.index(N)
#     # res = a[:temp]
#     # temp2=a.index(N+1)
    
#     # temp = a.index(N)
#     # res = a[:temp]
#     # for j in range(len(A)):
#     print(A.index(-1))
#         #     # temp = a.index(N)
#         #     # res = a[:temp]
#         #     print(str(res))
#         # else:
#         #     temp2=a.index(N+1)
#         #     print(temp2)

#             # res = list(takewhile( a))
#             # print(str(res))
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    for i, x in enumerate(a[::-1]):
        # print(a[::-1])
        if x <= 8:
            print(n-i)
            break