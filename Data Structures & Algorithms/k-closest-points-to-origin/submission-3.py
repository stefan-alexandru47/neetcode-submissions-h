class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def pythagoras(x, y):
            return math.sqrt(pow(x, 2) + pow(y, 2))

        min_heap = []

        for pair in points:
            distance = pythagoras(pair[0], pair[1])
            min_heap.append( (distance, [pair[0], pair[1]]) )
        heapq.heapify(min_heap)

        res = []
        while len(res) < k:
            res.append(heapq.heappop(min_heap)[1])

        return res

# to get distance between a point and origin, do pythagoras
# to keep distances ordered, we need to have pairs of distance & 2points
# to implement this, we can have a min-heap where we keep distances
# whenever adding a distance to the mean-heap, we also add it to a hashmap as key, with its 2points as value
# then we just find kth closest distance, and return its value from the hashmap