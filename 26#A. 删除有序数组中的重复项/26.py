class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 双指针解法
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[slow]<nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            else:
                fast += 1
        return slow+1
