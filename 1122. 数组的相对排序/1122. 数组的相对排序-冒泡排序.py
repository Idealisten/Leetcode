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
        for i in range(len(arr4)-1):
            for j in range(i+1, len(arr4)):
                if arr4[i] > arr4[j]:
                    arr4[i], arr4[j] = arr4[j], arr4[i]
        arr3.extend(arr4)
        return arr3