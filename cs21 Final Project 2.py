#cs21 E
#Sidhanth Kafley
#Final Project
#Simple Tic Tac Toe Game

#import random to be used by the computer as an opponent
import random

#define main
def main():
    print("Tic-Tac-Toe Game")
    print("-----------------")
    print("The computer is your formidable opponent!")
    print("\n")
    print("Rules: You have a select a number that represents a spot on the board as shown below:")
    print("   |   |   ")
    print("",1,"|",2,"|",3,"")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print("",4,"|",5,"|",6,"")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print("",7,"|",8,"|",9,"")
    print("   |   |   ")
    print("The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
    print("\n")
    print("For a little bit of challenge, try entering a spot other than the center spot;)")
    print("\n")
    
    #I'm adding a value for again in the beginning to enter into the loop.
    again="y"

#create a while loop to allow the user to play the game again.
#I've used breaks to exit the while loop as it was much easier and it greatly reduced the size of the code
    while again=="y" or again == "Y":
        
#add exception handling
        try:

            board=[""," "," "," "," "," "," "," "," "," "]

            while True:
            
                create_board(board)
                #1st player, get input from user
                user_input=int(input("Enter a number from 1-9 to select a spot: "))
                #Add input validation
                while user_input >9 or user_input<1:
                    print("Sorry! The number has to be from 1-9")
                    user_input=int(input("Enter a number from 1-9 to select a spot: "))

                #Add a way to prevent the user form selecting the same spot again
                while board[user_input] != " ":
                    print("Sorry the spot has already been selected.")
                    user_input=int(input("Enter a number from 1-9 to select a spot: "))
                    

            #check and see if the spot is empty or not, if it is empty add "x"
                if board[user_input] == " ":
                    board[user_input]="X"
                    
            #check if the user is the winner
                if winner(board,"X"):
                    print("Congratulations! You win :)")
                    again=input("Do you want to play again? y/n? ")
                    if again== "n" or again=="N":
                        print("Thank you for playing")
                    break
                    
            #Check for a draw/tie
                if tie(board) == True:
                    print("Its a tie :|")
                    again=input("Do you want to play again? y/n? ")
                    if again=="n" or again=="N":
                        print("Thank you for playing")
                    break
                
                #2nd player, get a random numer from the opponent which is the computer
                create_board(board)
                user_input= opponent_move(board,"O") 
                print("The opponent chose:", user_input)
                #Add a way to prevent the computer from selecting the same spot again
                while board[user_input] != " ":
                    print("Sorry the spot has already been selected.")
                    user_input=opponent_move(board,"O")
                    
            #check and see if the spot is empty or not, if it is empty add "O"
                if board[user_input] == " ":
                    board[user_input]="O"
                
            #check if the opponent is the winner
                if winner(board,"O"):
                    print("Opponent wins :(")
                    again=input("Do you want to play again? y/n? ")
                    if again=="n" or again=="N":
                        print("Thank you for playing")
                    break
            #Check for a draw/tie
                if tie(board) == True:
                    create_board(board)
                    print("Its a tie :|")
                    again=input("Do you want to play again? y/n? ")
                    if again=="n" or again=="N":
                        print("Thank you for playing")
                    break

        except ValueError:
            print("Sorry, you have to enter a whole numer from 1-9")
            again=input("Try again? y/n?")
            if again=="n" or again=="N":
                        print("Thank you for playing")

#create the tic tac toe board
def create_board(board):
    print("   |   |   ")
    print("",board[1],"|",board[2],"|",board[3],"")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print("",board[4],"|",board[5],"|",board[6],"")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print("",board[7],"|",board[8],"|",board[9],"")
    print("   |   |   ")

#Check for the winner using a function called winner()        
def winner(board,player):
    if board[1] == player and board[2] == player and board[3] == player:
        create_board(board)
        return True
        
    elif board[4] == player and board[5] == player and board[6] == player:
        create_board(board)
        return True
        
    elif board[7] == player and board[8] == player and board[9] == player:
        create_board(board)
        return True
        
    elif board[1] == player and board[5] == player and board[9] == player:
        create_board(board)
        return True
        
    elif board[3] == player and board[5] == player and board[7] == player:
        create_board(board)
        return True
        
    elif board[3] == player and board[6] == player and board[9] == player:
        create_board(board)
        return True
        
    elif board[1] == player and board[4] == player and board[7] == player:
        create_board(board)
        return True
        
    elif board[2] == player and board[5] == player and board[8] == player:
        create_board(board)
        return True
    else:
        return False

#Check for a tie or draw using function tie()
def tie(board):
    if " " in board:
        return False
    else:
        return True
    
#Use the function opponent_move to get a move from the opponent
def opponent_move(board,player):
    #To make things a little bit difficult for the user, I added this code to program the computer to win
    #if it gets an opportunity to win either in the vertical, horizontal or diagonal direction
    
    for i in [1,2,3]:
        if board[i]==player and board[i+3]==player and board[i+6]==" ":
            return i+6
        if board[i]==player and board[i+6]==player and board[i+3]==" ":
            return i+3
        if board[i+6]==player and board[i+3]==player and board[i]==" ":
            return i+6
    for i in [1,4,7]:
        if board[i]==player and board[i+1]==player and board[i+2]==" ":
            return i+2
        if board[i]==player and board[i+2]==player and board[i+1]==" ":
            return i+1
        if board[i+2]==player and board[i+2]==player and board[i]==" ":
            return i
    for i in [1]:
        if board[i]==player and board[i+4]==player and board[i+8]==" ":
            return i+8
        if board[i]==player and board[i+8]==player and board[i+4]==" ":
            return i+4
        if board[i+4]==player and board[i+8]==player and board[i]==" ":
            return i
    for i in [3]:
        if board[i]==player and board[i+2]==player and board[i+4]==" ":
            return i+4
        if board[i]==player and board[i+4]==player and board[i+2]==" ":
            return i+2
        if board[i+4]==player and board[i+2]==player and board[i]==" ":
            return i
    #To make things a little more difficult I programmed the computer to select the center position if the user does not
    #take the center position first based on the fact that the player that has the center spot has a better chance of winning in tic-tac-toe.
    if board[5] == " ":
        return 5
    
    else:
        #make a way by which the computer cannot occupy the same spot again
        while True:
            spot=random.randint(1,9)
            if board[spot] == " ":
                return spot
            
#call main  
main()
