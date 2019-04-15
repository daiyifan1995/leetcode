import sys
from collections import defaultdict

def get_di_graph(user_logs):#构造有向图的临接矩阵
    dict1 ={}

    for y, x in user_logs:
        if x !="Null":
            if x in dict1.keys():
                if y not in dict1[x]:
                    dict1[x].append(y)
            else:
                dict1[x]=[y]
    return  dict1 #dict的结构为{page:【page1，page2】}

def get_short_distance(start_page,pages,dict1,end_page):
    S_to_pages_diatance={}
    for i in pages:
        S_to_pages_diatance[i]=sys.maxsize
    queue=[]#存储的是page
    for i in dict1[start_page]:
        queue.append(i)
        S_to_pages_diatance[i]=1
    i=0
    visited_adj=set()
    while len(queue)!=0:
        if queue[i] in dict1.keys():
            for j in dict1[queue[i]]:
                S_to_pages_diatance[j]=min(S_to_pages_diatance[queue[i]]+1,S_to_pages_diatance[j])
                if j not in visited_adj:
                    queue.append(j)
        visited_adj.add(queue.pop(i))


    return S_to_pages_diatance[end_page]


if __name__ == "__main__":
    line = sys.stdin.readline().strip().split(",")
    start_page=line[0]
    end_page=line[1]
    input=[]
    for line in sys.stdin:
        log = line.split(",")
        input.append([log[0],log[1].strip()])

    pages=set()
    for i in input:
        pages.add(i[0])
        pages.add(i[1])

    dict1=get_di_graph(input)
    print(dict1)
    distance=get_short_distance(start_page,pages,dict1,end_page)
    print(distance)
