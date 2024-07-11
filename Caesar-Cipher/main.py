import art
print(art.logo)
check = 'yes'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(word, shifts, direction):
  new_word = ''
  for i in range(0 , len(word)):
    if word[i] not in alphabet:
      new_word += word[i]
      continue
    for k in range (0 , 26):
      if alphabet[k] == word[i]:
        if direction == 'encode':
          if (k + shift) >= 26:
            new_word += (''.join(alphabet[k + shift - 26]))   
          else:
            new_word += (''.join(alphabet[k + shift]))
        elif direction == 'decode':
          if (k - shift) < 0:
            new_word += (''.join(alphabet[k - shift + 26]))   
          else:
            new_word += (''.join(alphabet[k - shift]))
      
  print(f"The {direction}ed text is {new_word}")

while check == 'yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction == 'encode' or direction == 'decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
      while shift > 26:
        shift -= 26
    elif shift < 0:
      while shift < 0:
        shift += 26
    caesar(word = text, shifts = shift, direction = direction)
  check = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()