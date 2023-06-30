import tkinter

FONT = ("Arial", 16)


def calculate_km():
    mile_input = float(no_of_miles.get())
    ans = round(mile_input * 1.60934, 2)
    km.config(text=f"{ans}")


# Window configuration.
window = tkinter.Tk()
window.title("Miles to Kilometers converter")
window.config()
window.minsize(width=400, height=100)

# Entry method to get the miles input form the user.
no_of_miles = tkinter.Entry(width=10)
no_of_miles.grid(column=1, row=0)

# The Miles Label
miles = tkinter.Label(text="Miles", font=FONT)
miles.config(padx=5)
miles.grid(column=2, row=0)

# THe is equal to Label
is_equal_to = tkinter.Label(text="is equal to", font=FONT)
is_equal_to.grid(column=0, row=1)

# The Result Label
km = tkinter.Label(text="0")
km.grid(column=1, row=1)

# Creating a KM label
kilometer = tkinter.Label(text="Km", font=FONT)
kilometer.grid(column=2, row=1)

# Create a calculate Button
calc = tkinter.Button(text="calculate", command=calculate_km)
calc.grid(column=1, row=2)

window.mainloop()
