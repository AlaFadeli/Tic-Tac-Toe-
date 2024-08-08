
# This will be the first coding game for me : 

def create_board(): 

    return [" "] * 9 

def show_board(board) :

    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def input_moves():
    while True : 
            try :
            
                move = int(input("Enter you move (1-9) : ")) - 1 
                if move < 0 or move > 8 :  
                    print("Out of range")
                else : 
                    return move
            except ValueError : 
                print("Invalid input")

def make_move(board, move, player) : 
    if board[move] ==  " " : 
        board[move] = player 
        return True
    return False

def know_winner(board,player) : 
    win_cond = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for cond in win_cond : 
        if all(board[i] == player for i in cond) : 
            return True
        return False


def final_fun() : 
    board = create_board()
    current_player = "X"

    for turn in range(9) : 
        show_board(board)
        move = input_moves()

        if make_move(board, move, current_player) : 
            if know_winner(board,current_player) :
                show_board(board) 
                print(f"Player {current_player} wins !")
                return


            current_player = "O" if current_player == "X" else "O"
        else : 
            print("Position already taken")

    
    show_board(board)
    print("It's a draw")

final_fun()

print("Thanks for playing")
