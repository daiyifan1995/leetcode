import sys

def question(input):
    stack_both=[]
    stack_item=[]
    dict1={")":"(","]":"[","{":"}"}
    number_list=[str(i) for i in range(0,10)]
    number_list=set(number_list)
    for i in input:
        if i not in dict1.keys():
            stack_both.append(i)
        else:
            stack_item.append(i)
            stack=[]
            while stack_both[-1] not in dict1.values():
                j=stack_both.pop()
                stack.append(j)
            stack_both.pop()
            repeat=""
            while stack_both[-1] in number_list :
                repeat=stack_both.pop()+repeat
                if len(stack_both)==0:
                    break
            for i in range(int(repeat)):
                for j in range(len(stack)-1,-1,-1):
                    stack_both.append(stack[j])

    return  stack_both


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    res=question(line)
    output=""
    for j in range(len(res) - 1, -1, -1):
        output+=res[j]
    print(output)