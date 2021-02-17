class Chess:
    def __init__(self, maxRow, maxCol):
        self.maxCol = maxCol
        self.maxRow = maxRow
        self.board = [[0 for c in range(self.maxCol)] for r in range(self.maxRow)]
        self.queens = 0

    def placeQueen(self, row, col):
        self.board[row][col] = 'Q'

    def removeQueen(self, row, col):
        self.board[row][col] = 0

    def display(self):
        for row in range(self.maxRow):
            for col in range(self.maxCol):
                print(self.board[row][col], end = " ")
            print()

    def valid(self, row, col):
        # Check there is no other Queen in the same row
        if self.board[row][col] == 'Q':
            return False
        for j in range(col):
            if self.board[row][j] == 'Q':
                return False
        # Check there is no other Queen in the same column
        for i in range(row):
            if self.board[i][col] == 'Q':
                return False
        # Check there is no other Queen in the diagonals
        diagonalVectorRow = [-1, 1]
        diagonalVectorCol = [-1, -1]
        for i in range(2):
            currCol = col + diagonalVectorCol[i]
            currRow = row + diagonalVectorRow[i]
            while currRow >= 0 and currCol >= 0 and currRow < self.maxRow and currCol < self.maxCol:
                if self.board[currRow][currCol] == 'Q':
                    return False
                currCol += diagonalVectorCol[i] 
                currRow += diagonalVectorRow[i]

        return True
        
    def solve(self, col):
        if col >= self.maxCol:
            return True

        for i in range(self.maxRow):
            if self.valid(i, col):
                self.placeQueen(i, col)
                if self.solve(col + 1):
                    return True
                self.removeQueen(i, col)

        return False

        

board = Chess(8, 8)
board.display()
print(board.solve(0))
board.display()
