#TODO: Create a letter using starting_letter.txt
with open('./Input/Names/invited_names.txt', mode='r')as names:
    names_to_use = names.read().split('\n')
with open('./Input/Letters/starting_letter.txt', mode='r')as letter_prototype:
    words_to_use = letter_prototype.read()
    for name in names_to_use:
        new_letter = words_to_use.replace('[name],', f"{name},")
        with open(f'./Output/ReadyToSend/Letter_for_{name}.txt', mode='w') as letter:
            letter.write(new_letter)






#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
