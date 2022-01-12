#Bryan Jackson's tic tac toe game
#CS210 1-12-2021


def main():
    game_board = [1,2,3,4,5,6,7,8,9] #initialize game board
    move_count = 0 #Initialize moves counter
    move = -1 #Initialize move input
    win = False

    print_game_board(game_board)

    while(move_count < 9 and win == False):
        
        if move_count % 2 == 0:
            move = int(input(f"X's turn. Choose an open square (1-9): "))
            game_board[move - 1] = "X"
        else: 
            move = int(input(f"O's turn. Choose an open square (1-9): "))
            game_board[move - 1] = "O"
        
        move_count += 1

        print_game_board(game_board)

        win = detect_win(game_board)
    
    if (move_count == 9 and win == False):
        print("The game was a draw. Imagine that!")
    else:
        print()

def print_game_board(array_in): #Print game board
    print()
    print("Don't get bored, here's your board. Let's play!")
    print()
    print(f"{array_in[0]}|{array_in[1]}|{array_in[2]}")
    print("=====")
    print(f"{array_in[3]}|{array_in[4]}|{array_in[5]}")
    print("=====")
    print(f"{array_in[6]}|{array_in[7]}|{array_in[8]}")
    print()

def detect_win(array_in):
    if (array_in[0]=="X" and array_in[1]=="X" and array_in[2]=="X"):
        print("X is the winner! Congratulations!")
        win = True
    elif (array_in[3]=="X" and array_in[4]=="X" and array_in[5]=="X"):
        print("X is the winner! Congratulations!")
        win = True
    elif (array_in[6]=="X" and array_in[7]=="X" and array_in[8]=="X"):
        print("X is the winner! Congratulations!")
        win = True
    elif (array_in[0]=="X" and array_in[3]=="X" and array_in[6]=="X"):
        print("X is the winner! Congratulations!")
        win = True
    elif (array_in[1]=="X" and array_in[4]=="X" and array_in[7]=="X"):
        print("X is the winner! Congratulations!")
        win = True
    elif (array_in[2]=="X" and array_in[5]=="X" and array_in[8]=="X"):
        print("X is the winner! Congratulations!")
        win = True
    elif (array_in[0]=="X" and array_in[4]=="X" and array_in[8]=="X"):
        print("X is the winner! Congratulations!")
        win = True
    elif (array_in[2]=="X" and array_in[4]=="X" and array_in[6]=="X"):
        print("X is the winner! Congratulations!")
        win = True

    elif (array_in[0]=="O" and array_in[1]=="O" and array_in[2]=="O"):
        print("O is the winner! Congratulations!")
        win = True
    elif (array_in[3]=="O" and array_in[4]=="O" and array_in[5]=="O"):
        print("O is the winner! Congratulations!")
        win = True
    elif (array_in[6]=="O" and array_in[7]=="O" and array_in[8]=="O"):
        print("O is the winner! Congratulations!")
        win = True
    elif (array_in[0]=="O" and array_in[3]=="O" and array_in[6]=="O"):
        print("O is the winner! Congratulations!")
        win = True
    elif (array_in[1]=="O" and array_in[4]=="O" and array_in[7]=="O"):
        print("O is the winner! Congratulations!")
        win = True
    elif (array_in[2]=="O" and array_in[5]=="O" and array_in[8]=="O"):
        print("O is the winner! Congratulations!")
        win = True
    elif (array_in[0]=="O" and array_in[4]=="O" and array_in[8]=="O"):
        print("O is the winner! Congratulations!")
        win = True
    elif (array_in[2]=="O" and array_in[4]=="O" and array_in[6]=="O"):
        print("O is the winner! Congratulations!")
        win = True
    else:
        win = False

    return(win)

if __name__ == "__main__":
    main()