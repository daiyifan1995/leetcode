def numbers(A,B,C,D):
    counts_D=D
    counts_CA_to_D=min(A,C)
    counts_B_to_D=B//2
    lef_B=B % 2
    lef_A=A-counts_CA_to_D
    if lef_A>0:
        counts_AB_to_D=min(lef_B,lef_A//2)
    else:
        counts_AB_to_D=0
    lef_A =lef_A-counts_AB_to_D*2
    counts_A_to_D=lef_A//4

    counts_D +=counts_CA_to_D+counts_B_to_D+counts_AB_to_D+counts_A_to_D

    return counts_D
# if __name__ == "__main__":
#     # count = int(input())
#     # array = []
#     # for i in range(count):
#     #     myinput = [int(x) for x in input().split(" ")]
#     #     array .append(myinput)
#     #
#     # for myinput in array:
#     #     print(numbers(myinput[0],myinput[1],myinput[2],myinput[3]))

def sort(y_list,ascend,N):
    input=y_list
    y_list=y_list[:N]
    if ascend==0:#升序
        y_list_sorted = sorted(y_list)
    else :#降序
        y_list_sorted=sorted(y_list,reverse=True)

    return y_list_sorted+input[N:]

if __name__ == "__main__":
    sort_times=int(input().split(" ")[-1])#为0
    orign=input()
    if sort_times == 0:
        print(orign)
        exit()

    y_list=[int(i)for i in orign.split(" ")]
    array=[]
    for i in range(sort_times):
        myinput=[int(i)for i in input().split(" ")]
        array.append(myinput)
    for myinput in array:
        ascend=myinput[0]
        N=myinput[1]
        y_list=sort(y_list, ascend, N)
    output=""
    for i in y_list:
        output+=str(i)+" "
    print(output.strip())

# import sys
# def sum_min(A,N):
#     # sum=0
#     # list_x=[i for i in range(1,N+1)]
#     # for i in range(N):
#     #     if A[i]>=list_x[i]:
#     #         sum+=A[i]-list_x[i]
#     #     else:
#     #         sum+=list_x[i]-A[i]
#     # return sum
#
#
# if __name__ == "__main__":
#     N=int(input())
#     A=[int(i) for i in input().split(" ")]
#     res=sys.maxsize
#     for i in range(N):
#         res=min(res,sum_min(A,N))
#         A=A[1:]+A[0:1]
#     print(res)






