class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 先用二分法（双指针）拿到中间一个nums[left]=num[mid]
        l = len(nums)
        left = 0
        right = l - 1
        mid = -1
        # 特殊情况nums=[],时间复杂度O(1)
        if not nums:
            return([-1, -1])
            exit()
        # 二分法，时间复杂度O(logn)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid
                break
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        # 如果targe不在数组中，时间复杂度O(1)
        if nums[mid] != target:
            return([-1, -1])
            exit()
        # 将左右指针外延，时间复杂度O(1)
        while nums[left] == target:
            left -= 1
            if left < 0:
                break
        right = mid
        while nums[right] == target:
            right += 1
            if right > l-1:
                break
        return([left + 1, right - 1])
