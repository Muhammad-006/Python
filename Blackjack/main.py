############### Blackjack Project #####################
import art
import random
print(art.logo)

def you_Blackjack(your_cards, sum_your_cards):
  print(f"You have {your_cards}")
  print(f"You have {sum_your_cards} points.\n")
  print("Your BlackJack!")
  print("Congratulations! You won.")

def draw(your_cards, sum_your_cards, computer_cards, sum_computer_cards):
  print(f"You have {your_cards}")
  print(f"You have {sum_your_cards} points.\n")
  print(f"Computer has {computer_cards}")
  print(f"Computers has {sum_computer_cards} points.\n")
  print("Oh! It's a draw.")

def you_bust(your_cards, sum_your_cards):
  print(f"You have {your_cards}")
  print(f"You have {sum_your_cards} points.\n")
  print("You Bust!")
  print("Oh! You lose.")

def Computer_Blackjack(computer_cards, sum_computer_cards):
  print(f"Computer has {computer_cards}")
  print(f"Computers has {sum_computer_cards} points.\n")
  print("Computer's BlackJack!")
  print("Oh! You lose.")

def Computer_Bust(computer_cards, sum_computer_cards):
  print(f"Computer has {computer_cards}")
  print(f"Computers has {sum_computer_cards} points.\n")
  print("Computer's Bust!")
  print("Congratulations! You won.")

def sum(turn):
  sum_cards = 0
  if turn == 'your':
    for i in your_cards:
      sum_cards += i
  else:
    for i in computer_cards:
      sum_cards += i
  return sum_cards

deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
your_cards = []
computer_cards = []
Other_player_cards = []
temp = 0 

def computer_game():
  your_cards.append(random.choice(deck))
  your_cards.append(random.choice(deck))
  sum_your_cards = sum('your')
  print(f"You have {your_cards}")
  print(f"You have {sum_your_cards} points.\n")
  if sum_your_cards == 21:
    computer_cards.append(random.choice(deck))
    computer_cards.append(random.choice(deck))
    sum_computer_cards = sum ('computer')
    print(f"Computers one card is {computer_cards[0]}")
    print(f"Computers has {computer_cards[0]} points.\n")

    print("Your BlackJack!")
    print("Congratulations! You won.")
    return
  computer_cards.append(random.choice(deck))
  computer_cards.append(random.choice(deck))
  sum_computer_cards = sum ('computer')
  print(f"Computers one card is {computer_cards[0]}")
  print(f"Computers has {computer_cards[0]} points.\n")

  choice = 'hit'
  check = True
  while check == True:
    if choice == 'hit': 
      print("So you want to hit, or you want to stand?")
      choice = input("Type 'hit' to hit, and 'stand' to stand: ").lower()
      print("\n")
    if choice == 'hit':
      your_cards.append(random.choice(deck))
      sum_your_cards = sum('your')
      if sum_your_cards == 21:
        print(f"Computer has {computer_cards}")
        print(f"Computers has {sum_computer_cards} points.\n")
        computer_cards.append(random.choice(deck))
        sum_computer_cards = sum ('computer')
        print(f"Computer has {computer_cards}")
        print(f"Computers has {sum_computer_cards} points.\n")
        if sum_computer_cards == 21:
          draw(your_cards, sum_your_cards, computer_cards, sum_computer_cards)
          return
        else:
          sum_your_cards = sum('your')
          you_Blackjack(your_cards, sum_your_cards)
          return
      elif sum_your_cards > 21:
        if 11 not in your_cards:
          sum_your_cards = sum('your')
          you_bust(your_cards, sum_your_cards)
          return
        else:
          print(f"You have {your_cards}")
          print(f"You have {sum_your_cards} points.\n")
          your_cards[your_cards.index(11)] = 1
          sum_your_cards = sum('your')
          print(f"You have {your_cards}")
          print(f"You have {sum_your_cards} points.\n")
      elif sum_your_cards < 21:
        sum_your_cards = sum('your')
        print(f"You have {your_cards}")
        print(f"You have {sum_your_cards} points.\n")
      continue
    elif choice == 'stand':
      print(f"Computer has {computer_cards}")
      sum_computer_cards = sum ('computer')
      print(f"Computers has {sum_computer_cards} points.\n")
      if sum_computer_cards <= 16:
        computer_cards.append(random.choice(deck))
        sum_computer_cards = sum ('computer')
        if sum_computer_cards == 21:
          Computer_Blackjack(computer_cards, sum_computer_cards)
          return
        elif sum_computer_cards > 21:
          if 11 not in computer_cards:
            sum_computer_cards = sum ('computer')
            Computer_Bust(computer_cards, sum_computer_cards)
            return
          else:
            print(f"Computer has {computer_cards}")
            print(f"Computers has {sum_computer_cards} points.\n")
            computer_cards[computer_cards.index(11)] = 1
            sum_computer_cards = sum ('computer')
            print(f"Computer has {computer_cards}")
            print(f"Computers has {sum_computer_cards} points.\n")
        continue
      elif sum_computer_cards > 16:
        sum_your_cards = sum('your')
        sum_computer_cards = sum ('computer')
        if sum_your_cards > sum_computer_cards:
          you_Blackjack(your_cards, sum_your_cards)
          return
        elif sum_your_cards < sum_computer_cards:
          Computer_Blackjack(computer_cards, sum_computer_cards)
          return 
        elif sum_your_cards == sum_computer_cards:
          draw(your_cards, sum_your_cards, computer_cards, sum_computer_cards)
          return

      if sum_computer_cards == 21:
        sum_computer_cards = sum ('computer')
        print(f"You have {your_cards}")
        print(f"You have {sum_your_cards} points.\n")
        Computer_Blackjack(computer_cards, sum_computer_cards)
        return


computer_game()

