class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length_so_far = 0
        letters_in_window = set()

        for end in range(len(s)):
            if s[end] in letters_in_window:
                while s[start] != s[end]:
                    letters_in_window.remove(s[start])
                    start += 1
                letters_in_window.remove(s[start])
                start += 1
            letters_in_window.add(s[end])
            max_length_so_far = max(max_length_so_far, end - start + 1)

        return max_length_so_far
