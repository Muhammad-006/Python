
import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_dict = {attribute.letter: attribute.code for key, attribute in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input('Enter a word: ').upper()

nato_list = [data_dict[f'{letter}'] for letter in word if letter != ' ']
print(nato_list)
