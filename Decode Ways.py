from collections import defaultdict

class Solution:
    def numDecodings(self, s: str):
        letter={}
        for i in range(65,65+26):
            letter[str(i-64)]=chr(i)
        print(letter)

        #假设当前index为i，当s[i]有效的时候，则dp[i] = dp[i - 1]+1。当s[i - 1]s[i]组成的字符串有效时，dp[i] = dp[i - 2]+1
        dp=[0 for i in range(len(s))]
        if len(s)>0:
            if s[0] in letter.keys():
                dp[0] = 1
        if len(s)>1:
            if s[1] in letter.keys():
                dp[1] =  dp[1] + dp[0]
            if s[0]+s[1] in letter.keys():
                dp[1] =  dp[1] + dp[0]
        for i in range(2,len(s)):
            if s[i] in letter.keys():
                print(s[i])
                dp[i]=dp[i]+dp[i-1]
            if s[i-1]+s[i] in letter.keys():
                print(s[i-1]+s[i])
                dp[i]=dp[i]+dp[i-2]

        print(dp)
        return dp[-1] if len(dp)!=0 else 0



if __name__ == "__main__":
    SOLUTION=Solution()
    input=""
    print(SOLUTION.numDecodings("101"))