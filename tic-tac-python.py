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

  def check_cats_game(self):
    marker_counter = 0

    for row in self.game_state:
      for column in row:
        if column != '-':
          marker_counter += 1

    if marker_counter == 9:
      return True
    else:
      return False

  def check_winner(self, marker):
    match_counter = 0

    for row in self.game_state:
      for column in row:
        if column == marker:
          match_counter += 1

      if match_counter == 3:
        return True
      else:
        match_counter = 0

    for column_index in range(0, 3):
      for row_index in range(0, 3):
        if self.game_state[row_index][column_index] == marker:
          match_counter += 1

      if match_counter == 3:
        return True
      else:
        match_counter = 0

    row_index = 0
    column_index =0

    while row_index <= 2 and column_index <= 2:
      if self.game_state[row_index][column_index] == marker:
        match_counter += 1

      row_index += 1
      column_index += 1

    if match_counter == 3:
      return True
    else:
      match_counter = 0

    row_index = 0
    column_index = 2

    while row_index <= 2 and column_index >= 0:
      if self.game_state[row_index][column_index] == marker:
        match_counter += 1

      row_index += 1
      column_index -= 1

    if match_counter == 3:
      return True
    else:
      return False

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

# Is there a winner
is_winner = False

# Is there a cats game
is_cats_game = False

# If the users want to play again
is_play_again = ''

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

  # Test if the input is valid
  is_valid_input = game_board.is_valid_space(player_input)

  if is_valid_input:
    # Set the marker on the board
    game_board.set_space(player_marker, player_input)

    # Check for a winner or cat's game
    is_winner = game_board.check_winner(player_marker)

    if is_winner and is_player_1_turn:
      print('Player 1 wins!')
    elif is_winner and not is_player_1_turn:
      print('Player 2 wins!')
    else:
      is_cats_game = game_board.check_cats_game()

      if is_cats_game:
        print("Cat's game!")

    # Ask to play again
    if is_winner or is_cats_game:
      # Display the board to show the end state
      print(game_board)

      while is_play_again != 'y' and is_play_again != 'n':
        is_play_again = input('Play again? (y or n): ')

        if is_play_again != 'y' and is_play_again != 'n':
          print('Please select y or n.')

      #if is_play_again == 'y':
        # reset the board
        # reset the player turn
        # ask to switch markers
        # if switch markers
          # switch the markers
    # Switch turns
    else:
      if is_player_1_turn:
        is_player_1_turn = False
      else:
        is_player_1_turn = True
  elif is_valid_input == False:
    print("That space is already taken.")
  else:
    print("Invalid space code.")

print('Thanks for playing!')
