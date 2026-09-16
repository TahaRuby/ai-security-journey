# import

import tkinter as tk


# create window

window = tk.Tk()

window.title("Calculator")
window.geometry("300x400")


# calculator state

first_number = None
operator = None


# functions

def add_to_display(value):
    display.insert(tk.END, value)


def choose_operator(op):
    global first_number, operator

    first_number = float(display.get())
    operator = op

    display.delete(0, tk.END)


def calculate():
    global first_number, operator

    if first_number is None or operator is None:
        return

    try:
        second_number = float(display.get())

        if operator == "+":
            result = first_number + second_number

        elif operator == "-":
            result = first_number - second_number

        elif operator == "×":
            result = first_number * second_number

        elif operator == "÷":
            if second_number == 0:
                display.delete(0, tk.END)
                display.insert(0, "Error")
                first_number = None
                operator = None
                return

            result = first_number / second_number

        display.delete(0, tk.END)

        if result.is_integer():
            display.insert(0, int(result))
        else:
            display.insert(0, result)

        first_number = None
        operator = None

    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        first_number = None
        operator = None


def clear_display():
    global first_number, operator

    display.delete(0, tk.END)

    first_number = None
    operator = None


def add_decimal():
    current_value = display.get()

    if "." not in current_value:
        display.insert(tk.END, ".")


# display

display = tk.Entry(
    window,
    font=("Arial", 20),
    justify="right"
)

display.pack(
    padx=10,
    pady=20,
    fill="x"
)


# button frame

button_frame = tk.Frame(window)
button_frame.pack()


# number buttons

button_1 = tk.Button(
    button_frame,
    text="1",
    width=5,
    height=2,
    command=lambda: add_to_display("1")
)

button_2 = tk.Button(
    button_frame,
    text="2",
    width=5,
    height=2,
    command=lambda: add_to_display("2")
)

button_3 = tk.Button(
    button_frame,
    text="3",
    width=5,
    height=2,
    command=lambda: add_to_display("3")
)

button_4 = tk.Button(
    button_frame,
    text="4",
    width=5,
    height=2,
    command=lambda: add_to_display("4")
)

button_5 = tk.Button(
    button_frame,
    text="5",
    width=5,
    height=2,
    command=lambda: add_to_display("5")
)

button_6 = tk.Button(
    button_frame,
    text="6",
    width=5,
    height=2,
    command=lambda: add_to_display("6")
)

button_7 = tk.Button(
    button_frame,
    text="7",
    width=5,
    height=2,
    command=lambda: add_to_display("7")
)

button_8 = tk.Button(
    button_frame,
    text="8",
    width=5,
    height=2,
    command=lambda: add_to_display("8")
)

button_9 = tk.Button(
    button_frame,
    text="9",
    width=5,
    height=2,
    command=lambda: add_to_display("9")
)

button_0 = tk.Button(
    button_frame,
    text="0",
    width=5,
    height=2,
    command=lambda: add_to_display("0")
)


# operator buttons

button_plus = tk.Button(
    button_frame,
    text="+",
    width=5,
    height=2,
    command=lambda: choose_operator("+")
)

button_minus = tk.Button(
    button_frame,
    text="-",
    width=5,
    height=2,
    command=lambda: choose_operator("-")
)

button_multiply = tk.Button(
    button_frame,
    text="×",
    width=5,
    height=2,
    command=lambda: choose_operator("×")
)

button_divide = tk.Button(
    button_frame,
    text="÷",
    width=5,
    height=2,
    command=lambda: choose_operator("÷")
)


# extra buttons

button_clear = tk.Button(
    button_frame,
    text="C",
    width=5,
    height=2,
    command=clear_display
)

button_decimal = tk.Button(
    button_frame,
    text=".",
    width=5,
    height=2,
    command=add_decimal
)

button_equal = tk.Button(
    button_frame,
    text="=",
    width=5,
    height=2,
    command=calculate
)


# button positions

button_7.grid(row=0, column=0, padx=2, pady=2)
button_8.grid(row=0, column=1, padx=2, pady=2)
button_9.grid(row=0, column=2, padx=2, pady=2)
button_plus.grid(row=0, column=3, padx=2, pady=2)

button_4.grid(row=1, column=0, padx=2, pady=2)
button_5.grid(row=1, column=1, padx=2, pady=2)
button_6.grid(row=1, column=2, padx=2, pady=2)
button_minus.grid(row=1, column=3, padx=2, pady=2)

button_1.grid(row=2, column=0, padx=2, pady=2)
button_2.grid(row=2, column=1, padx=2, pady=2)
button_3.grid(row=2, column=2, padx=2, pady=2)
button_multiply.grid(row=2, column=3, padx=2, pady=2)

button_clear.grid(row=3, column=0, padx=2, pady=2)
button_0.grid(row=3, column=1, padx=2, pady=2)
button_decimal.grid(row=3, column=2, padx=2, pady=2)
button_divide.grid(row=3, column=3, padx=2, pady=2)

button_equal.grid(
    row=4,
    column=0,
    columnspan=4,
    sticky="ew",
    padx=2,
    pady=2
)


# start application

window.mainloop()