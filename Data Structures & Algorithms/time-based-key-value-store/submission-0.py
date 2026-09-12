class TimeMap:

    def __init__(self):
        self.store = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        tuples = self.store[key] # we grab the list of tuples at store[key]
        j = 0
        k = len(tuples) - 1
        res = ""

        while j <= k:
            mid = (j + k) // 2
            
                # we return touple at index 3,
                # and inside the touple we grab index 0 
                # (first value of the touple which is the word at that timestamp)

            if tuples[mid][1] <= timestamp:
                res = tuples[mid][0] 
                j = mid + 1
            else:
                k = mid - 1
        return res
        
