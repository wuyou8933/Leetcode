class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        sz, n = 0, len(matrix) and len(matrix[0])
        h = [0] * (n+1)
        for row in matrix:
            for i in range(n):
                h[i] = h[i] + 1 if row[i] == '1' else 0
            w = [-1]
            for j in range(n+1):
                while h[j] < h[w[-1]]:
                    height = h[w.pop()]
                    sz = max(sz, height * (j-1-w[-1]))
                w.append(j)
        return sz