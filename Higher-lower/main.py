from art import logo,vs
from game_data import data
import random
from replit import clear

data_A = 'Null'
data_B = 'Null'
Compair_A, Compair_B, count = 0 , 0 , 0
check = True

def select(A , B , A_followers , B_followers):
  if B == 'Null':
    index_for_B = random.randint(0,len(data)-1)
    B = data[index_for_B]['name'] + ', '+data[index_for_B]['description'] + ', '+data[index_for_B]['country']
    B_followers = data[index_for_B]['follower_count']
    index_for_A = random.randint(0,len(data)-1)
    A = data[index_for_A]['name'] + ', '+data[index_for_A]['description'] + ', '+data[index_for_A]['country']
    A_followers = data[index_for_A]['follower_count']
  else:
    A = B
    A_followers = B_followers 
    index_for_B = random.randint(0,len(data)-1)
    B = data[index_for_B]['name'] + ', '+data[index_for_B]['description'] + ', '+data[index_for_B]['country']
    B_followers = data[index_for_B]['follower_count']
  return A, B, A_followers, B_followers

def Comparison(Compair_A, Compair_B):
  if Compair_A >= Compair_B:
    return 'A'
  elif Compair_A < Compair_B:
    return 'B'

while check == True:
  print(logo)
  if count > 0:
    print(f"\nYour score is {count}.\n")
  data_A , data_B , Compair_A, Compair_B = select(A = data_A, B = data_B, A_followers = Compair_A, B_followers = Compair_B)
  compaired = Comparison(Compair_A = Compair_A, Compair_B = Compair_B)
  print(f"Compair A: {data_A}" )
  print(f"Followers of A are {Compair_A}.")
  print(vs)
  print(f"Compair B: {data_B}\n" )
  Guess = input("Who will have be having more followers on insta? type 'A' or 'B': ")
  if compaired == Guess:
    count += 1
    print(f'\nYou were right.\nYour score is {count}.')
  else:
    print(f'\nOh! You were wrong.\nYour score is {count}.')
    break
  clear()

print("Good bye")