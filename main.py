
import random
import hangman_words
import hangman_art

print(hangman_art.logo)
chosen_word = (random.choice(hangman_words.word_list)).lower()


used_letters = ''
lives = 6
check = True
display = []

for letter in chosen_word:
    display += '_'
print(f"\n\t\t\t\t{' '.join(display)}\n")

while check:
    guess = input("Guess a letter: ").lower()
    
    if guess in used_letters:
        print(f"You have already guessed {guess}.\n")
        print(hangman_art.stages[lives])
        continue
            
    i = 0
    for letter in chosen_word:
        if letter == guess:
            display[i] = letter
        i += 1 
    
    if guess not in chosen_word:
        lives -= 1
        print(f"OOPs! Your guessed letter {guess} is not in the word.")
        if lives == 0:
            check = False
            print("\nOh! You lose.\n")
            print("\nThe word was:")
            print(f"\t\t\t{' '.join(chosen_word)}\n")
            
    if check != False:
        print(f"\n\t\t\t\t{' '.join(display)}\n")

    if '_' not in display:
        check = False
        print("Congratulations! You Won.")
    
    used_letters += guess
    print(hangman_art.stages[lives])
    
