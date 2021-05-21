"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 26, 2020
"""

def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != " ":
                return False
    return True

def is_bounded(board, y_end, x_end, length, d_y, d_x):

    y_start = (y_end - (length)*d_y)
    x_start = (x_end - (length)*d_x)
    y_end = y_end + d_y
    x_end = x_end + d_x

    if (y_start<0 and x_start>=0) or (y_start>=0 and x_start<0) or (y_start<0 or x_start<0) or (y_start<=7 and x_start>7):
        y_start = y_start + d_y
        x_start =  x_start + d_x
    else:
        x_start
        y_start 

    if not (0<=y_end<=7 and 0<=x_end<=7):
        
        x_end = x_end - d_x
        y_end = y_end - d_y

    else:
        x_end 
        y_end 
    
    if board[y_start][x_start]==" " and board[y_end][x_end]==" ":
        return "OPEN" 
    elif board[y_start][x_start] !=" " and board[y_end][x_end]!=" ":
        return "CLOSED" 
    elif board[y_start][x_start]!=" " or board[y_end][x_end]!=" ":
        return "SEMIOPEN"

def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count = 0
    semi_open_seq_count = 0

    lengths = []
    x_coords = []
    y_coords = []
    seq_length = 0
    i = 0
    
    while i <= len(board):
        if 0 <= (x_start + i * d_x) < len(board[0]) and 0 <= (y_start + i * d_y) < len(board):
            cur_pos = board[y_start + i * d_y][x_start + i * d_x]
            if cur_pos == col:
                seq_length += 1
            else:
                if (seq_length == length) and (seq_length >= 2):
                    lengths.append(seq_length)
                    x_coords.append(x_start + (i - 1) * d_x)
                    y_coords.append(y_start + (i - 1) * d_y)
                seq_length = 0
            i +=1
        else:
            break

    if seq_length == length:
        lengths.append(seq_length)
        x_coords.append(x_start+  (i-1)* d_x)
        y_coords.append(y_start+ (i-1) * d_y)

    for i in range(len(lengths)):
        state = is_bounded(board, y_coords[i], x_coords[i], lengths[i], d_y, d_x) 
        if state == "OPEN":
            open_seq_count += 1
        elif state == "SEMIOPEN":
            semi_open_seq_count += 1
            
    return open_seq_count, semi_open_seq_count

def detect_row_closed(board, col, y_start, x_start, length, d_y, d_x):
    closed_seq_count = 0

    lengths = []
    x_coords = []
    y_coords = []
    seq_length = 0
    i = 0
    
    while i <= len(board):
        if 0 <= (x_start + i * d_x) < len(board[0]) and 0 <= (y_start + i * d_y) < len(board):
            cur_pos = board[y_start + i * d_y][x_start + i * d_x]
            if cur_pos == col:
                seq_length += 1
            else:
                if (seq_length == length) and (seq_length >= 2):
                    lengths.append(seq_length)
                    x_coords.append(x_start + (i - 1) * d_x)
                    y_coords.append(y_start + (i - 1) * d_y)
                seq_length = 0
            i +=1
        else:
            break
    
    if seq_length == length:
        lengths.append(seq_length)
        x_coords.append(x_start + (i-1) * d_x)
        y_coords.append(y_start + (i-1) * d_y)

    for i in range(len(lengths)):  
        state = is_bounded(board, y_coords[i], x_coords[i], lengths[i], d_y, d_x) 
        if state == "CLOSED":
            closed_seq_count += 1
            
    return closed_seq_count

def detect_rows(board, col, length):

    open_seq_count, semi_open_seq_count = 0, 0
    rd_dict ={}

    diag_runs = int((2+4*(len(board)-length))/2)
    
    for i in range(diag_runs):
        
        if (i>diag_runs/2):
            xdir = 0
            ydir = 1
            const =  int(diag_runs/2 - 0.5)
        else:
            xdir = 1
            ydir = 0
            const = 0

        if i == int(diag_runs/2 +0.5):
            for k in range(int(diag_runs/2 + 0.5), diag_runs):
                for j in range(len(board)-1, len(board)-2-int(diag_runs/2 - 0.5), -1):
                    if j in rd_dict.values():
                        pass
                    else:
                        rd_dict.update({k:j}) 

        left_down = detect_row(board, col, (0+i)*xdir, (i-const)*ydir, length, 1, 1)
        
        if i>int(diag_runs/2 - 0.5):
                right_down = detect_row(board, col, (0+i)*xdir, rd_dict[i]+(len(board)-1)*xdir, length, 1, -1)   
                
        else:
            right_down = detect_row(board, col, (0+i)*xdir, (i-1)*ydir+(len(board)-1)*xdir, length, 1, -1)
            
        open_seq_count += left_down[0] + right_down[0]
        semi_open_seq_count += left_down[1] + right_down[1]

    for j in range(len(board)):
        rows = detect_row(board, col, j, 0, length, 0, 1)
        columns = detect_row(board, col, 0, j, length, 1, 0)

        open_seq_count += rows[0] + columns[0]
        semi_open_seq_count += rows[1] + columns[1]

    return (open_seq_count, semi_open_seq_count)

def detect_rows_closed(board, col, length):
    closed_seq = 0
    rd_dict = {}
    diag_runs = int((2+4*(len(board)-length))/2)
    
    for i in range(diag_runs):
        if (i > diag_runs/2):
            xdir = 0
            ydir = 1
            const =  int(diag_runs/2 - 0.5)
        else:
            xdir = 1
            ydir = 0
            const = 0
        if i == int(diag_runs/2 +0.5):
            for k in range(int(diag_runs/2 + 0.5), diag_runs):
                for j in range(len(board)-1, len(board)-2-int(diag_runs/2 - 0.5), -1):
                    if j in rd_dict.values():
                        pass
                    else:
                        rd_dict.update({k:j})
        left_down = detect_row_closed(board, col, (0+i)*xdir, (i-const)*ydir, length, 1, 1)
        if i>int(diag_runs/2 - 0.5):
                right_down = detect_row_closed(board, col, (0+i)*xdir, rd_dict[i]+(len(board)-1)*xdir, length, 1, -1)   
        else:
            right_down = detect_row_closed(board, col, (0+i)*xdir, (i-1)*ydir+(len(board)-1)*xdir, length, 1, -1)
        closed_seq += left_down + right_down

    for j in range(len(board)):
        rows = detect_row_closed(board, col, j, 0, length, 0, 1)
        columns = detect_row_closed(board, col, 0, j, length, 1, 0)
        closed_seq += rows+columns

    return closed_seq

def search_max(board):
    coords = ()
    max_score = -1000000000
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                put_seq_on_board(board, i, j, 1, 1, 1, "b")
                cur_score = score(board)
                if cur_score >= max_score:
                    max_score = cur_score
                    coords = (i, j)
                put_seq_on_board(board, i, j, 1, 1, 1, " ")
                
    return coords
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def is_win(board):
    board_full = True
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                board_full = False
                break
    if (detect_rows(board, "w", 5)[0] or detect_rows(board, "w", 5)[1]) > 0:
        return "White won"
    elif (detect_rows(board, "b", 5)[0] or detect_rows(board, "b", 5)[1]) > 0:
        return "Black won"
    elif detect_rows_closed(board, "w", 5) > 0:
        return "White won"
    elif detect_rows_closed(board, "b", 5) > 0:
        return "Black won"
    elif board_full == True:
        return "Draw"
    else:
        return "Continue playing"

def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    
def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                
def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
          
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
               
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    print(analysis(board))
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0

def testing_win_5_closed():
    board = make_empty_board(8)
    board[2][2] = "w"
    y = 3;
    x = 2;
    d_x = 0;
    d_y = 1;
    length = 5
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    if is_win(board)=="Black won":
        print("PASSSSSSSSS")
    else:
        print("EPIC FAIL :(")

def is_bounded_test_corner():
    board = make_empty_board(8)
    board[0][0] = "w"
    board[0][7] = "w"
    board[7][0] = "w"
    board[7][7] = "w"
    print_board(board)

    a,mini_test_count=0,0
    #checking (0,0)
    y,x=0,0
    if is_bounded(board,y,x,1,0,1)=="SEMIOPEN" and is_bounded(board,y,x,1,1,0)=="SEMIOPEN" and is_bounded(board,y,x,1,1,-1)=="CLOSED" and is_bounded(board,y,x,1,1,1)=="SEMIOPEN":
        mini_test_count+=4

    #checking (7,0)
    x,y=7,0
    if is_bounded(board,y,x,1,0,1)=="SEMIOPEN" and is_bounded(board,y,x,1,1,0)=="SEMIOPEN" and is_bounded(board,y,x,1,1,-1)=="SEMIOPEN" and is_bounded(board,y,x,1,1,1)=="CLOSED":
        mini_test_count+=4

    #checking (0,7)
    x,y=0,7
    if is_bounded(board,y,x,1,0,1)=="SEMIOPEN" and is_bounded(board,y,x,1,1,0)=="SEMIOPEN" and is_bounded(board,y,x,1,1,-1)=="SEMIOPEN" and is_bounded(board,y,x,1,1,1)=="CLOSED":
        mini_test_count+=4

    #checking (7,7)
    x,y=7,7
    if is_bounded(board,y,x,1,0,1)=="SEMIOPEN" and is_bounded(board,y,x,1,1,0)=="SEMIOPEN" and is_bounded(board,y,x,1,1,-1)=="CLOSED" and is_bounded(board,y,x,1,1,1)=="SEMIOPEN":
        mini_test_count+=4

    if mini_test_count == 16:
        print("TEST CASE for is_bounded PASSED!!!!")
    else:
        print("TEST CASE for is_bounded FAILED, passing", mini_test_count,"/16",":(")

if __name__ == '__main__':
    #play_gomoku(8)
    
    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', 'b', ' ', ' ', ' ', ' '],
             [' ', ' ', 'b', ' ', ' ', ' ', ' ', ' '],
             [' ', 'b', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'b', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', 'b', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', 'b', ' ', ' ', ' ', ' ']]
    print(detect_row(board, "b", 4, 0, 3, 1, 1))
    

    '''board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    put_seq_on_board(board, 0, 5, d_y, d_x, 1, "w")
    put_seq_on_board(board, length + 1, 5, d_y, d_x, 1, "w")
    print_board(board)

    print(is_bounded(board, 4, 5, 5, 1, 0))
    print(detect_row(board, "b", 0, 5, 5, d_y, d_x))'''

    '''board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, length + 1, 5, d_y, d_x, 1, "w")
    put_seq_on_board(board, 0, 0, 1, 1, 6, "w")
    print_board(board)
    #test_detect_row()
    #print(detect_row(board, "w", 0, x, length, d_y, d_x))
    x_coords = []
    y_coords = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "w":
                print(i, j)
                x_coords.append(j)
                y_coords.append(i)
    print(sorted(x_coords), sorted(y_coords))
    '''
    '''
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    #print(detect_rows(board, col, 3))
    #print(detect_row(board, "w", 1, 5, 3, 1, 0))
    #test_detect_rows()
    print(is_bounded(board, 3, 5, 3, 1, 0))
    print(detect_row(board, "w", 1, 5, 3, 1, 0))
    '''
    
    
    ''' 
    board = make_empty_board(8)
    x = 7; y =1 ; d_x = -1; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    print(is_bounded(board, 4, 4,4, 1, -1))
    print(detect_row(board, "b", 1, 7, 4, 1, -1))

    
    board = make_empty_board(8)
    x = 0; y =2 ; d_x = 1; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    print(detect_row(board, "b", y, x, length, d_y, d_x))
    
    board = make_empty_board(8)
    x = 5; y = 5 ; d_x = 1; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    print(is_bounded(board, 7, 7,3, 1, 1))
    print(detect_row(board, "b", 5, 5, 3, 1, 1))
    '''
    '''
    board = make_empty_board(8)
    x = 0; y = 2; d_x = 1; d_y = 1; length = 3; 
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    print(is_bounded(board, 7, 7,3, 1, 1))
    print(detect_row(board, "b", 2, 0, 3, 1, 1))
    
    test_is_bounded()
    test_detect_row()
     
    board = make_empty_board(8)
    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    print(search_max(board))

    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    test_search_max()
    print(search_max(board))
    
    play_gomoku(8)
    '''    
    
    #easy_testset_for_main_functions()
    #play_gomoku(8)
    testing_win_5_closed()
    is_bounded_test_corner()

    board = []
    for i in range(8):
        board.append([" "]*8)
    put_seq_on_board(board, 0, 0, 0, 1, 1, "w")
    put_seq_on_board(board, 1, 1, 0, 1, 2, "w")
    put_seq_on_board(board, 3, 6, 0, 1, 1, "w")
    put_seq_on_board(board, 0, 3, 0, 1, 3, "w")
    put_seq_on_board(board, 6, 6, 0, 1, 1, "w")
    put_seq_on_board(board, 2, 3, 1, 1, 3, "w")
    put_seq_on_board(board, 7, 4, 0, 1, 4, "w")
    put_seq_on_board(board, 2, 5, 0, 1, 2, "w")
    put_seq_on_board(board, 5, 2, 1, 1, 2, "w")
    put_seq_on_board(board, 7, 0, 0, 1, 1, "b")
    put_seq_on_board(board, 0, 6, 0, 1, 1, "b")
    put_seq_on_board(board, 7, 2, 0, 1, 2, "b")
    put_seq_on_board(board, 2, 2, 1, 1, 4, "b")
    put_seq_on_board(board, 3, 2, 1, 1, 3, "b")
    put_seq_on_board(board, 3, 1, 1, 1, 3, "b")
    put_seq_on_board(board, 0, 7, 1, 0, 3, "b")
    put_seq_on_board(board, 6, 0, 0, 1, 2, "b")
    put_seq_on_board(board, 2, 0, 1, 0, 3, "b")
    put_seq_on_board(board, 3, 5, 1, 1, 3, "b")
    put_seq_on_board(board, 1, 4, 0, 1, 2, "b")
    print_board(board)
    print(detect_row(board, "b", 7, 0, 2, 0, 1))
    analysis(board)   
    