
import win_lose

def clear_board(board):
    for i in board:
        board[i] = " "

# declaring and initializing variables
board = {'a1': ' ', 'a2': ' ', 'a3': ' ',
         'b1': ' ', 'b2': ' ', 'b3': ' ',
         'c1': ' ', 'c2': ' ', 'c3': ' ', }
turn = 'X'
count = 0
game_over=False

print("WELCOME TO TIC TAC TOE, 2 PLAYER GAME")

while(True):
    print(board['a1'] + '  | ' + board['a2'] + ' |  ' + board['a3'])
    print('---+---+---')
    print(board['b1'] + '  | ' + board['b2'] + ' |  ' + board['b3'])
    print('---+---+---')
    print(board['c1'] + '  | ' + board['c2'] + ' | ' + board['c3'])
    print("ITS ", turn + "s turn, please select a place where u want to place it")
    move = input("select coordinates-->")
    if board[move] == ' ':
        board[move] =turn
        count += 1
    else:
        print("\nThat place already has been taken please select another one")
        continue
    win_lose.win_lose(board, turn, count,game_over)
    if turn == 'X':
        turn = 'O'
    elif turn == 'O':
        turn = 'X'
    else:
        print("error")
    if game_over==True:
        display_board.clear_board(board)
        restart=input("\n\nDO YOU WANT TO RESTART? (Y/N)")
        if restart=='Y' or restart=='y':
            print("initializing game again....")
            clear_board(board)
            count=0
            continue
        elif restart == 'N' or restart == 'n':
            print("\n\nQUITTING THE GAME....")
            break
        else:
            print("eror")
print("\nTHANK YOU FOR PLAYING")
if __name__ == "__main__":
    print("MAIN")
