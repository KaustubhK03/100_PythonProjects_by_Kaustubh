from flask import Flask
import random

rand_num = random.randint(0, 9)

app = Flask(__name__)


@app.route('/')
def guess_a_number():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbG5wZGE0YXk2a25uNDdmZW5yczZ3bXdodHcwa' \
           'WE4MjhocXBwa3F5OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/u4TIBIUrKRMajt6eqz/giphy.gif" width=400 ' \
           'height=600>'


@app.route('/url/<int:num>')
def check_number(num):
    if num == rand_num:
        return '<h1 style="color: green">You found me</h1>' \
                '<img src="https://media3.giphy.com/media/E3GKhFfMDjy1y/giphy.gif?cid=ecf05e476m62gy43he600jpeg4h' \
               'f9qjf17iehq9wtwofk7vl&ep=v1_gifs_search&rid=giphy.gif&ct=g">'
    elif num > rand_num:
        return '<h1 style="color: red">Too High!</h1>' \
                '<img src="https://media1.giphy.com/media/tXG1bTpN7uz839gSZA/giphy.gif?cid=ecf05e47xt0cdr4a' \
                'nso2zkgmx0yjb6y0u4kis1ckf4j4gk4t&ep=v1_gifs_search&rid=giphy.gif&ct=g">'
    else:
        return '<h1 style="color: purple">Too Low</h1>' \
                '<img src="https://media2.giphy.com/media/l0Exs4BQWa7iCPf20/giphy.gif?cid=ecf05e474yrt42yr6' \
                '7tp77vecritegw5figg91fqjhrkkol2&ep=v1_gifs_search&rid=giphy.gif&ct=g">'


if __name__ == "__main__":
    app.run(debug=True)
