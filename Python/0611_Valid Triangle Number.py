#Brute Force
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] != 0:
                k = i + 2
                for j in range(i+1, len(nums)-1):
                    while k < len(nums) and nums[i] + nums[j] > nums[k]:
                        k += 1
                    res += k-j-1
        return res

#Linear Scan by sorting
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] != 0:
                k = i + 2
                for j in range(i+1, len(nums)-1):
                    while k < len(nums) and nums[i] + nums[j] > nums[k]:
                        k += 1
                    res += k-j-1
        return res
