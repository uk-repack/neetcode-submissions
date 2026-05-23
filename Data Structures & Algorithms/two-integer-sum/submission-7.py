class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        my_map = {}

        for i, n in enumerate(nums):
            my_map[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in my_map and my_map[diff] != i:
                return [i, my_map[diff]]
        return []
      
   