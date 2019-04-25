

# if __name__=="__main__":
#     count=int(input())
#     input=[int(i) for i in input().split(" ")]
#     i=0
#     while i<count:
#         n=input[i]
#         interval=n+1
#         dis=[]
#         x=0
#         while x not in dis:
#             dis.append(x)
#             if x+interval < n*4:
#                 x = x + interval
#             else:
#                 x= x+interval-n*4
#         print(len(dis)+1)
#         i=i+1


import sys

if __name__ == '__main__':
    str_s = input()
    str_t = input()

    count = 0
    i = 0
    j = 0
    if len(str_t)>len(str_s):
        print(0)
    while i <len(str_s) :
        if(str_s[i]==str_t[j]):
            i+=1
            j+=1
        elif (str_s[i]=="?"):
            i+=1
            j+=1
        else:
            i=i-j+1
            j=0
        if j==len(str_t):
            count+=1
            i=i-len(str_t)+1
            j=0
    print(count)