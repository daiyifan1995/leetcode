class Solution:
    def searchRange(self,nums,target):
        length = len(nums)
        if length == 0 :
            return [-1, -1]
        if length==1 and nums[0]!=target:
            return [-1,-1]
        left=0
        right=len(nums)-1
        return self.check_equal(nums, left, right, target)

    def check_equal(self,nums,left,right,target):
        split_point=int((left+right)/2)
        if nums[split_point]<target:
            left=split_point+1
        elif nums[split_point]>target:
            right = split_point - 1
        elif nums[split_point]==target:
            #return split_point
            s,e=split_point,split_point
            while s>=0:
                if nums[s]==target:
                    s-=1
                else:
                    break
            while e<len(nums):
                if nums[e]==target :
                    e+=1
                else:
                    break
            return [s+1,e-1]
        if left<=right and left>=0 and right<len(nums):
            print(left, right, split_point)
            return self.check_equal(nums, left, right, target)
        else:
            #return -1
            return [-1,-1]





def binary_search_in_2(nums,target):
    global row,col
    while row<len(nums) and col >=0:
        print(row,col)
        res=check(nums, target)
        if res!=None:
            return res
    while row < len(nums):
        if nums[row][col] > target:
            return -1
        res=check(nums,target)
        if res!=None:
            return res
    while col >=0:
        if nums[row][col] < target:
            return -1
        res=check(nums,target)
        if res!=None:
            return res
    return -1

def check(nums,target):
    global row, col
    if nums[row][col] > target:
        col -= 1
    elif nums[row][col] < target:
        row += 1
    else:
        return (row, col)


if __name__=="__main__":
    nums=nums=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    row=0
    col=len(nums[0])-1
    print(binary_search_in_2(nums, 7))


