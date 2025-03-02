import tkinter as tk
import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*', '/'])
    if operation == '/':
        num1 = num1 * num2  # Ensure the division is always an integer
    question = f"{num1} {operation} {num2}"
    answer = eval(question)
    return question, answer

def check_answer(event=None):
    global score, question_count
    user_answer = answer_entry.get()
    if user_answer:
        if float(user_answer) == current_answer:
            result_label.config(text="Correct!", fg="green")
            score += 1
        else:
            result_label.config(text="Incorrect!", fg="red")
    else:
        result_label.config(text="Please enter an answer", fg="orange")
    
    question_count += 1
    if question_count < 5:
        root.after(2000, next_question)  # Wait 2 seconds before next question
    else:
        show_final_result()

def next_question():
    global current_question, current_answer
    current_question, current_answer = generate_question()
    question_label.config(text=current_question)
    answer_entry.delete(0, tk.END)
    result_label.config(text="")

def show_final_result():
    question_label.config(text="")
    answer_entry.pack_forget()
    # check_button.pack_forget()
    # next_button.pack_forget()
    result_label.config(text=f"Quiz Over! Your score: {score}/5", fg="blue")

# Initialize the main window
root = tk.Tk()
root.title("Math Quiz Game")

# Initialize game variables
score = 0
question_count = 0

# Create UI elements
question_label = tk.Label(root, text="", font=("Helvetica", 16))
question_label.pack(pady=20)

answer_entry = tk.Entry(root, font=("Helvetica", 16))
answer_entry.pack(pady=10)
answer_entry.bind("<Return>", check_answer)  # Bind Enter key to check_answer

# Remove check_button and next_button
# check_button = tk.Button(root, text="Check Answer", command=check_answer, font=("Helvetica", 16))
# check_button.pack(pady=10)

# next_button = tk.Button(root, text="Next Question", command=next_question, font=("Helvetica", 16))
# next_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=20)

# Start the game with the first question
next_question()

# Run the application
root.mainloop()
