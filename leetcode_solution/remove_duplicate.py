class Solution:
    @staticmethod
    def removeDuplicates(nums : list[int]) -> int:
        current = 0
        last = None
        for i in nums:
            if i == last: continue  # noqa: E701
            nums[current] = i
            last = i
            current += 1
        return current

print(Solution.removeDuplicates([-1,0,0,0,0,3,3]))
