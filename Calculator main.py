from tkinter import *
from tkinter import messagebox


# -----------------------------------------------------------------------------------#
def exit_window():
    if messagebox.askyesno(title="?", message="Do you want to exit?"):
        window.destroy()


def calculate():
    a = first_entry.get()
    b = second_entry.get()

    try:
        if var.get() == 1:
            messagebox.showinfo(title=f"{a} + {b}", message=f"{int(a) + int(b)} ")
            var.set(0)

        if var.get() == 2:
            messagebox.showinfo(title=f"{a} - {b}", message=f"{int(a) - int(b)} ")
            var.set(0)

        if var.get() == 3:
            messagebox.showinfo(title=f"{a} * {b}", message=f"{int(a) * int(b)} ")
            var.set(0)

        if var.get() == 4:
            messagebox.showinfo(title=f"{a} / {b}", message=f"{int(a) / int(b)} ")
            var.set(0)
    except ZeroDivisionError:
        messagebox.showerror(title="Invalid input", message="cannot be divided by zero")
    except ValueError:
        try:
            v = float(a)
        except ValueError:
            messagebox.showerror(title="Invalid input", message="Please provide valid entry in the first box")
            first_entry.focus_set()
        else:
            messagebox.showerror(title="Invalid input", message="Please provide valid entry in the second box")
            second_entry.focus_set()


# -----------------------------------------------------------------------------------#
window = Tk()
window.title("Mini Calculator")
window.minsize(width=130, height=130)
window.protocol("WM_DELETE_WINDOW", exit_window)

first_entry = Entry()
first_entry.grid(row=2, column=1, columnspan=2)

second_entry = Entry()
second_entry.grid(row=2, column=4, columnspan=2)

var = IntVar()
add_button = Radiobutton(text="+", variable=var, value=1)
add_button.grid(row=0, column=3)

subtract_button = Radiobutton(text="-", variable=var, value=2)
subtract_button.grid(row=1, column=3)

multiply_button = Radiobutton(text="*", variable=var, value=3)
multiply_button.grid(row=2, column=3)

divide_button = Radiobutton(text="/", variable=var, value=4)
divide_button.grid(row=3, column=3)

evaluate_button = Button(text="Evaluate", command=calculate)
evaluate_button.grid(row=4, column=3)

window.mainloop()
