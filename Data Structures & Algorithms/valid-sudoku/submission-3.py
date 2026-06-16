import collections
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        square = {}
        rows = collections.defaultdict(set) #defaultDict
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)


        #loop through the matrix
        for row in range(9):
            for col in range(9):

                if board[row][col] == ".":
                    continue
                
                if (board[row][col] in rows[row] or board[row][col] in cols[col] 
                or board[row][col] in square[(row//3,col//3)]):
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                square[(row//3,col//3)].add(board[row][col])
                
        return True