class Solution:
    def containsDuplicate(self, nums):
        """
        Check if array contains any duplicates using hash set.
        
        Args:
            nums: List[int] - array of integers
        
        Returns:
            bool - True if duplicates exist, False otherwise
        """
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        [1, 2, 3, 1],           # Expected: True
        [1, 2, 3, 4],           # Expected: False
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],  # Expected: True
    ]
    
    for i, nums in enumerate(test_cases):
        result = solution.containsDuplicate(nums)
        print(f"Test case {i + 1}: {nums} -> {result}")