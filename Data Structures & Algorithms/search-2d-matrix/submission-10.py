class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        out_l, out_r = 0, (len(matrix)-1)
        n = len(matrix[0])
        while out_l <= out_r:
            out_m = out_l + (out_r-out_l)//2

            if target < matrix[out_m][0]:
                out_r = out_m - 1
            elif target > matrix[out_m][-1]:
                out_l = out_m + 1
            elif target >= matrix[out_m][0] and target <= matrix[out_m][-1]:
                in_l, in_r = 0, (n-1)
                while in_l <= in_r:
                    in_m = in_l + (in_r-in_l)//2
                    if target < matrix[out_m][in_m]:
                        in_r = in_m - 1
                    elif target > matrix[out_m][in_m]:
                        in_l = in_m + 1
                    elif target == matrix[out_m][in_m]:
                        return True
                break
        return False
                