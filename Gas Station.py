class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        tank=[ [ 0 for i in range(len(gas))] for i in range(len(gas))]
        flag= [-1 for i in range(len(gas))]

        for i in range(len(gas)):#从0start
            order=[i for i in range(i,len(gas))]+[i for i in range(0,i)]

            for j in order:
                if j==0:
                    tank[i][j] = tank[i][-1] + gas[j] - cost[j]
                else:
                    tank[i][j]=tank[i][j-1]+gas[j]-cost[j]
                if tank[i][j]<0:
                    tank[i] =flag
                    break
            if tank[i]!= flag:
                return i
        return -1



gas  = [1,2,3,4,5]

cost = [3,4,5,1,2]

S=Solution()
print(S.canCompleteCircuit(gas,cost))
