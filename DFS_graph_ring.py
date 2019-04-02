
#深度优先遍历并检查是否有环
def findOrder(numCourses,prerequisites):
    if prerequisites == []:
        return [i for i in range(numCourses - 1, -1, -1)]

    graph=[[] for i in range(numCourses)]
    visit=[0 for i in range(numCourses)]
    for x in prerequisites:
        if len(x)==2:
            graph[x[1]].append(x[0])
    print(graph)
    stack = []
    order = []
    for i in range(numCourses):
        if dfs(stack,order,graph,numCourses,visit,i)==[]:
            return []
    return order

def dfs(stack,order,graph,numCourses,visit,i):
    print(i,visit[i],"fe")
    if visit[i]==0:
        stack.append(i)
        print(i,"+")
        order.append(i)
    elif visit[i] == -1:
        return []
    visit[i] = -1
    if visit[i] == 1:  # 若该节点访问过，则pop出一个item访问其指向的节点
        if len(stack) != 0:
            i = stack.pop()
        else:
            return None
    print(i,visit[i],"ing")
    for j in graph[i]:
        if dfs(stack,order,graph,numCourses,visit,j)==[]:
            return []
    visit[i]=1
    print(i, visit[i], "ed")
    return None



if __name__ == "__main__":
    input = [[0,1],[2,1],[3,0],[3,2]]
    print(findOrder(4,input))
