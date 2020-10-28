def print_the_board(the_board):
    print(the_board['a1'] + '  | ' + the_board['a2'] + ' |  ' + the_board['a3'])
    print('---+---+---')
    print(the_board['b1'] + '  | ' + the_board['b2'] + ' |  ' + the_board['b3'])
    print('---+---+---')
    print(the_board['c1'] + '  | ' + the_board['c2'] + ' | ' + the_board['c3'])


def clear_board(the_board):
    for i in the_board:
        the_board[i] = " "
