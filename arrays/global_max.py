# User function Template for python3

def maxIndexDiff(arr):
    # code here

    left_min = []
    right_max = [None]* len(arr)

    curr_min = arr[0]

    for i in arr:
        if i < curr_min :
            curr_min = i

        left_min.append(curr_min)

    curr_max = arr[len(arr) - 1]
    for i in range(len(arr)):
        if arr[len(arr) -1 -i] > curr_max :
            curr_max = arr[len(arr) -1 -i]
        right_max[len(arr) -1 -i] = curr_max

    print(left_min,'\n',right_max)


    max_diff = 0
    i=0
    j=0
    while i < len(arr) and j < len(arr):

        if right_max[j] >= left_min[i] :
            max_diff = max(max_diff, j-i)
            j+=1
        else:
            i+=1
            if j < i:
                j+=1

    print(max_diff)

maxIndexDiff([4,2,6,1,5,3])

maxIndexDiff([2,2,1,1,1,1])

