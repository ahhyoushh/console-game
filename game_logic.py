import os    
import time
import random
import getch
import threading
from rpc import run_rpc
board = ['',' ',' ',' ',' ','<',' ',' ',' ',' ', ' ', ' ', ' ', ' ', ' ',' ',' ',' ',' ',' ',' ']    
   
########win Flags##########    
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
###########################
Game = Running
nigga = 'O'
player = '<'
points = 0
os.system("")  # enables ansi escape characters in terminal

COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}

#This Function Draws Game Board    
def DrawBoard():
    print(f" ___ ___ ___ ___ ___   Points: \033[91m{points}\033[0m")  
    print("| %c | %c | %c | %c | %c |" % (board[1],board[2],board[3],board[4], board[5]))    
    print("|___|___|___|___|___|")    
    print("| %c | %c | %c | %c | %c |" % (board[6],board[7],board[8], board[9], board[10]))    
    print("|___|___|___|___|___|")    
    print("| %c | %c | %c | %c | %c |" % (board[11],board[12],board[13],board[14], board[15]))    
    print("|___|___|___|___|___|")    
    print("| %c | %c | %c | %c | %c |" % (board[16],board[17],board[18],board[19], board[20]))    
    print("|___|___|___|___|___|")  


def spawn_nigga():
    global nigga_pos
    for empty_space in board:
        count = board.count(' ')
        if count > 1:
            empty_space = count
    nigga_pos = random.randint(1, empty_space)
    if nigga_pos != ' ':
        nigga_pos = random.randint(1, empty_space)
        board[nigga_pos] = nigga
    else:
        board[nigga_pos] = nigga
        os.system('clear')
        DrawBoard()        

spawn_nigga()

print("\033[95mKlux game designed by ahhyoushh!\033[0m")
print("\033[91mEXPECT ERRORS!!!\033[0m")
print()
print()
print("Please Wait...")
rpc_thread = threading.Thread(target=run_rpc)
rpc_thread.start()
time.sleep(1)
while Game == Running:
    os.system("clear")
    s_invalid = [16, 17, 18, 19, 20]
    w_invalid = [1, 2, 3, 4, 5]
    player_pos = board.index(player)
    DrawBoard()
    if player_pos == nigga_pos:
        points+=1
        spawn_nigga()
    print("\033[94mInput:\033[0m", end=" ", flush=True)
    choice = getch.getch()
    if choice == 'q':
        exit()
    elif choice == 'd':
        if player_pos != 20:
            board[player_pos] = ' '
            board[player_pos+1] = player
    elif choice == 'a':
        if player_pos != 1:
            board[player_pos] = ' '
            board[player_pos-1] = player
    elif choice == 'w':
        if player_pos not in w_invalid:
            board[player_pos] = ' '
            board[player_pos-5] = player
    elif choice == 's':
        if player_pos not in s_invalid:
            board[player_pos] = ' '
            board[player_pos+5] = player

