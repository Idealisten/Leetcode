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
        # 假设第一个元素是有序的，从第二个元素开始(i=1)，找出当前元素在有序部分的位置，然后插入；找出合适位置的方法是从当前元素的前一个元素(j=i-1)开始
        # （也就是已排序部分的结尾），如果元素i小于前一个元素j，则将前一个元素后移一位(arr4[j+1] = arr4[j])，然后接着比较再前面一个元素(j-1)，
        # 直到arr4[j] <= arr4[i]，则将元素i插入到arr4[j+1]的位置(arr4[j+1] = arr4[i])，这轮循环结束， i = i + 1，继续下一轮循环，直到i = len(arr4) - 1
        for i in range(1, len(arr4)):
            j = i - 1
            key = arr4[i]
            while j >= 0 and key < arr4[j]:
                arr4[j+1] = arr4[j]
                j = j -1
            arr4[j+1] = key
        arr3.extend(arr4)
        return arr3