import sys

def question(line):
    i=0
    while i<len(line):
        if len(line[i])==8:
            i=i+1
            continue
        elif len(line[i])==0:
            i=i+1
            continue
        elif len(line[i])<8:
            for j in range(8-len(line[i])):
                line[i]+="0"
        elif len(line[i])>8:
            t=line[i]
            line[i]=t[0:8]
            line.insert(i+1,t[8:])
        i=i+1

    return sorted(line)


if __name__=="__main__":
    line=sys.stdin.readline().strip().split(" ",1)
    n=int(line[0])
    input=line[1].split(" ",n-1)


    res=question(input)

    x=""
    for i in res:
        x+=" "+i
    print(x.strip())



