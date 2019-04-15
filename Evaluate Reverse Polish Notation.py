def evalRPN(tokens) -> int:
    stack = []
    #在字典中使用lambda表达式！！！！！！！！！！！！！！！！！！！！！！！！！！！
    OP = {'+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '*': lambda x, y: x * y,
          '/': lambda x, y: x // y if x // y > 0 else -(abs(x) // abs(y))}
    for i in tokens:
        if i in OP.keys() :
            if len(stack) >= 2:
                a = int(stack.pop())
                b = int(stack.pop())
                res=OP[i](b,a)###字典的lambda表达式的调用！！！！！！！！！！！！！！！！！！！！！！！！！！
                res=int(res)
                stack.append(str(res))
        else:
            stack.append(i)
    if len(stack)==1:
        return stack[0]
    else :
        return []
tokens= ["2", "1", "+", "3", "*"]
print(evalRPN(tokens))