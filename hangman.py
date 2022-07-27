# hangman.py
# you have to guess the word
# Rules: 
    # 1. 6 chanches to guess
    # 2. 3 warnings (the letter was already guessed, not symbol)
    # 3. have list of available letters. If you choose letter, will be deleted from list
    # 4. ! --> get the list of words, which could be the word

# Import the random library
import random
# Import the string library
import string
# Set the 'load_words' function
def load_words():
  """Load all words and return them in word_list. """
  word_list = open('words.txt', 'r').readline().split()
  # Return the 'word_list'
  return word_list

  
def choose_word_random(word_list):
  """Return the random word from the 'word_list'"""
  return random.choice(word_list)

def is_word_guessed(gameword, letters_already_guessed):
  """Return True, when the gameword is guessed. """
  if set(gameword) & set(letters_already_guessed) == set(gameword):
    return True
  else:
    return False


# Test the function
test_gameword = 'sunny'
test_letters_already_guessed = ['s', 'u', 'n', 'y']
print(is_word_guessed(test_gameword, test_letters_already_guessed))


def get_guessed_word(gameword, letters_already_guessed):
  """Take the guess letter and control, if it in the gameword. If yes, add it to result_list. If no, add '_ '. """
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
print(get_guessed_word(test_gameword, test_letters_already_guessed))

