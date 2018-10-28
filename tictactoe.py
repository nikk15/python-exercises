from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('     |     |     ')
    print('  '+board[1]+'  |  '+board[2]+'  |  '+board[3]+'  ')
    print('     |     |    ')
    print('-----------------')
    print('     |     |     ')
    print('  '+board[4]+'  |  '+board[5]+'  |  '+board[6]+'  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ') 
    print('  '+board[7]+'  |  '+board[8]+'  |  '+board[9]+'  ')
    print('     |     |     ')

def player_input():
    marker = ' '
    while marker != 'X' and marker != 'O':
        marker = (input('Player 1, choose X or 0: ')).upper()
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)

def place_marker(board, marker, position):
    for num in board:
        board[position]=marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return ' ' in board[position]

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        try:
            position = int(input('Where would you like to go? Choose a number, 1-9: '))
        except ValueError: 
            print("Not a position! Try again.")
            continue 
    return position

def replay():
    return input('Would you like to play again? Yes or No: ').lower().startswith('y')
    
#####################

def tic_tac_toe(): 
    
    print('Welcome to Tic Tac Toe!')
    
    while True: 
        #Sets/Resets game
        board = [' ']*10
        player1_mark, player2_mark = player_input()
        turn = choose_first()
        print(turn + ', you\'re up!')

        #while not win_check(board, mark) and not full_board_check(board):
            
        play_game = input('Ready, ' + turn + '? Enter Yes or No.')
            
        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:

            display_board(board)

            #Player 1's Turn
            if turn == 'Player 1':
                print(turn)
                position = player_choice(board)
                place_marker(board, player1_mark, position)
                if win_check(board, player1_mark):
                    display_board(board)
                    print('Congratulations, ' + turn)
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print("TIE!!!")
                        break
                    else:
                            turn = 'Player 2'
                
            #Player 2's Turn
            else:
                print(turn)
                position = player_choice(board)
                place_marker(board, player2_mark, position)
                if win_check(board, player2_mark):
                    display_board(board)
                    print('Congratulations, ' + turn)
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print("TIE!!!")
                        break
                    else:
                            turn = 'Player 1'

        if not replay():
            break
                
