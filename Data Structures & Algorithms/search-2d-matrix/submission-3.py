class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_list = 0
        end_list = len(matrix) - 1
        row = 0

        while start_list <= end_list: # this while loop should find which row target resides in
            middle_list = (start_list + end_list) // 2

            if target <= matrix[middle_list][-1] and target >= matrix[middle_list][0]:
                row = middle_list
                break
            elif target <= matrix[middle_list][-1]:
                end_list = middle_list - 1
            else:
                start_list = middle_list + 1

        start, end = 0, len(matrix[row]) - 1
        mid_value = 0

        while start <= end:
            mid = (start + end) // 2
            mid_value = matrix[row][mid]

            if target == mid_value:
                return True
            elif target < mid_value:
                end = mid - 1
            else:
                start = mid + 1
        
        return False

# we first check if target < or > [len(matrix) // 2][0] (the beginning or end of middle list)
# if target > [len(matrix) // 2][]
# since the first integer of every row > than the last integer of previous row