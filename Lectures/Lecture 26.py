def is_win21(n):
    '''Return true if being at sum n and having the turn results in a win; user
    can move 1 or 2'''
    #Base Case
    if n == 19 or n == 20:
        return True
    elif n >= 21:
        return False

    return not is_win21(n + 1) or not is_win21(n + 2)

def is_win21_simple(n):
    '''Return true if being at sum n and having the turn results in a win; user
    can move only 1'''
    if n == 20:
        return True
    
    return not is_win21_simple(n + 1)
    
import random
def move21(n):
    if not is_win21(n + 1):
        return 1
    elif not is_win21(n + 2):
        return 2
    else:
        return int(2*random.random())
        
def play_21():
    n = 0
    while n < 21:
        n = int(input("Num: "))
        n += move21(n)
        print("Computer move:", n)
        if is_win21(n) == "Computer Wins":
            print("Computer Wins")
            return None
        elif n == 21:
            print("Human Wins")
            return None

def game21_nice(cur_player):
    n = 0
    print("Current Sum =", n)
    allowed_moves = [1, 2]
    while n != 21:
        if cur_player == 'USER':
            move = int(input("MOVE: "))
            while move not in allowed_moves:
                move = int(input("MOVE: "))
            cur_player = 'COMPUTER'
        else:
            move = move21(n)

            cur_player = 'USER'
        
        n += move
        if n > 0:
            print("Current Sum =", n)
    
    if cur_player == "USER":
        print("COMPUTER WON")
    else:
        print("USER WON")


def sum_list(L):
    if len(L) == 0:
        return 0
    
    return L[0] + sum_list(L[1:])

def sum_list2(L):
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        return L[0]
    
    mid = len(L) // 2
    return sum_list2(L[:mid]) + sum_list2(L[mid:])

def letter_trials():
    alpha = ['C', 'B', 'M']
    for c1 in alpha:
        for c2 in alpha:
            for c3 in alpha:
                if c1 != c2 and c2 != c3 and c1 != c3:
                    print(c1 + c2 + c3)
letter_trials()








