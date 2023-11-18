class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3 = []
        arr4 = []
        for item2 in arr2:
            for i, item1 in enumerate(arr1):
                if item1 == item2:
                    arr3.append(item1)
                if item1 not in arr2:
                    del arr1[i]
                    arr4.append(item1)
        # arr4.sort()
        # 快速排序
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quick_sort(left) + middle + quick_sort(right)
        arr4 = quick_sort(arr4)
        arr3.extend(arr4)
        return arr3