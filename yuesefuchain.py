#阿里面试题
#N个有序号的人拍成一圈，每次把第三个人剔除，最后剩下两个人，他们的序号是什么

#约瑟夫环问题
def index(N):
    list=[i for i in range(1,N+1)]
    print(list)
    flag=1
    i=0
    while len(list)>2:
        if flag==3:
            list.remove(list[i])
            flag=1
            if i ==len(list):#若删除元素为最后一个元素，则i=0
                i=0
            continue
        else:
            if i+1==len(list):#若访问到最后一个元素，则i=0
                i=0
            else:
                i=i+1
            flag=flag+1
    return list
print(index(10))

