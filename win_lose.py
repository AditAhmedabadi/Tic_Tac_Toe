def win_lose(theBoard, turn, count,game_over):
    if theBoard['a1'] == theBoard['a2'] == theBoard['a3'] != ' ':
        print('\n*********GAME OVER*********')
        print('Player', turn, 'WON')
        print('♪┏(・o･)┛♪┗ ( ･o･) ┓♪')
        game_over=True
        print(" ")
    elif theBoard['b1'] == theBoard['b2'] == theBoard['b3'] != ' ':
        print('\n*********GAME OVER*********')
        print('Player', turn, 'WON')
        print('♪┏(・o･)┛♪┗ ( ･o･) ┓♪')
        game_over=True
        print(" ")
    elif theBoard['c1'] == theBoard['c2'] == theBoard['c3'] != ' ':
        print('\n*********GAME OVER*********')
        print('Player', turn, 'WON')
        print('♪┏(・o･)┛♪┗ ( ･o･) ┓♪')
        game_over=True
        print(" ")
    elif theBoard['c1'] == theBoard['b1'] == theBoard['a1'] != ' ':
        print('\n*********GAME OVER*********')
        print('Player', turn, 'WON')
        print('♪┏(・o･)┛♪┗ ( ･o･) ┓♪')
        game_over=True
        print(" ")
    elif theBoard['c2'] == theBoard['b2'] == theBoard['a2'] != ' ':
        print('\n*********GAME OVER*********')
        print('Player', turn, 'WON')
        print('♪┏(・o･)┛♪┗ ( ･o･) ┓♪')
        game_over=True
        print(" ")
    elif theBoard['c3'] == theBoard['b3'] == theBoard['a3'] != ' ':
        print('\n*********GAME OVER*********')
        print('Player', turn, 'WON')
        print('♪┏(・o･)┛♪┗ ( ･o･) ┓♪')
        game_over=True
        print(" ")
    elif theBoard['c1'] == theBoard['b2'] == theBoard['a3'] != ' ':
        print('*********GAME OVER*********')
        print('♪┏(・o･)┛♪┗ ( ･o･) ┓♪')
        print('Player', turn, 'WON')
        game_over=True
        print(" ")
    elif theBoard['a1'] == theBoard['b2'] == theBoard['c3'] != ' ':
        print('*********GAME OVER*********')
        print('Player', turn, 'WON')
        print('♪┏(・o･)┛♪┗ ( ･o･) ┓♪')
        game_over=True

    if count == 9:
        print("************IT'S A TIE************")
        game_over=True
