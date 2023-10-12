#Number Guessing Game Objectives:
from art import logo
import random
CORRECT_NUMBER = random.randint(1, 100)
GUESSED_NUMBER = 0
QTD_TRIES = 0
print(logo)

#Set the number of tries in the game
def difficulty_level():
  global QTD_TRIES
  choosen_difficulty = input("Choose a difficulty: type 'easy' or 'hard': ").lower()
  if choosen_difficulty == "easy":
    QTD_TRIES = 10
  elif choosen_difficulty == "hard":
    QTD_TRIES = 5
  else:
    print("Invalid choice.")
  return QTD_TRIES

#loop that will repeat until one of the two valid options is chosen
while QTD_TRIES != 10 and QTD_TRIES != 5:
  difficulty_level()

#function that will ask for the guessed number
def guessing_number():
  global GUESSED_NUMBER
  GUESSED_NUMBER = int(input("Please choose a number between 1 and 100: "))
  return GUESSED_NUMBER

#Loop that will run while the guessed number is incorrect, and there are still tries left.
while GUESSED_NUMBER != CORRECT_NUMBER and QTD_TRIES > 0:
  guessing_number()
  if GUESSED_NUMBER < CORRECT_NUMBER:
    print(f"Too low. Number of tries: {QTD_TRIES-1}")
    QTD_TRIES -=1
  elif GUESSED_NUMBER > CORRECT_NUMBER:
    print(f"Too high. Number of tries: {QTD_TRIES-1}")
    QTD_TRIES -=1


if GUESSED_NUMBER == CORRECT_NUMBER:
  print("Congratulations! You guessed right.")
if QTD_TRIES == 0:
  print(f"Sorry, you're out of tries. The correct answer was: {CORRECT_NUMBER}.")
