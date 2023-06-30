import tkinter

FONT = ("Arial", 16)


def calculate_km():
    mile_input = float(no_of_miles.get())
    ans = round(mile_input * 1.60934, 2)
    km.config(text=f"{ans}")


window = tkinter.Tk()
window.title("Miles to Kilometers converter")
window.config()
window.minsize(width=400, height=100)

no_of_miles = tkinter.Entry(width=10)
no_of_miles.grid(column=1, row=0)

miles = tkinter.Label(text="Miles", font=FONT)
miles.config(padx=5)
miles.grid(column=2, row=0)

is_equal_to = tkinter.Label(text="is equal to", font=FONT)
is_equal_to.grid(column=0, row=1)

km = tkinter.Label(text="0")
km.grid(column=1, row=1)

kilometer = tkinter.Label(text="Km", font=FONT)
kilometer.grid(column=2, row=1)

calc = tkinter.Button(text="calculate", command=calculate_km)
calc.grid(column=1, row=2)

window.mainloop()
