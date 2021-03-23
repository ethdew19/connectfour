array1 = [0,0,0,0,0,0,0]
array2 = [0,0,0,0,0,0,0]
array3 = [0,0,0,0,0,0,0]
array4 = [0,0,0,0,0,0,0]
array5 = [0,0,0,0,0,0,0]
array6 = [0,0,0,0,0,0,0]
columnlist = [1,2,3,4,5,6,7]

board = [array6,array5,array4,array3,array2,array1]

def display_board():
    for x in reversed(board):
        print(x)
    print(columnlist)

def player1_turn():
    display_board()
    print("Player 1 Enter your column")
    move_row = int(input()) - 1
    if board[5][move_row] != 0:
        print("Column is full, try again")
        player1_turn()
    else:
        make_move(move_row,1)

def player2_turn():
    display_board()
    print("Player 2 Enter your column")
    move_row = int(input()) - 1
    if board[5][move_row] != 0:
        print("Column is full, try again")
        player2_turn()
    else:
        make_move(move_row,2)


def make_move(column, player) :
    for x in range(len(board)):
        if board[x][column] == 0:
            board[x][column] = player
            if is_winner(column,x) :
                display_board()
                print("Player " + str(player) + " has won")
                game_over()
            elif player == 1:
                player2_turn()
            else:
                player1_turn()
                

            
            
    

def is_winner(x,y):
    going = True
    tracker = board[y][x]
    temp_x = x
    counter = 0
    #horizontal win
    while(going and temp_x > 0 ):
        temp_x =-1 
        if board[y][temp_x] != tracker:
            going = False
    going = True
    while (going and temp_x < 6):
        temp_x += 1
        if board[y][temp_x] != tracker:
            going = False
        else:
            counter+=1
    if counter >= 4:
        return True
    counter = 0
    going = True
    temp_y = y
    #vertical win
    while(going and temp_y > 0 ):
        temp_y =-1 
        if board[temp_y][x] != tracker:
            going = False
    going = True
    while (going and temp_y < 5):
        temp_y += 1
        if board[temp_y][x] != tracker:
            going = False
        else:
            counter+=1
    if counter >= 4:
        return True
    counter = 0
    #diagonal win 1
    temp_x = x
    temp_y = y
    going = True
    while(going and temp_x > 0 and temp_y > 0):
        temp_x -= 1
        temp_y -= 1
        if board[temp_y][temp_x] != tracker:
            going = False
    going = True
    while (going and temp_y < 5 and temp_x < 6) :
        if board[temp_y][temp_x] != tracker:
            going = False
        else:
            counter +=1
        temp_x +=1
        temp_y +=1
    if counter >= 4:
        return True
    #diagonal win 2
    counter = 0
    temp_x = x
    temp_y = y
    going = True
    while(going and temp_x > 0 and temp_y < 5):
        temp_x -= 1
        temp_y += 1
        if board[temp_y][temp_x] != tracker:
            going = False
    going = True
    while (going and temp_y >= 0 and temp_x < 6) :
        if board[temp_y][temp_x] != tracker:
            going = False
        else:
            counter +=1
        temp_x +=1
        temp_y -=1
    if counter >= 4:
        return True


def game_over():
    print("Game over")
    quit()
    

player1_turn()

    
