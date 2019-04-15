import sys


# def cholate_num(n,a,b,c):
# #     buy_numbers=n//c
# #     if buy_numbers<a:
# #         return buy_numbers
# #     else:
# #         return buy_numbers+(buy_numbers//a)*b
# #
# # if __name__ == "__main__":
# #     line= sys.stdin.readline().strip().split(" ")
# #     array=[int(i) for i in line]
# #     if len(array)==4:
# #         n=array[0]
# #         a=array[1]
# #         b=array[2]
# #         c=array[3]
# #         print(cholate_num(n,a,b,c))


import sys

if __name__ == "__main__":
    n,w = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    arr = [int(x) for x in sys.stdin.readline().strip().split(" ")]

    arr = sorted(arr)
    girl_min = arr[0]
    boy_min = arr[n]
    count = boy_min / 2 if girl_min > boy_min / 2 else girl_min
    if n * (2 * count + count) <= w:
        print('%.6f' % (n * (2 * count + count)))
    else:
        print(w)