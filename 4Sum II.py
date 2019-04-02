# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# Output:
# 2

#将input分为A\B和C\D两个部分


from collections import defaultdict


class Solution:
    def fourSumCount(self, A, B, C, D) :
        sum_dict = defaultdict()
        for i in range(len(A)):
            for j in range(len(B)):
                sum_dict[A[i] + B[j]] = sum_dict.get(A[i] + B[j], 0)+1

        res = 0
        print(sum_dict)

        for i in range(len(C)):
            for j in range(len(D)):
                sum = C[i] + D[j]
                print(sum)
                res = res + sum_dict.get(-1 * sum, 0)

        return res




if __name__ == "__main__":
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]

    SOLUTION=Solution()
    input=""
    print(SOLUTION.fourSumCount( A, B, C, D) )