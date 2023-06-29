import pandas
nato_codes = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_codes.iterrows()}

name = input("Enter your name: ").upper()
name_lst = [letter for letter in name]
# print(name_lst)
list_of_phonetic_code = [nato_dict[letter] for letter in name]
print(list_of_phonetic_code)