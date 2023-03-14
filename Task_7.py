"""
Solution with buffer: Runtime 2060 ms, memory 21.7 MB
Solution without buffer: Runtime 3801 ms, memory 22.3 MB ... Why??
"""

class Solution_1:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(array, s, m, e, buf):
            i, j = s, m
            k = s
            while i < m and j < e:
                if array[i] <= array[j]:
                    buf[k] = array[i]
                    i += 1
                else:
                    buf[k] = array[j]
                    j += 1
                k += 1

            while i < m:
                buf[k] = array[i]
                k += 1
                i += 1
            while j < e:
                buf[k] = array[j]
                k += 1
                j += 1

        def merge_sort_buf(array, s, e, buffer):
            if e - s == 1:
                return
            if e - s == 2:
                if array[e - 1] < array[s]:
                    array[e - 1], array[s] = array[s], array[e - 1]
                return
            elif s < e:
                m = (s + e) // 2
                merge_sort_buf(array, s, m, buffer)
                merge_sort_buf(array, m, e, buffer)
                merge(array, s, m, e, buffer)

                for i in range(s, e):
                    array[i] = buffer[i]

        def merge_sort(array):
            buf = [0] * len(array)
            return merge_sort_buf(array, 0, len(array), buf)

        merge_sort(nums)
        return nums


class Solution_2:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(array, s_1, e_1, s_2, e_2, location):
            while s_1 < e_1 and s_2 < e_2:
                if array[s_1] <= array[s_2]:
                    array[location], array[s_1] = array[s_1], array[location]
                    s_1 += 1
                else:
                    array[location], array[s_2] = array[s_2], array[location]
                    s_2 += 1
                location += 1
            while s_1 < e_1:
                array[location], array[s_1] = array[s_1], array[location]
                s_1 += 1
                location += 1
            while s_2 < e_2:
                array[location], array[s_2] = array[s_2], array[location]
                s_2 += 1
                location += 1

        def m_sort(array, s, e, where):
            if (e - s) > 1:
                middle = s + (e - s) // 2
                smart_sort(array, s, middle)
                smart_sort(array, middle, e)
                merge(array, s, middle, middle, e, where)
            else:
                array[s], array[where] = array[where], array[s]  #one just swap

        def smart_sort(array, s, e):
            if (e - s) > 1:
                middle = s + (e - s) // 2
                w = s + e - middle #exactly half or one more on the right
                m_sort(array, s, middle, w)
                while w - s > 2:
                    old_w = w
                    w = s + (old_w - s + 1) // 2 #exactly half or one more on the left
                    m_sort(array, w, old_w, s)  #sort the middle to beginning
                    merge(array, s, s + old_w - w, old_w, e, w)

                #insert if there are less than 3 elements
                for i in range(w, s, -1):
                    j = i
                    key = array[i - 1]
                    while (j < e) and (array[j] < key):
                        array[j - 1] = array[j]
                        j += 1
                    array[j - 1] = key

        def merge_sort(array):
            smart_sort(array, 0, len(array))

        merge_sort(nums)
        return nums
