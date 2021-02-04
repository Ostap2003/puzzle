""" 
Module that checks if the board is valid or not
repo on Github: https://github.com/Ostap2003/puzzle
"""


def check_rows(board: list) -> bool:
    """
    Checks if ther are no duplicates in each row of the board.
    """
    for row in range(len(board)):
        row_nums = set()
        for el in board[row]:
            try:
                if isinstance(int(el), int):
                    if int(el) in row_nums:
                        return False
                    else:
                        row_nums.add(int(el))
            except ValueError:
                pass

    return True


def check_cols(board: list) -> bool:
    """
    Checks if there are no duplicates in the board's columns.
    """
    for col in range(len(board)):
        col_nums = set()
        for row in range(len(board)):
            try:
                if isinstance(int(board[row][col]), int):
                    if int(board[row][col]) in col_nums:
                        return False
                    else:
                        col_nums.add(int(board[row][col]))
            except ValueError:
                pass

    return True


def check_same_color_area(board: list) -> bool:
    """
    Checks the same colored areas in the board for duplicates.
    """
    cursor = 0
    for col in range(len(board)):
        color_area = []

        for row in range(len(board)):
            color_area.append(board[row][col])

        cursor += 1
        # don't count entire column, only same colored areas
        color_area = color_area[:-(cursor)]
        color_area.extend(board[-(col + 1)][cursor - 1:])

        if len(color_area) < 9:
            break

        # print(color_area)

        col_area_num_entry = set()  # to check the nums entries
        for el in color_area:
            try:
                if isinstance(int(el), int):
                    if int(el) in col_area_num_entry:
                        return False
                    else:
                        col_area_num_entry.add(int(el))
            except ValueError:
                pass

    return True


def validate(board: list) -> bool:
    """
    Main functrion of the module.
    Recieves board and checks if it is a valid one or not with
    the help of other functions.
    """
    if check_rows(board):
        if check_cols(board):
            if check_same_color_area(board):
                return True

    return False
