import sys
def maxArea(height):
    i = 0
    j = len(height) - 1
    max_area = 0

    while i <= j:
        max_area = max(max_area, (j - i) * min(height[i], height[j]))
        if height[i] >= height[j]:
            j = j - 1
        else:
            i = i + 1

    return max_area

if __name__=="__main__":
    height=sys.stdin.readline().strip()
    height=height.split(" ")
    height=[int(x)for x in height]
    
    print(maxArea(height))


