# Assume that player 1 always chooses 'x' and 2 always chooses 'o'

board = [[None, None, None], [None, None, None], [None, None, None]]


def welcome_msg():
    """

    :return: String that welcomes the user
    """
    return "=" * 21 + "\n*      Welcome      *\n" + "=" * 21


def map_position(pos, player_num):
    global board
    if player_num == 1:

        if pos == 1 and board[0][0] is None:
            board[0][0] = 'x'
        elif pos == 2 and board[0][1] is None:
            board[0][1] = 'x'
        elif pos == 3 and board[0][2] is None:
            board[0][2] = 'x'
        elif pos == 4 and board[1][0] is None:
            board[1][0] = 'x'
        elif pos == 5 and board[1][1] is None:
            board[1][1] = 'x'
        elif pos == 6 and board[1][2] is None:
            board[1][2] = 'x'
        elif pos == 7 and board[2][0] is None:
            board[2][0] = 'x'
        elif pos == 8 and board[2][1] is None:
            board[2][1] = 'x'
        elif pos == 9 and board[2][2] is None:
            board[2][2] = 'x'
        else:
            print "Invalid location or location already filled"
    elif player_num == 2:
        if pos == 1 and board[0][0] is None:
            board[0][0] = 'o'
        elif pos == 2 and board[0][1] is None:
            board[0][1] = 'o'
        elif pos == 3 and board[0][2] is None:
            board[0][2] = 'o'
        elif pos == 4 and board[1][0] is None:
            board[1][0] = 'o'
        elif pos == 5 and board[1][1] is None:
            board[1][1] = 'o'
        elif pos == 6 and board[1][2] is None:
            board[1][2] = 'o'
        elif pos == 7 and board[2][0] is None:
            board[2][0] = 'o'
        elif pos == 8 and board[2][1] is None:
            board[2][1] = 'o'
        elif pos == 9 and board[2][2] is None:
            board[2][2] = 'o'
        else:
            print "Invalid location or location already filled"
    else:
        print "Invalid Player"

def chk_draw_condtn():
    if board[0][0]!=None and board[0][1]!=None and board[0][2]!=None and board[1][0]!=None and board[1][1]!=None and board[1][2]!=None and board[2][0]!=None and board[2][1]!=None and board[2][2]!=None:
        return True
    else:
        return False

def chk_winning_condtn():
    if (board[0][0] == board[0][1] == board[0][2] == 'x') or (board[0][0] == board[0][1] == board[0][2] == 'o'):
        return True
    elif (board[1][0] == board[1][1] == board[1][2] == 'x') or (board[1][0] == board[1][1] == board[1][2] == 'o'):
        return True
    elif (board[2][0] == board[2][1] == board[2][2] == 'x') or (board[2][0] == board[2][1] == board[2][2] == 'o'):
        return True
    elif (board[0][0] == board[1][0] == board[2][0] == 'x') or (board[0][0] == board[1][0] == board[2][0] == 'o'):
        return True
    elif (board[0][1] == board[1][1] == board[2][1] == 'x') or (board[0][1] == board[1][1] == board[2][1] == 'o'):
        return True
    elif (board[0][2] == board[1][2] == board[2][2] == 'x') or (board[0][2] == board[1][2] == board[2][2] == 'o'):
        return True
    elif (board[0][0] == board[1][1] == board[2][2] == 'x') or (board[0][0] == board[1][1] == board[2][2] == 'o'):
        return True
    elif (board[0][2] == board[1][1] == board[2][0] == 'x') or (board[0][2] == board[1][1] == board[2][0] == 'o'):
        return True
    else:
        return False


# 00 01 02
# 10 11 12
# 20 21 22

print welcome_msg()
# raw_input("\nEnter player 1's position (0,1,2,3,4,5) :")
while True:
    posA = input("Player 1's turn : \n===================== \n")
    map_position(posA, 1)

    if chk_winning_condtn():
        print "Player 1 won the game"
        break
    elif chk_draw_condtn():
        print "It's a draw"
        break

    print board
    print "\n\n"+"="*10

    posB = input("Player 2's turn : \n===================== \n")
    map_position(posB, 2)

    if chk_winning_condtn():
        print "Player 2 won the game"
        break
    elif chk_draw_condtn():
        print "It's a draw"
        break

    print board
    print "\n\n" + "=" * 10


