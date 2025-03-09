
def twoSum( nums: list[int], target: int) -> list[int]:

    i = 0
    a = dict()
    for n in nums:

        if n in a :
            return [a[n], i]
        else:
            a[target-n] = i

        i = i + 1

    return list()

print(twoSum([1,2,3,4],5))