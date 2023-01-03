"""
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true


Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

solution leet code
https://leetcode.com/problems/isomorphic-strings/solutions/1261227/isomorphic-strings/?envType=study-plan&id=level-1

"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        character_mapping_dict = {}
        for s_char, t_char in zip(s, t):
            existing_char = character_mapping_dict.get(s_char,None)
            if existing_char is None and t_char not in character_mapping_dict.values():
                character_mapping_dict[s_char] = t_char
            elif existing_char != t_char:
                return False
        return True


if __name__ == '__main__':
    s = Solution()

    print(s.isIsomorphic("foo", "bar"))
    print(s.isIsomorphic("paper", "title"))