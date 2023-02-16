class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def insertion_sort_k(array, k):
            for i in range(k, len(array)):
                j = i
                key = array[j]
                while (j - k >= 0) and (array[j - k] > key):
                    array[j] = array[j - k]
                    j -= k
                array[j] = key
            return array

        def hir(arr):
            i = size = len(arr)
            if size == 1:
                if arr[0]:
                    return 1
                return 0
            while (i - 1) and arr[i - 1] >= size - i + 1:
                if arr[i - 1] == size - i + 1:
                    return size - i + 1
                i -= 1
            if i == 1 and arr[0] >= size:
                return size
            return size - i

        k_seq, num = [], 1
        while num <= (len(citations) // 2):
            k_seq.append(num)
            num = (num * 3) + 1

        for i in k_seq[::-1]:
            insertion_sort_k(citations, i)

        return hir(citations)