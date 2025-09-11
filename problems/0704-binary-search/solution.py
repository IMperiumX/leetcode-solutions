class Solution:
    def search(self, nums, target):
        """
        Binary search in a sorted array.
        
        Args:
            nums: List[int] - sorted array of integers
            target: int - target value to search for
        
        Returns:
            int - index of target if found, -1 otherwise
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Calculate mid to avoid overflow
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9),    # Expected: 4
        ([-1, 0, 3, 5, 9, 12], 2),    # Expected: -1
        ([5], 5),                      # Expected: 0
        ([5], -5),                     # Expected: -1
        ([2, 5, 8, 12, 16, 23, 38, 45, 67, 78, 88, 92, 96, 99], 23),  # Expected: 5
    ]
    
    for i, (nums, target) in enumerate(test_cases):
        result = solution.search(nums, target)
        print(f"Test case {i + 1}: nums={nums}, target={target} -> {result}")