def merge_sort(arrays):
   #时间复杂度NlogN
    if len(arrays)==0 or arrays==[[]]:
        return [[]]
    length=len(arrays)
    for i in range(0,length-1,2):
        m,n=0,0
        while m<len(arrays[i]) and n<len(arrays[i+1]):
            if arrays[i][m]<arrays[i+1][n]:
                m=m+1
            elif arrays[i][m]>=arrays[i+1][n]:
                t=arrays[i][m]
                arrays[i][m]=arrays[i+1][n]
                arrays[i].insert(m+1,t)
                n=n+1
                m=m+1

        if n<len(arrays[i+1]):
            arrays[i]=arrays[i]+arrays[i+1][n:]

        arrays[i+1]=[]


    arrays=[i for i in arrays if i!=[]]

    if len(arrays)>1:
        arrays=merge_sort(arrays)

    return  arrays







input=[1,2,3,4]
arrays=[[i] for i in input]
print(merge_sort(arrays)[0])