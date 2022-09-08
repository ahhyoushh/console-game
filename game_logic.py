import os    
import time    
import random
board = ['',' ',' ',' ',' ','<',' ',' ',' ',' ']    
   
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
    print(f" ___ ___ ___              Points: \033[91m{points}\033[0m")  
    print("| %c | %c | %c |" % (board[1],board[2],board[3]))    
    print("|___|___|___|")    
    print("| %c | %c | %c |" % (board[4],board[5],board[6]))    
    print("|___|___|___|")    
    print("| %c | %c | %c |" % (board[7],board[8],board[9]))    
    print("|___|___|___|")    


def spawn_nigga():
    global nigga_pos
    for empty_space in board:
        count = board.count(' ')
        if count > 1:
            empty_space = count
    nigga_pos = random.randint(1, empty_space)
    if board[nigga_pos] == ' ':
        board[nigga_pos] = nigga

spawn_nigga()

print("\033[95mKlux game designed by ahhyoushh!\033[0m")
print("\033[91mEXPECT ERRORS!!!\033[0m")
print()
print()
print("Please Wait...")
time.sleep(3)
while Game == Running:
    os.system("clear")
    s_valid = [1, 2, 3, 4, 5, 6]
    w_valid = [4, 5, 6, 7, 8, 9]
    player_pos = board.index(player)
    DrawBoard()
    if player_pos == nigga_pos:
        points+=1
        spawn_nigga()
    choice = str(input("\033[94mInput:\033[0m"))
    if choice == 'q':
        exit()
    elif choice == 'd':
        if player_pos != 9:
            board[player_pos] = ' '
            board[player_pos+1] = player
    elif choice == 'a':
        if player_pos != 1:
            board[player_pos] = ' '
            board[player_pos-1] = player
    elif choice == 'w':
        if player_pos in w_valid:
            board[player_pos] = ' '
            board[player_pos-3] = player
    elif choice == 's':
        if player_pos in s_valid:
            board[player_pos] = ' '
            board[player_pos+3] = player

