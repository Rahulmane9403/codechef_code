# # list1=[]
# # n=int(input())
# # for _ in range(n):
# #     # c=[]
# #     b=int(input())
# #     list1.append(b)
# # list1.sort()
# # for j in range(0,len(list1)):
# #     print(list1[j])
# #     # c.append(b)

# #     # c = b.sort()
    
# # # c = [5,5,5,5,2,1,3,4,7,8]
# # # b=c.sort
# # # # print(b)
# # age=int(input())
# # if age >=20:
# #     print("eligi")
# # elif age >= 18:
# #     print("expericenced")
# # else:
# #     print("not elig")

# import http.client
# from urllib.parse import urlparse

# def parse_http_request(url):
#     parsed_url = urlparse(url)
#     conn = http.client.HTTPSConnection(parsed_url.netloc) if parsed_url.scheme == "https" else http.client.HTTPConnection(parsed_url.netloc)
#     conn.request("GET", parsed_url.path)
#     resp = conn.getresponse()
#     headers = resp.getheaders()
#     http_version = "HTTP/{}".format(resp.version/10) # Get HTTP version from response
#     parsed_request = "{} {} {}\r\n".format("GET", parsed_url.path or "/", http_version)
#     parsed_request += "Host: {}\r\n".format(parsed_url.netloc)
#     for header in headers:
#         if header[0].lower() != "connection":
#             parsed_request += "{}: {}\r\n".format(header[0], header[1])
#     conn.close()
#     return parsed_request
# url = input() 
# parse_http_request(url)
# cook your dish here
# for i in range(int(input())):
#     n=int(input())
#     s=input()
#     l=[]
#     for i in s:
#         if(i=='H'or i=='T'):
#             l.append(i)
#     l=''.join(l)
#     h=l.count('H')
#     t=l.count('T')
#     hh=l.count('HH')
#     ht=l.count('HT')
#     #print(hh)
#     if(h!=t or hh>0 or ht<len(l)//2 ):
#         print('Invalid')
#     else:
#         print('Valid')
# for i in range(int(input())):
#     n=int(input())
#     l=[]
#     l.append(n)
#     # print(n)
#     for i in l:
#         if(l[0]+l[1]==l[2] or l[2]+l[1]==l[0]):
#             print("Yes")
# #         else:
# #             print("No")
# for i in range(int(input())):
#     n = int(input())
#     l = []
#     l.append(n)
#     # if len(l) >= 3:
#     if (l[0] + l[1] == l[2]) or (l[2] + l[1] == l[0]):
#             print("Yes")
#     else:
#             print("No")
# cook your dish here
t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    if (a+b==c or b+c==a or b==a+c):  
        print("YES")
    else:  
        print("NO")
    


