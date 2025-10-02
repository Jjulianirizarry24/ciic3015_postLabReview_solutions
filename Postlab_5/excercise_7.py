def isPalindrome(word: str) -> bool:
    left = 0
    right = len(word) - 1
    
    while left < right:
        # If the characters at the current pointers don't match, it's not a palindrome
        if word[left] != word[right]:
            return False
        
        # Move the pointers closer to the center
        left += 1
        right -= 1
    
    return True