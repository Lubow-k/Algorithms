"""
This solution failed test 222 with Time Limit Exceeded error :(
The solution of Task_8 in C is correct!
"""

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        def merge_inv(array, s, m, e, buf):
            i, j = s, m + 1
            k = s
            counter = 0
            while i <= m and j <= e:
                if array[i] <= array[j]:
                    buf[k] = array[i]
                    i += 1
                else:
                    buf[k] = array[j]
                    counter += m - i + 1
                    j += 1
                k += 1

            while i <= m:
                buf[k] = array[i]
                k += 1
                i += 1
            while j <= e:
                buf[k] = array[j]
                k += 1
                j += 1
            return counter

        def merge_sort_inv(array, s, e, buffer):
            if s == e:
                return 0
            if e - s == 1:
                if array[e] < array[s]:
                    array[e], array[s] = array[s], array[e]
                    return 1
                return 0
            elif s < e:
                m = (s + e) // 2
                left = merge_sort_inv(array, s, m, buffer)
                right = merge_sort_inv(array, m + 1, e, buffer)
                spl = merge_inv(array, s, m, e, buffer)

                for i in range(s, e + 1):
                    array[i] = buffer[i]
                return left + right + spl

        def count_inv(array):
            buf = [0] * len(array)
            return merge_sort_inv(array, 0, len(array) - 1, buf)

        count_loc = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count_loc += 1

        return count_inv(nums) == count_loc
