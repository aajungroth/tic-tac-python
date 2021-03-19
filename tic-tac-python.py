# Game board class
class Board:
  def __init__(self):
    self.game_state = [['-', '-', '-'] for index in range(0, 3)]
    self.row_code = {'a': 0, 'b': 1, 'c': 2}
    self.valid_code_list = {
      'a1': True,
      'b1': True,
      'c1': True,
      'a2': True,
      'b2': True,
      'c2': True,
      'a3': True,
      'b3': True,
      'c3': True
    }

  def __repr__(self):
    display = '  '
    row_list = list(self.row_code.keys())
    row_index = 0

    # The board columns
    for index in range(1, 4):
      display += str(index) + ' '

    display += '\n'

    # The board spaces
    for row in self.game_state:
      display += row_list[row_index] + ' '
      row_index += 1

      for column in row:
        display += column + ' '

      display += '\n'

    return display

  def is_valid_space(self, space):
    result = None

    if space in self.valid_code_list:
      result = self.valid_code_list[space]

    return result

  def set_space(self, marker, space):
    row = self.row_code[space[0]]
    column = int(space[1]) - 1
    self.game_state[row][column] = marker
    self.valid_code_list[space] = False

# An empty Tic-tac-toe board
game_board = Board()

# Tracks if the game is being player
is_game_running = True

# Tracks if it is player 1's or player 2's turn
is_player_1_turn = True

# The markers for the players which can either by x or o
player_1_marker = ''
player_2_marker = ''

# The current player's marker
player_marker = ''

# The current player's input on where to place a marker
player_input = ''

# Is the player input valid
is_input_valid = None

# Opening message
start_text = 'Welcome to Tic-tac-python!\n'
start_text += 'Valid space codes are: a1, a2, a3, b1, b2, b3, c1, c2, c3'

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

while is_game_running:
  # Display the game board
  print(game_board)

  if is_player_1_turn:
    print("Player 1's turn")
    player_marker = player_1_marker
  else:
    print("Player 2's turn")
    player_marker = player_2_marker

  # Get input
  player_input = input('Select a space code (letter + number): ')

  is_valid_input = game_board.is_valid_space(player_input)

  if is_valid_input:
    game_board.set_space(player_marker, player_input)

    # check for winner
    # if there is a winner (or cat's game)
      # display the winner
      # ask to play again
      # if play again
        # reset the board
        # reset the player turn
        # ask to switch markers
        # if switch markers
          # switch the markers
    # else
    if is_player_1_turn:
      is_player_1_turn = False
    else:
      is_player_1_turn = True
  elif is_valid_input == False:
    print("That space is already taken.")
  else:
    print("Invalid space code.")

print('Thanks for playing!')
