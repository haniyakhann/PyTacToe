def playGame():

    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    turn = 1 #1 for X and 0 for O

    print()     
    print("Welcome to Tic Tac Toe <3")
    print()
    while True:
        printBoard(xState, zState)
        print()
        if turn == 1:
            print("X's chance")
            print()
            while True:
                value = int(input("Please enter a value (0-8): "))
                if value not in range(9) or xState[value] == 1 or zState[value] == 1:
                    print("Invalid input. Try again.")
                else:
                    xState[value] = 1
                    break
        else:
            print("O's chance")
            while True:
                value = int(input("Please enter a value (0-8): "))
                if value not in range(9) or xState[value] == 1 or zState[value] == 1:
                    print("Invalid input. Try again.")
                else:
                    zState[value] = 1
                    break

        cwin = checkWin(xState, zState)
        if cwin != -1:
            print("Match over.")
            break

        if all(xState[i] == 1 or zState[i] == 1 for i in range(9)):
            print("It's a draw!")
            break
        
        turn = 1 - turn
        
      

def printBoard(xState, zState):

    red = '\033[91m'  # Red color
    blue = '\033[94m'  # Blue color
    reset = '\033[0m'  # Reset to default color

    zero = f"{red}X{reset}" if xState[0] else (f"{blue}O{reset}" if zState[0] else '0')
    one = f"{red}X{reset}" if xState[1] else (f"{blue}O{reset}" if zState[1] else '1')
    two = f"{red}X{reset}" if xState[2] else (f"{blue}O{reset}" if zState[2] else '2')
    three = f"{red}X{reset}" if xState[3] else (f"{blue}O{reset}" if zState[3] else '3')
    four = f"{red}X{reset}" if xState[4] else (f"{blue}O{reset}" if zState[4] else '4')
    five = f"{red}X{reset}" if xState[5] else (f"{blue}O{reset}" if zState[5] else '5')
    six = f"{red}X{reset}" if xState[6] else (f"{blue}O{reset}" if zState[6] else '6')
    seven = f"{red}X{reset}" if xState[7] else (f"{blue}O{reset}" if zState[7] else '7')
    eight = f"{red}X{reset}" if xState[8] else (f"{blue}O{reset}" if zState[8] else '8')
      
    print(f"{zero} | {one} | {two}")
    print(f"--|---|---") 
    print(f"{three} | {four} | {five}")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight}")



def checkWin(xState, zState):

    wins = [0, 3, 6], [1, 4 ,7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2 , 4, 6]
    for win in wins:
        
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X won the match!")
            return 1
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O won the match!")
            return 0
    
    return -1



def sum(a, b, c):
    return a + b + c
  


def main():

    while True:
        playGame()
        restart = input("Do you want to play again? (yes/no): ").strip().lower()
        if restart != 'yes':
            print("Thank you for playing!")
            break    

main()