#tic tac toe 
player_1_symb=''
player_2_symb=''
board = [[None,None,None],[None,None,None],[None,None,None]]


def welcome_message():
    """
    Function to just greet the Player.
    """
    print "="*21
    print "*"*7+"Welcome"+"*"*7
    print "="*21
    
    

"""def choice_of_symbol():
    """
    #Get the choice of the symbol
    """
    global player_1_symb
    global player_2_symb
    player_1_symb=raw_input("Choose '1' or '0' as the symbol for player 1 : ")
    if player_1_symb =='1':
        player_2_symb='0'
    else:
        player_2_symb='1'"""

def pos_map(num,symbol):
    global board
    if num==1:
        board[0][1]=symbol
    elif num==2:
        board[0][2]=symbol
    elif num==3:
        board[0][3]=symbol
    elif num==4:
        board[1][1]=symbol
    elif num==5:
        board[1][2]=symbol
    elif num==6:
        board[1][3]=symbol
    elif num==7:
        board[2][1]=symbol
    elif num==8:
        board[2][2]=symbol
    elif num==9:
        board[2][3]=symbol
    else:
        print "Invalid Position entered."
    

def get_input():
    print "Input the position at which you want to place "
    print "\n 1 | 2 | 3 \n"+"-"*11+"\n 4 | 5 | 6 \n"+"-"*11+"\n 7 | 8 | 9 \n"
    
        
        
welcome_message()
get_input()


while (True):
    print ("\n"+"="*15+"\nPlayer 1's turn"+"\n"+"="*15)
    print raw_input("\nEnter the position : ")
    get_input()
    pos2=raw_input("Player 1's turn")
    get_input()
    pos_map(pos1,'x')
    pos_map(pos2,'0')
    
