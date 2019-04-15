def duplicate_by_change_arrary(list):
    if len(list)==0:
        return -1
    for i in range(len(list)):
        if i == list[i]:
            continue
        elif list[list[i]]==list[i]:
            return list[i]
        else:
            t=list[list[i]]
            list[list[i]]=list[i]
            list[i]=t
    return -1



print(duplicate_by_change_arrary([2,3,1,0,2,5,3]))