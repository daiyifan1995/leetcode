import sys

def DirGraphShorDis(matrix,start,end):
    dist=matrix[start]#设置start的行的dist
    visited=[start]
    while True:
        p = 1
        min_weight, visit = sys.maxsize, 1
        while p<len(dist):#找到在dist中距离起始点最近的点
            if min_weight>dist[p] and p not in visited:
                min_weight=dist[p]
                visit=p
            p+=1
        if visit==1: #若不存在未访问的距离最近的点则退出
            break
        i=1
        while i<len(dist):
            if matrix[visit][i]!=sys.maxsize and i not in visited:
                matrix[start][i]=min(matrix[start][i], matrix[visit][i]+matrix[start][visit])
            i+=1
        visited.append(visit)
        if len(visited)==len(dist)-1:#若所有的点都放问过了则退出
            break
    print(dist)
    return dist[end]


if __name__=="__main__":
    #inital admatrix
    l1=[int(i)for i in sys.stdin.readline().strip().split(" ")] #input为 节点数 边个数
    point_num,edge_num=l1[0],l1[1]

    #节点编号从1开始，为了方便基数，第0个元素为空
    matrix=[[sys.maxsize for i in range(point_num+1)]for i in range(point_num+1)]
    for i in range(edge_num):
        line= [int(i) for i in sys.stdin.readline().strip().split(" ")] #input为 start，end，weight
        start,end,weight=line[0],line[1],line[2]
        if matrix[start][end]>weight:
            matrix[start][end]=weight

    l2=[int(i)for i in sys.stdin.readline().strip().split(" ")]#input为 start end
    start, end= l2[0], l2[1]

    if start==end:
        print("0")
    dist=DirGraphShorDis(matrix, start, end)
    if dist!=sys.maxsize:
        print(dist)
    else:
        print("NA")

#test1
# 6 9
# 1 2 1
# 1 3 12
# 2 3 9
# 2 4 3
# 3 5 5
# 4 3 4
# 4 5 13
# 4 6 15
# 5 6 4
# # 1 6

#test2
# 4 5
# # 1 2 3
# # 1 3 3
# # 1 4 4
# # 2 3 5
# # 3 4 3
#1 3