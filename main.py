# Importing modules
import pandas
# Read file
data = pandas.read_csv('nato_phonetic_alphabet.csv')
# create object form data using object comprehension technique
nato_phonetic = {row.letter:row.code for (index, row) in data.iterrows()}
# Get word from the user
text = input('Entre the word: ')
# Create list of each first letter of the word
list_phonetic_of_text = [nato_phonetic[letter] for letter in text.upper() if letter != ' ']
print(f'[{text}] => {list_phonetic_of_text}')

