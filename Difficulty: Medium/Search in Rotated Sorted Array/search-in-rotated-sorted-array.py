class Solution:
    def search(self, arr, target):
        # code here
        i = 0
        j = len(arr)-1
        
        while i<=j:
            mid = (i+j)//2
            if arr[mid]==target:
                return mid
            elif arr[i] <= arr[mid]:
                #left half is sorted
                if arr[i]<=target<arr[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                #right half is sorted
                if arr[mid]<target<=arr[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        return -1