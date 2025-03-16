# Function to reverse every sub-array group of size k.

class Solution:
    # Function to reverse every sub-array group of size k.
    def reverse(self, arr, start, end):
        while start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1
            end -= 1
        print(arr)

    def reverse_in_Groups(self, arr, k):

        start = 0
        end = start + (k - 1)

        while end < len(arr)-1:
            self.reverse(arr, start, end)
            start = end+1
            end = start + (k - 1)

        if start < end:
           self.reverse(arr, start, len(arr) - 1)
        print(arr)

print(Solution().reverse_in_Groups([1,2,3,4,5],3))

print(Solution().reverse_in_Groups([1,2,3,4,5],2))