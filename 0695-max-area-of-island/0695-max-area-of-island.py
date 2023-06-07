class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #get dimensions of grid
        rows = len(grid)
        cols = len(grid[0])
        #initialize visited hash set
        visited= set()
        
        #dfs algorithm
        def dfs(row, col):
            #base case
            #if out of bound or if water or if row/col is visited 
            if (row <0 or row == rows or col<0 or col == cols or grid[row][col] == 0 or (row, col) in visited):
                return 0
            #add row, col to visited set
            visited.add((row, col))
            #calculate area : 1 for current cell + all 4-4 connected island cells
            return (1+ dfs(row+1, col)+ dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1))
        
        #loop over all grid
        #initialize area
        area=0
        for row in range(rows):
            for col in range(cols):
                #get maximum area
                area = max(area, dfs(row, col))
        return area
        
                