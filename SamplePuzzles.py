"""
These the sample puzzles to be used with the two not touch solver

The data structure of these puzzles is divided into 2 parts:
-board: a list of lists containing the location of each numbered space
-sector: a list of lists containing which spaces belong to each sector

The data structure of a board is as follows: (let n be the width and m be the height of the board)
-board are designed as nXm rectangles
-each space on the board is uniquely numbered from 1 - (n * m)
-The boards are stored in 2 dimensional arrays with n lists containing m unique elements

This is a sample 4X4 board with square numbers 1 - 16: """
board = [[1,   2,  3,  4],
         [5,   6,  7,  8],
         [9,  10, 11, 12],
         [13, 14, 15, 16]]

"""
The data structure of the sectors is as follows:
-sectors are a list of lists
-each list contains a set of integers which correspond to the numberings used on the board
-a space belongs to the sector which contains its number

This is a sample sector list for the 4x4 board above: """
sectors = [[1, 2, 5, 6],
           [3, 4, 7],
           [8, 9, 10, 11, 12],
           [13, 14, 15, 16]]

""""""


# a satisfiable 8X8 puzzle
puzzle1 = {
    "board": [[x for x in range(1, 9)],
              [x for x in range(9, 9 + 8)],
              [x for x in range(8 * 2 + 1, 8 * 2 + 1 + 8)],
              [x for x in range(8 * 3 + 1, 8 * 3 + 1 + 8)],
              [x for x in range(8 * 4 + 1, 8 * 4 + 1 + 8)],
              [x for x in range(8 * 5 + 1, 8 * 5 + 1 + 8)],
              [x for x in range(8 * 6 + 1, 8 * 6 + 1 + 8)],
              [x for x in range(8 * 7 + 1, 8 * 7 + 1 + 8)]],

    "sectors": [[x for x in range(1, 9)],
                [x for x in range(9, 9 + 8)],
                [x for x in range(8 * 2 + 1, 8 * 2 + 1 + 8)],
                [x for x in range(8 * 3 + 1, 8 * 3 + 1 + 8)],
                [x for x in range(8 * 4 + 1, 8 * 4 + 1 + 8)],
                [x for x in range(8 * 5 + 1, 8 * 5 + 1 + 8)],
                [x for x in range(8 * 6 + 1, 8 * 6 + 1 + 8)],
                [x for x in range(8 * 7 + 1, 8 * 7 + 1 + 8)]]
}

# a satisfiable 8X8 puzzle
puzzle2 = {
    "board": [[x for x in range(1, 9)],
              [x for x in range(9, 9 + 8)],
              [x for x in range(8 * 2 + 1, 8 * 2 + 1 + 8)],
              [x for x in range(8 * 3 + 1, 8 * 3 + 1 + 8)],
              [x for x in range(8 * 4 + 1, 8 * 4 + 1 + 8)],
              [x for x in range(8 * 5 + 1, 8 * 5 + 1 + 8)],
              [x for x in range(8 * 6 + 1, 8 * 6 + 1 + 8)],
              [x for x in range(8 * 7 + 1, 8 * 7 + 1 + 8)]],

    "sectors": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 18],
                [13, 14, 15, 16],
                [17, 19, 25, 26, 27, 28],
                [20, 21, 22, 23, 24, 29, 30, 31, 32],
                [41, 42, 43, 44, 45, 46, 47, 48, 49],
                [50, 51, 52],
                [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64],
                [33, 34, 35, 36, 37, 38, 39, 40]]
}

# an unsatisfiable 8X8 puzzle
unsatisfiable_puzzle = {
    "board": [[x for x in range(1, 9)],
              [x for x in range(9, 9 + 8)],
              [x for x in range(8 * 2 + 1, 8 * 2 + 1 + 8)],
              [x for x in range(8 * 3 + 1, 8 * 3 + 1 + 8)],
              [x for x in range(8 * 4 + 1, 8 * 4 + 1 + 8)],
              [x for x in range(8 * 5 + 1, 8 * 5 + 1 + 8)],
              [x for x in range(8 * 6 + 1, 8 * 6 + 1 + 8)],
              [x for x in range(8 * 7 + 1, 8 * 7 + 1 + 8)]],

    "sectors": [[1,  2,  3,  4,  5, 9,  10, 11, 12, 17, 18, 19, 27, 35],
                [6,  7,  8, 13, 14, 15, 16, 20, 21],
                [25, 26, 33, 34, 42, 43, 50, 51, 52, 58, 59, 60],
                [28, 29, 36, 44],
                [22, 23, 24, 30, 37, 38, 39, 40, 45, 46, 47, 48, 56, 63, 64],
                [41, 49, 57],
                [53, 54, 55, 61, 62]]
}