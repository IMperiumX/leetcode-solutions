# 271. Encode and Decode Strings, Difficulty: Medium

**Link:** [https://leetcode.com/problems/encode-and-decode-strings/](https://leetcode.com/problems/encode-and-decode-strings/)

## Problem Description

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

```cpp
string encode(vector<string> strs) {
// ... your code
return encoded_string;
}
```

Machine 2 (receiver) has the function:

```cpp
vector<string> decode(string s) {
//... your code
return strs;
}
```

So Machine 1 does:
`string encoded_string = encode(strs);`

and Machine 2 does:
`vector<string> strs2 = decode(encoded_string);`

`strs2` in Machine 2 should be the same as `strs` in Machine 1.

Implement the `encode` and `decode` methods.

**Note:**

* The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
* Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
* Do not rely on any library method such as `eval` or `serialize` methods. You should implement your own encode/decode algorithm.

## Solution Approach (Length Prefix)

The [`solution.py`](./solution.py) file contains a Python solution that uses a length prefix approach.

**Encode:**

* For each string in the input list, we prepend the length of the string followed by a '#' character.
* We concatenate all these modified strings to form the encoded string.

**Decode:**

* We iterate through the encoded string, reading the length prefix until we encounter the '#' character.
* We extract the substring of the specified length.
* We repeat this process to obtain all the original strings.
