class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        Check if ransom note can be constructed from magazine letters.
        
        Args:
            ransomNote: str - the ransom note to construct
            magazine: str - available letters to use
        
        Returns:
            bool - True if ransom note can be constructed, False otherwise
        """
        # Count characters in magazine
        char_count = {}
        for char in magazine:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Check if ransom note can be constructed
        for char in ransomNote:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1
        
        return True


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("a", "b"),         # Expected: False
        ("aa", "ab"),       # Expected: False
        ("aa", "aab"),      # Expected: True
        ("aab", "baa"),     # Expected: True
        ("aaa", "aa"),      # Expected: False
    ]
    
    for i, (ransom_note, magazine) in enumerate(test_cases):
        result = solution.canConstruct(ransom_note, magazine)
        print(f"Test case {i + 1}: ransomNote='{ransom_note}', magazine='{magazine}' -> {result}")