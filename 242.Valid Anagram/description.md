Valid Anagram
===

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,

s = "anagram", t = "nagaram", return true.

s = "rat", t = "car", return false.

**Note:**

You may assume the string contains only lowercase alphabets.

**Follow up:**

What if the inputs contain unicode characters? How would you adapt your solution to such case?

---

1、用一个字典记录每个字母出现的次数，然后对比俩字典。

2、第二个方法是用一个字典，记录一串字符串中字符的次数，在第二串字符串中这些字符串存在的话减去相应的次数，到最后如果字典里所有值都是0, 则两个字符串是同构字符串。

~~之前想次数到0之后pop出，根据是不是空字典来判断是不是同构，然而执行速度上不比前者快~~