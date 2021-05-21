'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random
##Playing Mechanics
def make_random_move(board, mark):
    free_squares = get_free_squares(board)
    coord_num = random.randint(1, 9)
    coords = return_coord(coord_num)
    while coords not in free_squares:
        coord_num = random.randint(1, 9)
        coords = return_coord(coord_num)
    if coords in free_squares:
        put_in_board(board, mark, coord_num)

def is_row_all_marks(board, row_i, mark):
    counter  = 0
    for i in range(3):
        if board[row_i][i] == mark:
            counter += 1
    if counter == 3:
        return True
    return False

def is_col_all_marks(board, col_i, mark):
    counter  = 0
    for i in range(3):
        if board[i][col_i] == mark:
            counter += 1
    if counter == 3:
        return True
    return False

def is_win(board, mark):
    colmns = [0, 1, 2]
    rows = [0, 1, 2]
    diagonals = [[1, 5, 9], [3, 5, 7]]
    for colmn in colmns:
        if is_col_all_marks(board, colmn, mark) == True:
            return True
    for row in rows:
        if is_row_all_marks(board, row, mark) == True:
            return True
    diag_counter = 0
    for diagonal in diagonals:
        for coords in diagonal:
            coord = return_coord(coords)
            if board[coord[0]][coord[1]] == mark:
                diag_counter += 1
        if diag_counter == 3:
            return True
        else:
            diag_counter = 0
    return False

#Bot gameplay
def bot_play(mark):
    free = get_free_squares(board)
    if len(free) == 0:
        return None
    for i in range(1, 10):
        if return_coord(i) in free:
            put_in_board(bot_board, mark, i)
            if is_win(bot_board, mark) == True:
                put_in_board(board, mark, i)
                return None
            else:
                put_in_board(bot_board, " ", i)
        else:
            continue
    for i in range(1, 10):
        if return_coord(i) in free:
            put_in_board(bot_board, "X", i)
            if is_win(bot_board, "X") == True:
                put_in_board(board, mark, i)
                return None
            else:
                put_in_board(bot_board, " ", i)
        else:
            continue
    make_random_move(board, mark)

##Board manipulation
def return_coord(square_num):
    coord = [0] * 2
    row_num = ((square_num - 1) // 3)
    if square_num % 3 != 0:
        col_num = (square_num % 3) - 1
    else:
        col_num = 2
    coord[0] = row_num
    coord[1] = col_num
    return coord

def put_in_board(board, mark, square_num):
    coord = return_coord(square_num)
    board[coord[0]][coord[1]] = mark

def get_free_squares(board):
    free = []
    for i in range(1, 10):
        coords = return_coord(i)
        if board[coords[0]][coords[1]] == " ":
            free.append(coords)
    return free

#Player type
def player_mode():
    player_type = int(input("Enter number of players: "))
    while player_type not in [1, 2]:
        player_type = input("Enter number of players: ") 
    return player_type

##printing
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
            
def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
     
if __name__ == '__main__':
    print("\n")
    print("Welcome to TicTacToe. If playing with another human, \nplayer 1 is player O. With the bot, the human is player X")
    print("\n")
    board = make_empty_board()
    bot_board = make_empty_board()
    print_board_and_legend(board)    
    
    print("\n")
       
    if_win = False
    game_type = player_mode()
    user_count = 0
    while (game_type == 2) and (if_win == False):  
        input_num = int(input("Enter your move: "))
        while input_num < 1 or input_num > 9:
            input_num = int(input("Enter your move: "))

        while return_coord(input_num) not in get_free_squares(board):
            input_num = int(input("Square not free. Enter your move: "))

        user_count += 1

        if user_count % 2 == 0:
            put_in_board(board, "X", input_num)
            print_board_and_legend(board)
            if is_win(board, "X") == True:
                if_win = True
                print ("Player X wins")  
                exit()   
        else:
            put_in_board(board, "O", input_num)
            print_board_and_legend(board)
            if is_win(board, "O") == True:
                if_win = True
                print ("Player O wins") 
                exit() 
        (get_free_squares(board))
        print("\n")
        if len(get_free_squares(board)) == 0:
            print("Tie")
            exit()

    while (game_type == 1) and (if_win == False):
        input_num = int(input("Enter your move: "))
        while input_num < 1 or input_num > 9:
            input_num = int(input("Enter your move: "))

        while return_coord(input_num) not in get_free_squares(board):
            input_num = int(input("Square not free. Enter your move: "))

        put_in_board(board, "X", input_num) 
        put_in_board(bot_board, "X", input_num) 
        if is_win(board, "X") == True:
            if_win = True
            print("Human Wins")
            print_board_and_legend(board)
            break

        bot_play("O")
        if is_win(board, "O") == True:
            if_win = True
            print("Bot Wins")
        print_board_and_legend(board)
        if len(get_free_squares(board)) == 0:
            print("Tie")
            exit()
    

