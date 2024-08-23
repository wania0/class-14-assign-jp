tic_tac_toe_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def display_board():
    print(tic_tac_toe_board[0], "|", tic_tac_toe_board[1], "|", tic_tac_toe_board[2])
    print("----------")
    print(tic_tac_toe_board[3], "|", tic_tac_toe_board[4], "|", tic_tac_toe_board[5])    
    print("----------")
    print(tic_tac_toe_board[6], "|", tic_tac_toe_board[7], "|", tic_tac_toe_board[8], "\n")
    
display_board()

def tic_tac_toe():
    player = "X"
    while True:
        choice = int(input(f"Player {player} make your choice (1-9):"))
        if choice in (1,9):
            index = choice - 1
            if player == "X":
                if tic_tac_toe_board[index] == " ":
                    tic_tac_toe_board[index] = player
                    display_board()
                else:
                    print("this position is not available. Try again")
                    display_board()
        else:
                choice = int(input(f"Player {player} make your choice (1-9):"))
        if choice in (1,9):
            index = choice - 1
            if player == "X":
                if tic_tac_toe_board[index] == " ":
                    tic_tac_toe_board[index] = player
                    display_board()
                else:
                    print("this position is not available. Try again")
                    display_board()
                    
      
tic_tac_toe()



# # Function to check if there's a winner
# def check_winner():
#     # Define the winning combinations (rows, columns, diagonals)
#     win_combinations = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
#         [0, 4, 8], [2, 4, 6]              # Diagonals
#     ]
    
#      # Check for a winner in each combination
#     for combo in win_combinations:
#         if tic_tac_toe_board[combo[0]] == tic_tac_toe_board[combo[1]] == tic_tac_toe_board[combo[2]]and tic_tac_toe_board[combo[0]] != " ":
#             return tic_tac_toe_board[combo[0]]
    
#     return None

# # Function to check if the board is full (draw condition)
# def is_board_full():
#     return " " not in tic_tac_toe_board

# # Main game loop
# def play_game():
#     current_player = "X"
    
#     while True:
#         display_board()
#         index = choice - 1
#         # Check if the chosen position is available
#         if tic_tac_toe_board[index] != " ":
#             print("That position is already taken. Try again.")
#             continue
#         # Place the player's move on the board
#         tic_tac_toe_board[index] = current_player
        
#         # Check for a winner
#         winner = check_winner()
#         if winner:
#             display_board()
#             print(f"Player {winner} wins!")
#             break
        
#         # Check for a draw
#         if is_board_full():
#             display_board()
#             print("It's a draw!")
#             break
        
#         # Switch players
#         current_player = "O" if current_player == "X" else "X"

# # Start the game
# play_game()
