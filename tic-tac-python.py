# An empty Tic-tac-toe board
class Board:
  def __init__(self):
    self.game_state = [['-', '-', '-'] for index in range(0, 3)]

  def __repr__(self):
    display = ''

    for row in self.game_state:

      for column in row:
        display += column + ' '

      display += '\n'

    return display

game_board = Board()

# Tracks if it is player 1's or player 2's turn
player_1_turn = True

# The markers for the players which can either by x or o
player_1_marker = ''
player_2_marker = ''

# Opening message
start_text = 'Welcome to Tic-tac-python!'

# Game Start
print(start_text)

# Loops until player 1 picks x or o
while player_1_marker != 'x' and player_1_marker != 'o':
  player_1_marker = input('Choose a marker (x or o): ')

  if player_1_marker != 'x' and player_1_marker != 'o':
    print('Please select x or o.')

# Give player 2 the opposite marker of player 1
if player_1_marker == 'x':
  player_2_marker = 'o'
else:
  player_2_marker = 'x'


# Display the intial game board
print(game_board)
