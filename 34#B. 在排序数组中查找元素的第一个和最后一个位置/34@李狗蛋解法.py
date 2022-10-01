class Solution:

    # 寻找左边界
    def leftMargin(self, nums: List[int], target: int):

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            # 如果 nums[mid] = target，继续向左寻找左边界
            if nums[mid] == target:
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if nums[low] == target:
            return low
        # 如果左边界的值不等于 target
        else:
            return -1

    # 寻找右边界
    def rightMargin(self, nums: List[int], target: int):

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            # 如果 nums[mid] = traget，继续向右寻找右边界
            if nums[mid] == target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if nums[high] == target:
            return high
        # 如果右边界的值不等于 target
        else:
            return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0 or nums[0] > target or nums[-1] < target:
            return [-1,-1]

        lm = self.leftMargin(nums, target)
        rm = self.rightMargin(nums, target)

        return [lm,rm]

作者：rocky0429-2
链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/solution/acm-xuan-shou-tu-jie-leetcode-zai-pai-xu-yz1m/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。