import tkinter as tk

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Stylish Calculator")
root.geometry("400x500")  # Set initial size

# Set background color
root.configure(bg='#f2f2f2')

# Entry widget to display input and results
entry = tk.Entry(root, width=16, font=('Arial', 20), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, pady=10) 

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add buttons to the grid with styling
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 16),
              command=lambda b=button: on_button_click(b) if b != '=' else calculate(),
              bg='#4CAF50', fg='white').grid(row=row_val, column=col_val)  # Set button color
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button with different color
tk.Button(root, text="C", padx=20, pady=20, font=('Arial', 16), command=clear_entry,
          bg='#ff3333', fg='white').grid(row=row_val, column=col_val)

# Run the Tkinter event loop
root.mainloop()
