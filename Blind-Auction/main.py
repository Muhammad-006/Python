from replit import clear
import art
info = {}
name = ''
bid = 0
check = 'yes'
while check == 'yes':
  print(art.logo)
  name = input('What is the name of the bidder?\n')
  bid = int(input('The amount do you want to bid is: $'))
  check = input('Is there any other didder "yes" or "no"?\n').lower()
  info[name] = bid
  clear()
  
largest = 0
for i in info:
  if largest < info[i]:
    largest = info[i]
    name = i
print(f"The winner is {name} with the highest bid of ${largest}")
#HINT: You can call clear() to clear the output in the console.