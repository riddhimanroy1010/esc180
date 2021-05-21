#creds to Balaji as well for making the continous analysis function!

import socket, threading, json, contextlib, io, time
from random import *

gomoku = __import__("gomoku") #put your filename here (pls for the love of god run this shit in the same folder as your file (and for the love of jesus do not pyzo this))

HEADER = 16
DELAY = 0.5 #hehehehe
PORT = 5555
FORMAT = 'utf-8'
HOST_IP = '172.105.7.203' #hey those trying to hack my server! there ain't shit on there so gl + my gomoku server is run within a try statement so good f****** luck trying to break that shit

class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = HOST_IP 
        self.addr = (self.host, PORT)
        self.id = self.connect()

    def connect(self):
        self.client.connect(self.addr)
        self.client.send(str.encode('controller'))
        received_message = self.client.recv(2048).decode(FORMAT)
        print(received_message)

    def send(self, data):
        """
        :param data: str
        :return: str
        """
        try:
            self.client.send(str.encode("a:" + str(data)))
            print("DONE")
        except socket.error as e:
            return str(e)

    def get_analysis(self, board):
        self.client.send(str.encode('A:' + json.dumps(board)))
        return self.client.recv(2048).decode(FORMAT)

    def get_win(self, board):
        self.client.send(str.encode('W:' + json.dumps(board)))
        return self.client.recv(2048).decode(FORMAT)

    def get_search(self, board):
        self.client.send(str.encode('S:' + json.dumps(board)))
        return self.client.recv(2048).decode(FORMAT)

class client():

    def __init__(self):
        self.network = Network()

    def run(self):
        not_ended = True
        print("Hello! Welcome to mrmandarin's Gomoku testing program!")
        while(not_ended):
            print("Here are your options:")
            print("1 - Analyse Once")
            print("2 - Continuously Analyse")
            print("3 - Check Win Once")
            print("4 - Continuously Check Win")
            print("5 - Continously Check Search_Max")
            print("6 - Exit")
            s = input()
            if(s == '6'):
                not_ended = False
            elif(s == '1'):
                self.analyze()
            elif(s == '2'):
                self.continuous_analysis()
            elif(s == '3'):
                self.compare_win()
            elif(s == '4'):
                self.continuous_win()
            elif(s == '5'):
                self.continuous_search_max()
            else:
                print("Dafuq you entered boii")

    def analyze(self):
        print("ANALYSING!")
        print("GENERATED BOARD:")
        board = self.generate_random_board()
        gomoku.print_board(board)
        print("HERE'S YOUR ANALYSIS:")
        gomoku.analysis(board)
        print("-------------------------------")
        analysis = json.loads(self.network.get_analysis(board))
        print("HERE'S MRMANDARINS ANALYSIS:")
        for a in analysis:
            print(a)
        print('\n')

    def continuous_win(self):
        board = self.generate_random_board()
        correct_cnt = 0

        while(gomoku.is_win(board) == self.network.get_win(board) or self.network.get_win(board) == "Impossible"):
            print(gomoku.is_win(board))
            print(self.network.get_win(board))
            correct_cnt += 1
            print(f"Number of correct matches: {correct_cnt}")
            time.sleep(DELAY)
            board = self.generate_random_board()

        print("\n\nSomething Doesn't Match!")
        print("Here's the board:")
        gomoku.print_board(board)
        print("YOUR PROGRAM CLAIMS: ")
        print(gomoku.is_win(board))
        print('-------------------------------')
        print("MRMANDARINS'S PROGRAM CLAIMS:")
        print(self.network.get_win(board))
        print('\n')

    def continuous_search_max(self):
        print("USE AT YOUR OWN RISK CUZ SCORE DO BE WHACK")
        board = self.generate_random_board()
        correct_cnt = 0

        while(str(gomoku.search_max(board)) == self.network.get_search(board)):
            correct_cnt += 1
            print(f"Number of correct matches: {correct_cnt}")
            board = self.generate_random_board()

        print("WE HAVE FOUND AN ERROR ^_^")
        print("Here's the board:")
        gomoku.print_board(board)
        print("YOUR PROGRAM CLAIMS: ")
        print(str(gomoku.search_max(board)))
        print('-------------------------------')
        print("MRMANDARINS'S PROGRAM CLAIMS:")
        print(self.network.get_search(board))
        print('\n')

    def compare_win(self):
        print("Impossible refers to when both white and black have winning sequences, this will not be tested.")
        print("GENERATED BOARD:")
        board = self.generate_random_board()
        gomoku.print_board(board)
        print("YOUR PROGRAM CLAIMS:")
        print(gomoku.is_win(board))
        print("-------------------------------")
        print("MRMANDARINS'S PROGRAM CLAIMS:")
        print(self.network.get_win(board))
            
    def continuous_analysis(self): #thanks Balaji!
        yourAnalysis = []
        serverAnalysis = []
        board = None
        correct_counter = 0
        print("To go back to menu just restart the program")
        while yourAnalysis == serverAnalysis:
            correct_counter += 1
            board = self.generate_random_board()

            f = io.StringIO()
            with contextlib.redirect_stdout(f): # temporarily redirect console output to a string buffer 
                gomoku.analysis(board)
            yourAnalysis = f.getvalue().split("\n")[0:-1] # readlines() didn't work
            
            serverAnalysis = json.loads(self.network.get_analysis(board))   
            print("Correct:", correct_counter) # my highscore is 17023

        print("\nFound a case that doesn't work!")
        print("\nThis is the list version of the board (for copy-paste):\n", board)
        print("\nBoard:")
        gomoku.print_board(board)
        print("\nHere is the difference between the analyses:\n")

        # if analyses aren't the same length, then you messed up gomoku.analysis()
        for i in range(len(serverAnalysis)): 
            
            # which stone colour?
            if yourAnalysis[i].find("stones") >= 0:
                print(yourAnalysis[i])
            # either print only the lines that are wrong:
            if yourAnalysis[i] != serverAnalysis[i]:
                print("  Your:", yourAnalysis[i])
                print("Server:", serverAnalysis[i])
                print("")

    #this returns a randomized board, you can also make this return your own custom board to test it against my program
    def generate_random_board(self):
        board = []
        for i in range(8):
            board.append([" "]*8)
        for i in range(randint(5, 30)):
            #this below is absolutely disgusting code but just let it be, man's on a time crunch
            yeee = ('w', 'b')
            try:
                gomoku.put_seq_on_board(board, randint(0, 7), randint(0, 7), randint(-1, 1), randint(0, 1), randint(2, 5), yeee[randint(0,1)])
            except:
                i -= 1
        return board
        '''
        str_board = json.dumps(board)
        return json.loads(str_board)
        '''

root = client()
root.run()
