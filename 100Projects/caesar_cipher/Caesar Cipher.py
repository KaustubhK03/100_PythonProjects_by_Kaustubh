from logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()


def caesar(start_text, shift_amount, cypher_direction):
    end_text = ""
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if cypher_direction == "encode":
                new_position = position + shift_amount
                if new_position > 25:
                    new_position = new_position % len(alphabet)
            else:
                new_position = position - shift_amount % 26
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {cypher_direction}d text is: {end_text}")


if direction == "encode" or direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    caesar(start_text=text, shift_amount=shift, cypher_direction=direction)
    restart = input("Do you want to restart the caesar cipher? Type yes or no: ").lower()
    while restart == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(start_text=text, shift_amount=shift, cypher_direction=direction)
        restart = input("Do you want to restart the caesar cipher? Type yes or no: ").lower()
else:
    print("Write either encode or decode!!!")
    exit()