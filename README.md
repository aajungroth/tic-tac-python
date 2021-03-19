# tic-tac-python

I have been working on Python 3 tutorials on Codecademy.
One of the projects was to write a terminal application in Python 3.
I decided to go with a two player Tic-Tac-Toe game.

I made a Board class to manage the game state.
The class had a two dimensional list to keep track of the nine spaces.
Each row had a letter 'a', 'b', or 'c' which I kept track of with dictionary.
The columns were numbered '1', '2', and '3'.
I also kept track of which spaces were still valid with a dictionary make
validation simple.

I used the Python's __repr__ method to print out a diagram of the board state.

I wrote a check_cats_game method to test if all of the spaces have been filled.

I used a check_winner method to check in row, column and both diagonals for
three of given marker in a row.

I set up an is_valid_space method that used the dictionary that kept track of
valid spaces. Any unused space returns True, used spaces return False, and
invalid spaces that are not on the board return None.

I had a reset_board method that cleared the game state back to an empty board
and reset the dictionary of valid spaces so users can play repeat games.

The final method was a set space method that would take a player marker and
set it to the correct position in the two dimensional array. It would also
mark that space as no longer valid.

I wrote a get_binary_answer function to get the answer to an question with two
options. This was useful for asking player one for there marker, either 'x' or
'o' and other yes and no questions. The function loops until the user picks
one of the two valid options.

The game starts by displaying a greeting, a valid move list and  prompting the
user to chose a marker, either 'x' or 'o'. I used the get_binary_answer
function to clean up the code for this.

Then the game enters a while loop. This loop will continue until players
finish the current game and chose to not start a new game. Each iteration of
the loop switches between player one and player two as the current player.

The players are prompted for a space code that maps to one of the nine spaces.
Each code has the row as a letter and the column as a number. The codes are
'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', and 'c3'.

The player's space code input is validated to make sure that it is valid. If
it is then, the code is used to mark that space on the board with the player's
maker.

Then the check_winner board method is used to check if the move resulted in
three in a row for that player. If there is no winner and it the board is not
full then the loop continues until either a player wins or the game ends in a
draw.

Once a player has won or cat's game has been reached the result is displayed
to the user. They are prompted to play another game. If they chose to play
another game then they are also asked if they want to switch markers. I used
the get_binary_answer function to avoid having to create the same while loops
and error handling code to make sure a 'y' or 'n' was inputted.

Once the player's decided to finish playing the game exits the while loop and
prints a 'thanks for playing' message.
