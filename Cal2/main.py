import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("360x600")
root.title("Modern Calculator")
root.config(bg="#f0f4f8")
root.resizable(False, False)

btn_color = "#5b86e5"
btn_font = ("Segoe UI", 16)
btn_width = 4
btn_height = 2

def create_button(text, row, col, cmd=None, colspan=1):
    btn = tk.Button(
        root,
        text=text,
        command=cmd,
        width=btn_width * colspan,
        height=btn_height,
        font=btn_font,
        bg=btn_color,
        fg="white",
        activebackground="#b8b63d",
        activeforeground="white",
        bd=0,
        relief="flat"
    )
    btn.grid(row=row, column=col, columnspan=colspan, padx=6, pady=6, sticky="nsew")


text_result = tk.Text(root, height=2, width=20, font=("Segoe UI", 24), bg="#e2e8f0", fg="#0f172a", bd=0)
text_result.grid(columnspan=5, padx=10, pady=20)

buttons = [
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("+", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("*", 4, 3),
    ("(", 5, 0), ("0", 5, 1), (")", 5, 2), ("/", 5, 3),
]

for (text, r, c) in buttons:
   create_button(text, r, c, lambda t=text: add_to_calculation(t))

create_button("C", 6, 0, clear_field, colspan=2)
create_button("=", 6, 2, evaluate_calculation, colspan=2)

root.mainloop()
