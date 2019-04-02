
input=[[1,0],[0,1],[2,1],[1,2]]
#查找有向图中是否有环

def canFinish(numbercourse,prerequisites):
    graph = [[] for _ in range(numbercourse)]
    visit = [0 for _ in range(numbercourse)]#将未访问过的节点设置为0
    for x, y in prerequisites:#构造有向图的临界矩阵
        graph[x].append(y)
    for course in range(numbercourse):#遍历全部节点
        if not dfs(course,visit,graph):
            return False
    return True

def dfs(i,visit,graph):
    #   0，此节点没有被访问过

    # -1，被访问过至少1次，其后代节点正在被访问中
    #
    # 1，其后代节点都被访问过。
    if visit[i] == -1:
        return False
    if visit[i] == 1:
        return True
    visit[i] = -1
    for j in graph[i]:
        if not dfs(j,visit,graph):
            return False
    visit[i] = 1
    return True
if __name__ == "__main__":
    print(canFinish(4,input))