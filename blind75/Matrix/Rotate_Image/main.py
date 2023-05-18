class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = cols = len(matrix)
        # 先對矩陣進行轉置（行列互換）
        for i in range(rows):
            for j in range(i+1, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 對每一行進行反轉
        for i in range(rows):
            matrix[i] = matrix[i][::-1]

        return matrix