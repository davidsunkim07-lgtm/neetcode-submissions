class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict = defaultdict(list)
        colDict = defaultdict(list)
        squareDict = defaultdict(list)

        for row in range(len(board[0])):
            for col in range(len(board)):
                if (board[row][col] in rowDict[row]) or (board[row][col] in colDict[col]) or (board[row][col] in squareDict[(row//3,col//3)]):
                    return False
                elif board[row][col] != '.':
                    squareDict[(row//3,col//3)].append(board[row][col])
                    rowDict[row].append(board[row][col])
                    colDict[col].append(board[row][col])
        
        return True