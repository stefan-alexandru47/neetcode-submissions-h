class Solution:
    def search(self, nums: List[int], target: int) -> int:
        j = 0
        k = len(nums) - 1

        while j < k:
            mid = (k + j) // 2

            if nums[mid] > nums[k]:
                j = mid + 1
            else: 
                k = mid
        n = j

        j, k = n, len(nums) - 1 + n # 4 & 9
        print(j, k)
        
        if k >= len(nums):
            while j <= k:
                mid = (k + j) // 2 # 6
                print("Mid: " + str(mid))
                if nums[mid - len(nums)] == target:
                    print("Num at mid - length == target: " + str(mid - len(nums)))
                    if mid >= len(nums):
                        return mid - len(nums)
                    else:
                        return mid
                if nums[mid - len(nums)] > target:
                    k = mid - 1
                    print("k = Mid - 1: " + str(k))
                else:
                    j = mid + 1
                    print("j = Mid + 1: " + str(j))
        else:
            while j <= k:
                mid = (k + j) // 2
            #    print(str(j) + ' ' + str(k))
                if nums[mid + n] == target:
                    return mid + n
                if nums[mid + n] > target:
                    k = mid - 1
                else:
                    j = mid + 1
        return -1




        
'''
algorithm that detects cutoff 
and treats the array as if it starts and ends at cutoff
it could be done by offsetting nums[i] by doing nums[i + n]

[3,4,5,6,1,2]

if min at index 4, n = 4, so if we want to access index 2, 
we have to access index 6 to get the correct value instead,
so we do nums[i + 4]

for numbers where i + 4 >= len(nums), we instead do :

i + 4 - len(nums)
'''