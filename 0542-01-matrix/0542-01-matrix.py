class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = []
        rows = len(mat) - 1
        cols = len(mat[0]) - 1
        
        if rows <= 0 and cols <= 0:
            return mat
        
        for i in range(rows + 1):
            for j in range(cols + 1):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = None
        
        while queue:
            row, col = queue.pop(0)
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                d_r = row + x
                d_c = col + y
                if 0 <= d_r <= rows and 0 <= d_c <= cols and mat[d_r][d_c] is None:
                    mat[d_r][d_c] = mat[row][col] + 1
                    queue.append((d_r, d_c))
        
        return mat
