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
        # 每一轮排序找出未排序部分最小的值放在已排序部分的最后一位
        for i in range(0, len(arr4)-1):
            min_index = i
            for j in range(i+1, len(arr4)):
                if arr4[min_index] > arr4[j]:
                    min_index = j
            arr4[i], arr4[min_index] = arr4[min_index], arr4[i]
        arr3.extend(arr4)
        return arr3