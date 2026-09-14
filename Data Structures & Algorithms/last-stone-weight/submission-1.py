class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        max_heap = stones
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            if x == y:
                continue
            elif x < y:
                y = y - x
                heapq.heappush(max_heap, -y)
            else:
                x = x - y
                heapq.heappush(max_heap, -x)

        if len(max_heap) < 1:
            return 0
        return -heapq.heappop(max_heap)
        
    
[-6, -4, -3, -2, -2]

# we keep a max heap of the stones 
# (by simply reversing the heap values and reverting back when grabbing/viewing them)
# (while processing, literally everything remains negative so that pop and push operations can work in reverse)
# (we only need to revert back to + when returning)
# (or for processing we can revert then negate again when putting them back)
# (so we don't have to do logic in reverse)
# we pop last and assign it to x
# we pop last and assign it to y
# if x == y: we skip
# if x < y: y = y - x 
# and pushback y
# else (y < x): x = x - y, pushback x (reverse scenario)

# we put all this in a while heap > 1,
# to repeat the process until one stone is repeated
# after while, we return that value