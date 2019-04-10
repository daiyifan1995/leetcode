#(1)将连续出现三次及以上的字母删去，只剩下两个，eg:wooooow 变为woow
#(2)将AABB型的字母换为AAB
#(1)的优先级大于(2)

def check(sen):
    target=[]
    new_sen=""
    for i in sen:
        if len(target)==0:
            target=[i,1,0]#[字母，出现次数，前面是否存在AA]
        else:
            if target[0]==i:
                target[1]+=1
                if target[1]>2:
                    continue
            else:
                target = [i, 1, 0]
        new_sen = new_sen + i

    sen=new_sen
    new_sen=""
    target = []
    for i in sen:
        if len(target)==0:
            target=[i,1,0]
        else:
            if target[0]==i:
                target[1]+=1
                if target[1]==2 and target[2]==0:
                    target[2]=1
                elif target[1] == 2 and target[2] == 1:
                    target[2] = 0
                    target[1] = 1
                    continue
            else:
                if target[1]==1:
                    target = [i, 1, 0]
                elif target[1]==2:
                    target = [i, 1, 1]

        new_sen = new_sen + i


    return new_sen


print(check("WOOOWAAABBBBCCCC"))
