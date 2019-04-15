import sys



def question3(arrays,n):
    not_zero=[i for i in arrays if i!=0]
    min_not_zero = min(not_zero)
    print(min_not_zero)
    aft=[i-min_not_zero if i!=0 else 0 for i in arrays ]

    target=[0 for i in range(n)]
    if aft ==target:
        print(0)
    return aft


#Q1
# import sys
#
# n, k = [ int(x) for x in sys.stdin.readline().strip().split(" ")]
# dp = [[0 for x in range(k+1)] for y in range(n+1)]
#
# dp[1] = [ 1 for x in range(k + 1)]
#
# for i in range(1, n+1):
#     for j in range(1, k+1):
#         if j == 0 :
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j]  = min(dp[i-1][j], dp[i//2][j-1]+dp[i//2][j-1])
#
# print(dp[n][k])



# Q2
# import sys
#
# if __name__ == "__main__":
#     num = int(sys.stdin.readline().strip())
#     arr = [ int(x) for x in sys.stdin.readline().strip().split(" ")]
#     count = 0
#     for i in range(1, num):
#         arr[i] = arr[i] + arr[i-1]
#         count += abs(arr[i-1])
#
#     print(count)

if __name__ == "__main__":
    line= sys.stdin.readline().strip().split(" ")
    n=int(line[0])
    k=int(line[1])

    not_null_arrays= [int(i) for i in sys.stdin.readline().strip().split(" ") if int(i)!=0]

    sort_not_null_arrays=set(sorted(not_null_arrays))
    print(sort_not_null_arrays[0])
    max_arrarys=max(sort_not_null_arrays)
    for i in range(k):
        if i<len(sort_not_null_arrays):
            max_arrarys=max_arrarys-sort_not_null_arrays[i]
            if max_arrarys==0:
                print(0)
                break





