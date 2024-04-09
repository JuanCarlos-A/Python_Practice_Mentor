class Solution:
    @staticmethod
    def removeDuplicates(nums : list[int]) -> int:
        num_list = list(set(nums))
        num_list.sort()
        for i in range(len(num_list)):
            nums[i] = num_list[i]
        return len(num_list)

print(Solution.removeDuplicates([-1,0,0,0,0,3,3]))
