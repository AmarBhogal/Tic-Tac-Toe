def display_board(board):
    clear_output()
    print(board[7],"|",board[8],"|",board[9])
    print("---------")
    print(board[4],"|",board[5],"|",board[6])
    print("---------")
    print(board[1],"|",board[2],"|",board[3])


def instructions():
    clear_output()
    print("Welcome to Naughts and Crosses!!")
    print("Game of the Year Edition!!")
    print("Inclusive of all DLC!!")
    print("With the cheapest microtransactions around!!")
    print("")
    print("Player 1 will be 'O'")
    print("Player 2 will be 'X'")
    print("")
    print("The spaces on the board match the numbers on the numpad.")
    print("Select a number to place an 'X' or 'O' on the board.")
    print("For example:")
    print("")
    print(" 7 | 8 | 9 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 1 | 2 | 3 ")
    print("")
    print("ARE YOU READYYYYYY?!?!?!?!?")
    print("LET'S GO!!!!!")
    print("")
    print("")


def whos_go(round_count):
    if round_count % 2 != 0:
        print("It's Player 1's go")
        return 1
    else:
        print("It's Player 2's go")
        return 2

def player_input(player,board):
    player_input_valid = False

    #checks if input is valid
    while player_input_valid == False:
        player_input = input(f"Player {player} - Where do you want to play? (1-9): ")
    
        #Checks if input is a number
        if player_input.isdigit() == False:
            print("INVALID INPUT: Not a number.")
    
        #Checks if input is 0-9
        elif int(player_input) not in range(1,10):
            print("INVALID INPUT: Not 1-9.")
            
        #Checks if input has already been played
        elif board[int(player_input)] != " ":
            print("INVALID INPUT: That position has already been played.")

        else:
            player_input_valid = True
            
    #Takes input at integer when input == valid
    player_input = int(player_input)
    return player_input

def update_board(player,board,position_selected):
    #Replace board list
    if player == 1:
        board[position_selected] = "O"
    else:
        board[position_selected] = "X"

def end_conditions(board):
    if " " not in board:
        print("")
        print("DRAW!")
        return True
    elif (board[7] == board[8] == board[9] == "X") or (board[4] == board[5] == board[6] == "X") or (board[1] == board[2] == board[3] == "X") or (board[7] == board[4] == board[1] == "X") or (board[8] == board[5] == board[2] == "X") or (board[9] == board[6] == board[3] == "X") or (board[7] == board[5] == board[3] == "X") or (board[1] == board[5] == board[9] == "X"):
        print("")
        print("Player 2 WINS!")
        return True
    elif (board[7] == board[8] == board[9] == "O") or (board[4] == board[5] == board[6] == "O") or (board[1] == board[2] == board[3] == "O") or (board[7] == board[4] == board[1] == "O") or (board[8] == board[5] == board[2] == "O") or (board[9] == board[6] == board[3] == "O") or (board[7] == board[5] == board[3] == "O") or (board[1] == board[5] == board[9] == "O"):
        print("")
        print("Player 1 WINS!")
        return True
    else:
        return False

def play_again():
    play_again_list = ["Y","N"]
    play_again_input = "Placeholder Response"
    
    while play_again_input not in play_again_list:
        play_again_input = input("Would you like to play again? (Y/N): ")
        if play_again_input not in play_again_list:
            print("INVALID INPUT! Not Y or N.")
    
    return play_again_input == "Y"

from IPython.display import clear_output

restartgame = True

while restartgame == True:
    
    board=["Spare"," "," "," "," "," "," "," "," "," "]
    endgame = False
    round_count = 0

    instructions()

    while endgame == False:

        round_count += 1
    
        #Is it player 1 or 2's go?
        #Checks by seing if Round_count is odd or even
        player = whos_go(round_count)

        #Asks for input from the player 
        #stays in loop if not a number or in 0-9 
        #stays in loop if number has already been played
        position_selected = player_input(player,board)

        #updates the board list 
        update_board(player,board,position_selected)

        #displays board 
        display_board(board)

        #Checks if latest move wins or file the board
        #End game or loops back for next player
        endgame = end_conditions(board)
    
    #Checks if players want to play again
    restartgame = play_again()