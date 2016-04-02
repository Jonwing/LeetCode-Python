Move Zeroes
===

Given an array `nums`, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.


For example, given `nums = [0, 1, 0, 3, 12]`, after calling your function, nums should be `[1, 3, 12, 0, 0]`.


**Note:**


You must do this **in-place** without making a copy of the array.
Minimize the total number of operations.

---

思路： 把所有非零的数前移。

遍历数组，遇到非零的数字时，将它移动到已前置的数字后面（游标指示，每前移一次游标+1），整个数组遍历完后，将游标到数组末端的所有位置置零。