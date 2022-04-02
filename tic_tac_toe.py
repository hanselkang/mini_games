import random
from timeit import repeat
from IPython.display import clear_output


def display_board(board):
    clear_output()
    print(board[1] + " | " + board[2] + " | " + board[3])
    print('--+---+--')
    print(board[4] + " | " + board[5] + " | " + board[6])
    print('--+---+--')
    print(board[7] + " | " + board[8] + " | " + board[9])


# tttest_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
ttt_board = [' '] * 10
display_board(ttt_board)


def player_input():

    marker = ' '
    # Keep asking first player to choose X or O
    while not (marker == 'X' or marker == 'O'):
        # Upper case in case player put lower case
        marker = input('Player 1, please choose X or O: ').upper()
        player1 = marker

    # Player's Marker decision
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'

    return (player1, player2)


def place_marker(ttt_board, marker, position):
    ttt_board[position] = marker

# Test
# place_marker(ttt_board,'$', 8)
# display_board(ttt_board)


def win_check(ttt_board, mark):
    # Check the possible combination
    # All rows check to see if they all occupied by same marker
    return ((ttt_board[1] == ttt_board[2] == ttt_board[3] == mark) or
            (ttt_board[4] == ttt_board[5] == ttt_board[6] == mark) or
            (ttt_board[7] == ttt_board[8] == ttt_board[9] == mark) or
            # All columns Check
            (ttt_board[1] == ttt_board[4] == ttt_board[7] == mark) or
            (ttt_board[2] == ttt_board[5] == ttt_board[8] == mark) or
            (ttt_board[3] == ttt_board[6] == ttt_board[9] == mark) or
            # 2 diagonals Check
            (ttt_board[1] == ttt_board[5] == ttt_board[9] == mark) or
            (ttt_board[3] == ttt_board[5] == ttt_board[7] == mark))


# Who is going to be first?


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Check if the board is empty


def space_check(ttt_board, position):
    return ttt_board[position] == ' '

# Check if the board is full


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # Board is full if it's True
    return True

# Choose a position which is empty


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position (1-9) : '))

    return position

# After finish game


def replay():
    choice = input("Play again? Enter Y or N ").lower()
    if choice == 'n':
        game_on = False
    else:
        return choice == 'y'


# While loop to keep running the game
print('Welcome to Tic Tac Toe')
while True:
    # Play the game
    ttt_board = [' '] * 10
    # Set everything up ( Board, Who's first, Choose markers)
    player1_marker, player2_marker = player_input()
    print(f'Player1: "{player1_marker}", Player2: "{player2_marker}"')
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # Game play

    while game_on:
        # Player 1 turn
        if turn == 'Player 1':

            # Show the board
            display_board(ttt_board)

            # Choose a position
            position = player_choice(ttt_board)

            # Place the marker on the position
            place_marker(ttt_board, player1_marker, position)

            # Check if they won
            if win_check(ttt_board, player1_marker):
                display_board(ttt_board)
                print('Player 1 has WON')
                game_on = False
            else:
                # Or check if there is a tie
                if full_board_check(ttt_board):
                    display_board(the_board)
                    print("DRAW!")
                    game_on = False
                # No tie, No win? Next player
                else:
                    turn = 'Player 2'
        # Player 2 turn
        else:
            # Show the board
            display_board(ttt_board)

            # Choose a position
            position = player_choice(ttt_board)

            # Place the marker on the position
            place_marker(ttt_board, player2_marker, position)

            # Check if they won
            if win_check(ttt_board, player2_marker):
                display_board(ttt_board)
                print('Player 2 has WON')
                game_on = False
            else:
                # Or check if there is a tie
                if full_board_check(ttt_board):
                    display_board(the_board)
                    print("DRAW!")
                    game_on = False
                # No tie, No win? Next player
                else:
                    turn = 'Player 1'

    if not replay():
        break
# Break out tf the while loop on replay()
