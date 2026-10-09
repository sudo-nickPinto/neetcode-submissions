class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for elem in nums:
            if elem in unique:
                return True
            else:
                 unique.add(elem)

        return False