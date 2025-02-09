import time
import tkinter as tk

def countdown(n, label):
    def update_countdown():
        nonlocal n
        if n > 0:
            label.config(text=str(n))
            n -= 1
            label.after(1000, update_countdown)
        else:
            label.config(text="Countdown finished!")

    update_countdown()

def start_countdown():
    n = int(entry.get())
    countdown(n, label)

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("300x200")
root.configure(bg="lightblue")

# Create and place the widgets
entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=20)

start_button = tk.Button(root, text="Start Countdown", command=start_countdown, font=("Helvetica", 14), bg="green", fg="white")
start_button.pack(pady=10)

label = tk.Label(root, text="", font=("Helvetica", 18), bg="lightblue")
label.pack(pady=20)

# Run the application
root.mainloop()
