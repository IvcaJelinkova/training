# hangman.py
# you have to guess the word
# Rules: 
    # 1. 6 chanches to guess
    # 2. 3 warnings (the letter was already guessed, not symbol)
    # 3. have list of available letters. If you choose letter, will be deleted from list
    # 4. ! --> get the list of words, which could be the word

# Import the random library
import random
import string

# The 'word_list' to test
test_word_list = ['sun', 'sky', 'water', 'fire', 'nature']


def load_words():
  """Load all words and return them in word_list. """
  word_list = open('words.txt', 'r').readline().split()
  return word_list

  
def choose_word_random(word_list):
  """Returns the random word from the 'word_list'"""
  return random.choice(word_list)

def is_word_guessed(gameword, letters_already_guessed):
  """Returns True, when the gameword is guessed. """
  if set(gameword) & set(letters_already_guessed) == set(gameword):
    return True
  else:
    return False


# Test the function
test_gameword = 'sunny'
test_letters_already_guessed = ['s', 'u', 'n', 'y']
print('Gameword is guessed:', is_word_guessed(test_gameword, test_letters_already_guessed))


def get_guessed_word(gameword, letters_already_guessed):
  """Takes the guess letter and controls, if it is in the gameword. If yes, adds it to result_list. If no, adds '_ '. """
  result_list = []
  for i in range(len(list(gameword))):
    # Set condition to check if elements of the 'gameword' equal to 'letters_already_guessed'
    if list(gameword)[i] in set(letters_already_guessed):
      # Append correct guessed letters to the 'result_list'
      result_list.append(list(gameword)[i])
    else:
      result_list.append('_ ')
  # Append the space to the 'result_list'
  return ''.join(result_list)

  
# Test the function  
test_gameword = 'sunny'
test_letters_already_guessed = ['n']
print('Get guessedword:', get_guessed_word(test_gameword, test_letters_already_guessed))

print('\n_________')
def get_available_letters(letters_already_guessed):
  """Returns the string contains of letters that haven't been used before.
  To help the user we show available letters after every guess. """
  available_list = list(string.ascii_lowercase)
  for i in range(-len(available_list), 0):
    if available_list[i] in letters_already_guessed:
      # Delete an element from the 'available_list' if it has been guessed
      del available_list[i]
  return ''.join(available_list)


# Test the function
test_letters_already_guessed = ['s', 'u', 'm', 'n', 'a']
print('Get available_letters:', get_available_letters(test_letters_already_guessed))


print('\n__________')
def hints_match(word_to_match, word_from_list):
  """Returns boolean True if letters and '_' from the word_to_match
  match corresponding letters from the word_from_list, False otherwise."""
  # Delete spaces in the 'word_to_match'
  test_list = list(word_to_match.replace(' ', ''))
  other_list = list(word_from_list)
  # Compare lengths of the 'test_list' and the 'other_list'
  if len(test_list) != len(other_list):
    # Return False
    return False
  else:
    counter = 0
    # Set 'for' loop to work with the 'test_list'
    for i in range(len(test_list)):
      if test_list[i] == '_':
        if other_list[i] not in test_list:
          # Increase the 'counter'
          counter += 1
      elif test_list[i] == other_list[i]:
        # Increase the 'counter'
        counter += 1
  if counter == len(word_to_match.replace(' ', '')):
    return True
  else:
    return False


# Test the function 
test_word_to_match = 's_ _ _ _' 
test_word_from_list = 'sunny'
print('Hint match:', hints_match(test_word_to_match, test_word_from_list))


print('\n__________')
def show_possible_matches(word_to_match):
  """Prints every word from the word_list, that matches word_to_match."""
  possible_matches=[]
  # Set 'for' loop to work with the elements of the 'test_word_list'
  for word in test_word_list:
    if hints_match(word_to_match, word):
      # Append an element to the 'possible matches' list_
      possible_matches.append(word)
  # Set condition if the 'possible_matches' list is empty
  if len(possible_matches) == 0:
    return 'No matches found'
  else:
    return ' '.join(possible_matches)


# Test the function
test_word_to_match = 's_ _ '
print('Show possible matches:', show_possible_matches(test_word_to_match))



print('\n__________')
def hangman(gameword):
  """Main body function. """
  letters_guessed = []
  guesses_remaining = 6
  warnings_remaining = 3
  print('Welcome!')
  print('A gameword is', len(gameword), 'letters long')

  while True:
    # Set condition if the word isn't guessed using the 'is_word_guessed' function
    if not is_word_guessed(gameword, letters_guessed):
      # Print the 'guesses_remaining' and the 'warnings_remaining'
      print('You have', int(guesses_remaining), 'guess(es) left and', int(warnings_remaining), 'warning(s) left!')
      # Print available letters
      print('Available letters: ', get_available_letters(letters_guessed))
      print('Game word: ', get_guessed_word(gameword, letters_guessed))
      print('------------------------------------------------')
      # Used to ask user to input the letter
      guess = str.lower(input('Please guess a letter: '))
      
      # Set condition if the 'guess' is not a letter
      if not guess.isalpha():
        # Here we will add code later
        pass
      # Set condition if the letter has been used already
      elif guess in set(letters_guessed):
        # Here we will add code later
        pass
      # Set condition if the letter is in the 'gameword'
      elif guess in set(gameword):
        # Here we will add code later
        pass
      # The letter is not in the 'gameword'
      else:
        # Here we will add code later
        pass

      # Set condition if the 'guesses_remaining' <= 0
      if guesses_remaining <= 0:
        # Print the 'gameword'
        print('Sorry, you ran out of guesses. The word was: ', gameword)
        break

    else:
      print('Congratulations, you won!')
      print('The gameword is: ', gameword)
      break



    