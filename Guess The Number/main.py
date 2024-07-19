#Number Guessing Game Objectives:
import art
import random
print (art.logo)

def Your_Choice():
  Guess = int(input("What's your guess? "))
  return Guess
  
def selected():
  Number = random.randint(1, 100)
  return Number

def Total_Turns(difficulty):
  if difficulty == 'easy':
    return 10
  elif difficulty == 'hard':
    return 5

def Turns_left(Turns):
  Turn = Turns - 1
  return Turn

def compare(Yours, Num):
  if Yours == Num:
    return 'Congratulations! You have found the number.'
  elif Yours > Num:
    return 'Too High.'
  else:
    return 'Too Low.'


Given = selected()
print("The chosen number is between 1 to 100.\n")
difficulty = input("Chose difficulty 'easy' or 'hard': ")
Total = Total_Turns(difficulty)
print(f"\nYou have {Total} turns.")
Turn = Turns_left(Total) + 1
while Turn != 0:
  Your_Guess = Your_Choice ()
  print(f"\n{compare(Num = Given, Yours = Your_Guess)}")
  if compare(Num = Given, Yours = Your_Guess) == 'Congratulations! You have found the number.':
    break
  Turn = Turns_left(Turn)
  print(f"\nYou have {Turn} turns left.")
  if Turn == 0:
    print ("\nOOPs! you ran out off Turns.")
    print(f"The chosen number was {Given}.")
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

