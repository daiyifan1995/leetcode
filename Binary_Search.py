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

    print(searchRange([5,7,7,8,8,10],11))
