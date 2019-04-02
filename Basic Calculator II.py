

#识别出表达式中的字符，将*/运算直接计算出数字后后放入栈中
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        cal = ["0"]
        number=[str(i) for i in range(0,10)]
        mark=["+","-","*","/"]
        i = 0
        while i < len(s):
            if s[i] in number and cal[-1][0] in number:
                cal[-1]=cal[-1]+s[i]
                i=i+1
            elif s[i] in mark[:2] or s[i] in number:
                cal.append(s[i])
                i=i+1
            elif s[i]=="*":
                aft=cal[-1]
                bef=""
                j=i+1
                while j<len(s) and s[j] in number:
                    bef=bef+s[j]
                    j=j+1
                cal[-1]=str(int(aft)*int(bef))
                i=j
            elif s[i]=="/":
                aft=cal[-1]
                bef=""
                j=i+1
                while j<len(s) and s[j] in number:
                    bef=bef+s[j]
                    j=j+1
                cal[-1]=str(int(aft)//int(bef))
                i=j


        i = 1
        res=cal[0]
        while i < len(cal):
            if cal[i]=="+":
                res=str(int(res)+int(cal[i+1]))
            elif cal[i]=="-":
                res = str(int(res) - int(cal[i + 1]))
            i = i + 1

        return int(res)

