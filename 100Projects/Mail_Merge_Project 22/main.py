with open(file="Input/Names/invited_names.txt") as names:
    list_of_names = names.readlines()
    for each_name in list_of_names:
        with open(file="Input/Letters/starting_letter.txt", mode="r") as letter:
            txt = letter.read()
            stripped_name = each_name.strip()
            replaced_text = txt.replace("[name]", f"{stripped_name}")
            with open(file=f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as invitation:
                invitation.write(replaced_text)
