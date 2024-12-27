# String Manipulation Approach

class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.

        The encoding works by prefixing each string with its length followed by a delimiter.
        """
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.

        The decoding reads the length of the next string, followed by the string itself.
        """
        decoded_strings = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded_strings.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decoded_strings


# 271. Encode and Decode Strings - Length Prefix Approach

class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res
