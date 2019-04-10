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