class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict = defaultdict(set)
        colDict = defaultdict(set)
        squareDict = defaultdict(set)

        for row in range(len(board[0])):
            for col in range(len(board)):
                if (board[row][col] in rowDict[row]) or (board[row][col] in colDict[col]) or (board[row][col] in squareDict[(row//3,col//3)]):
                    return False
                elif board[row][col] != '.':
                    squareDict[(row//3,col//3)].add(board[row][col])
                    rowDict[row].add(board[row][col])
                    colDict[col].add(board[row][col])
        
        return True