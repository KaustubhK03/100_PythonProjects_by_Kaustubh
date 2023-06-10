import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '{', '}', '@', '^', '_', '-', '?']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

ch_letter = []
ch_number = []
ch_symbols = []

for i in range(0, nr_letters):
    choice_letter = random.choice(letters)
    ch_letter.append(choice_letter)

for i in range(0, nr_numbers):
    choice_numbers = random.choice(numbers)
    ch_number.append(choice_numbers)

for i in range(0, nr_symbols):
    choice_symbols = random.choice(symbols)
    ch_symbols.append(choice_symbols)
combined_choices_list = ch_letter + ch_number + ch_symbols
random.shuffle(combined_choices_list)
password = ""
for char in combined_choices_list:
    password += char
print("Your Password could be: ", password)