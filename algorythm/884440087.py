# https://leetcode.com/problems/build-array-from-permutation/description/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # ans[i] = nums[nums[i]]になる
        # ans = [nums[0], nums[2], nums[1], nums[5],
        # nums[3], nums[4]]
        # 問題文としては、ans[i] = nums[nums[i]]になるやつを作れと言っている。
        a = [nums[v] for i, v in enumerate(nums)]
        return a