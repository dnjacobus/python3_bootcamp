from IPython.display import clear_output

import random

board = ['#',' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']

def display_board(board):
    
    clear_output()
    print(' ',board[7],'|',board[8],'|',board[9])
    print('----|---|----')
    print(' ',board[4],'|',board[5],'|',board[6])
    print('----|---|----')
    print(' ',board[1],'|',board[2],'|',board[3])

def player_input():
    
    marker = 'incorrect'
    
    while marker not in ['X','O']:
        
        marker = input('Which marker: X or O  ').upper()
        
        if marker not in ['X','O']:
            clear_output
            print('What chu doin? X or O')
            
    return marker

def place_marker(board, marker, position):
    
    board[position] = marker

def win_check(board, mark):
    #there has to be a for loop to do this
    
    #manual check rows:
    if board[7] == board[8]== board[9]== mark or board[4]== board[5]== board[6]== mark or board[1] == board[2]== board[3]== mark:
        return True
    #manual check columns
    elif board[7]== board[4]== board[1]== mark or board[8]== board[5]== board[2]== mark or board[9] == board[6]== board[3]== mark:
        return True
    #manual check cross
    elif board[7]== board[5]== board[3]== mark or board[9]== board[5]== board[1]== mark:
        return True
    else:
        return False

def choose_first():
    goes_first = random.randint(1,2)
    if goes_first == 1:
        return "Player X goes first."
    else:
        return 'Player O goes first.'

def space_check(board, position):
    '''
    when True, space is available
    ''' 
    return board[position] == " "

def full_board_check(board):
    '''
    when True, board is full
    '''
    return ' ' not in board

def player_choice_check():
    #default values
    choice = 'incorrect'
    board_range = range(1,10)
    within_range = False
    
    while choice.isdigit() == False or within_range == False:
        #Ask for input
        choice = input('Choose 1-9 to place marker: ')
            
        #Digit Ceck
        if choice.isdigit() == False:
            print(f'A number is needed! You put {choice}')
            
        #Range check
        if choice.isdigit() == True:
            if int(choice) in board_range:
                within_range = True
            else:
                within_range = False
                print(f'Not in range. Should be 1-9. You put {choice}')
    return int(choice)

def player_choice(board):

    #default values
    space = 'must check'

    #Loop to check for a space
    while space == 'must check':
        position = player_choice_check()
        #check if space is available
        if space_check(board, position):
            space = 'free'
            return position
        else:
            print(f"That's taken :/ You put {position}")
            continue

def replay():
    
    #default value
    replay = 'incorrect'
    acceptable_values = ['Y','N']
    while replay not in acceptable_values:
        
        replay = input('Want to replay? Y or N: ').upper()
        if replay not in acceptable_values:
            clear_output()
            print(f'Oops! Y or N only :) You put {replay}')
    return replay == 'Y'

#Game
while True:
    print('Welcome to Tic Tac Toe!')
    board = ['#',' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']
    game_on = True
    
    display_board(board)
    
    #pass
    while game_on:
        #Player 1 Turn
        marker = player_input()
        
        position = player_choice(board)
        
        place_marker(board,marker,position)
        
        win_check(board,marker)
        
        display_board(board)
        
        if full_board_check(board):
            print("It's a tie. You should play again")
            game_on = False
        
        if win_check(board, marker):
            print('You win!')
            game_on = False
        # Player2's turn.
            
            #pass
    if not replay():
        break