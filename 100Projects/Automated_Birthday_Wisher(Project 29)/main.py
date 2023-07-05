import pandas
import datetime as dt
import random
import smtplib

email = "test@gmail.com"
password = "saanixjuyiwicsrp"

now = dt.datetime.now()
current_month = now.month
current_day = now.day

data = pandas.read_csv("birthdays.csv")

data_lst = data.to_dict("records")


for dictionary in data_lst:

    def send_mail():
        letters_lst = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        random_letter = random.choice(letters_lst)
        with open(file=f"letter_templates/{random_letter}") as letter:
            full_letter = letter.readlines()
            full_letter[0] = f"Dear {dictionary['name']},"
            updated_letter = "".join(full_letter)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=dictionary["email"],
                msg=f"Subject:Birthday Letter\n\n{updated_letter}"
            )


    if current_month in dictionary.values() and current_day in dictionary.values():
        send_mail()
