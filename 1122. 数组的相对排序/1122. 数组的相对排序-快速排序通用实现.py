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
        def quick_sort(arr, low ,high):
            if low < high:
                pivot_index = partition(arr, low, high)
                quick_sort(arr, low, pivot_index-1)
                quick_sort(arr, pivot_index+1, high)
        def partition(arr, low, high):
            pivot = arr[low]
            left = low + 1
            right = high
            while left <= right:
                while left <= right and arr[left] <= pivot:
                    left += 1
                while left <= right and arr[right] >= pivot:
                    right -= 1
                if left <= right:
                    arr[left], arr[right] = arr[right], arr[left]
            arr[low], arr[right] = arr[right], arr[low]
            return right
        quick_sort(arr4, 0, len(arr4)-1)
        arr3.extend(arr4)
        return arr3