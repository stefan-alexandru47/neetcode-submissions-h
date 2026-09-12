class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        j = 1
        k = max(piles)
        # we wanna make sure we eat in the slowest time we're allowed to

        while j <= k:
            mid = (j + k) // 2
            hours = 0

            for num in piles:
                hours += math.ceil(num / mid)

            if hours <= h:
                k = mid - 1
            else: 
                j = mid + 1
        return j




# we do binary search on j through k 
# j .. k being smallest to largest eating speed
# you can set k to = h, but doing so is redundant,
# we want to go as slow as possible eating bananas
# we know the largest pile is the slowest we can go
# so k should be set to the maximum pile (4)
# then we need to check which out of 1 through 4 is the slowest we can possibly go
# binary search here is just an accessory to make the algorithm faster, not a requirement
# if t < h: j + 1 becomes mid, else k - 1 becomes mid (to look for a faster time if possible)
# so we check every eating speed against every pile in the array to ensure we don't spend more than 9 hours
# to check, we divide by speed, and round up to the next integer, which gives us the hours it takes
# we can do math.ceil(piles[i] / mid) mid being the speed we're trying



# we need to find the minimum eating rate so that we eat all bananas within time limit
# each i takes 1 hour per eating rate until you finish the bananas
# eating rate 2 at a pile of 4 = piles[i] // 2 
# do sum of piles
# if sum < h: upperbound = sum, else = h
# can you finish pile with 1? 
# no bcs pile is 10 and reaching 10 iterations goes over h
# can koko finish with 2?
# yes because you only do 5 iterations until you reach 10
# so you could check every number from 0 to -1 but that would take too long
# we do binary search 
# calculate how many 

# k = max(piles)
# j = 1
# do binary search to find the smallest possible k

