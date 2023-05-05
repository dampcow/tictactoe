import random
import time

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
available_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]

x_or_o = input("Would you like to be x or o? ")

while x_or_o != "x" and x_or_o != "o":
    print("Invalid input. Please try again.")
    x_or_o = input("Would you like to be x or o? ")

def main():
    display_board()
    
    while available_squares != []:
        if x_or_o == "o":
            player_start()
        else:
            computer_start()

def computer_start():
    time.sleep(1)
    computer_move()
    display_board()
    time.sleep(1)
    player_move()
    display_board()

def player_start():
    time.sleep(1)
    player_move()
    display_board()
    time.sleep(1)
    computer_move()
    display_board()

def display_board():
    print(f"""
    {board[0]} | {board[1]} | {board[2]}
    ---------
    {board[3]} | {board[4]} | {board[5]}
    ---------
    {board[6]} | {board[7]} | {board[8]}
    """)

def computer_move():
    if available_squares == []:
        print("No more available squares. It's a tie.")
        exit()

    computer_square = random.choice(available_squares)
    print("The computer chose square " + str(computer_square) + ".\n")
        
    if available_squares != []:
        available_squares.remove(computer_square)

    if x_or_o == "x":
        board[computer_square - 1] = "o"
    else:
        board[computer_square - 1] = "x"

def player_move():
    if available_squares == []:
        print("No more available squares. It's a tie.")
        exit()
    
    player_square = int(input("Choose a square from the available tiles: "))

    while player_square not in available_squares:
        print("Invalid input. Please try again.")
        player_square = int(input("Choose a square from the available tiles: "))

    if available_squares != []:
        available_squares.remove(player_square)

    board[player_square - 1] = x_or_o

def check_win():
    pass

if __name__ == '__main__':
    main()