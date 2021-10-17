board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]
key_dict = {"1":[0,0],"2":[0,1],"3":[0,2],"4":[1,0],"5":[1,1],"6":[1,2],"7":[2,0],"8":[2,1],"9":[2,2]}

def print_board(board):

  print(board[0][0]+" | "+board[0][1]+" | "+board[0][2]+" ")
  print("---------")
  print(board[1][0]+" | "+board[1][1]+" | "+board[1][2]+" ")
  print("---------")
  print(board[2][0]+" | "+board[2][1]+" | "+board[2][2]+" ")


def player_input(letter, position):
  board[key_dict[position][0]][key_dict[position][1]]=letter

def check_winner(board_values,position_status):
    if board_values[0][0] == board_values[0][1] == board_values[0][2] == position_status:
      return True
    elif board_values[1][0] == board_values[1][1] == board_values[1][2] == position_status:
      return True
      
    elif board_values[2][0] == board_values[2][1] == board_values[2][2] == position_status:
      return True
    
    elif board_values[0][0] == board_values[1][1] == board_values[2][2] == position_status:
      return True
  
    elif board_values[0][2] == board_values[1][1] == board_values[2][0] == position_status:
      return True
      
    elif board_values[0][0] == board_values[1][0] == board_values[2][0] == position_status:
      return True
      
    elif board_values[0][1] == board_values[1][1] == board_values[2][1] == position_status:
      return True
     
    elif board_values[0][2] == board_values[1][2] == board_values[2][2] == position_status:
      return True
    return False

  
def check_board(board):
 count = 0
 for i in range(3):
   for j in range (3):
    if board[i][j]==' ':
     count+=1
 trigger=count
 if trigger==0:
  return False
 else:
  return True


def main():
  print("Welcome to the game of Tic-Tac-Toe!")
  not_satisfied = True
  while not_satisfied:
    
    player1= input("Player 1, please put X in one of the location on the board: ")
    player_input("X",player1)
    if check_winner(board,"X"):
      not_satisfied = False
      print("Player 1 won!")
      break
    
    print_board(board)
    
    if check_board (board) == False :
      print("It's a tie!Game over...")
      break

    player2= input("Player 2, please put O in one of the location on the board: ")
    player_input("O",player2)
    if check_winner(board,"O"):
      not_satisfied =False
      print("Player 2 won!")
      break
    print_board(board)

    if check_board (board) == False :
      print("It's a tie!Game over...")
      break
    
main()
