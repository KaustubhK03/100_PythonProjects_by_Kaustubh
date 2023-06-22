# import colorgram
#
# colours = colorgram.extract('Heirst_Painting.jpg.webp', 40)
# lst_colors = []
# for color in colours:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tup = (r, g, b)
#     lst_colors.append(tup)
# print(lst_colors)
import random
import turtle as t

bob = t.Turtle()
t.colormode(255)
lst_colors = [
    (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216),
    (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177),
    (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28),
    (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8),
    (233, 66, 34), (11, 97, 52), (169, 181, 232), (241, 169, 155), (252, 7, 40), (10, 84, 100), (63, 98, 8),
    (14, 51, 250), (250, 11, 8)
]
bob.hideturtle()
bob.penup()
bob.setposition(-300, -300)
bob.speed("fastest")


def dot_line():
    for i in range(10):
        bob.pencolor(random.choice(lst_colors))
        bob.dot(20)
        bob.forward(50)


i = -300
current_pos = bob.pos()
for _ in range(10):
    dot_line()
    bob.setposition(-300, i + 50)
    i = i + 50

bob.setposition(0, 0)
screen = t.Screen()
screen.exitonclick()
