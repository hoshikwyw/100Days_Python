import tkinter as tk
from tkinter import messagebox
# shopping_list = ["Milk","Eggs","Bread","Banana","Apple","Orange"]

# shopping_list.append("Pineapple") # Add "Pineapple" to the end
# shopping_list.insert(0,"Strawberries") # Insert "Strawberries" at index 0
# shopping_list.remove("Eggs") # Remove the first occurrence of "Eggs"
# shopping_list.pop(3) # Remove the element at index 3

# print(shopping_list)

# for index, item in enumerate(shopping_list):
#     print(f"{index + 1}. {item}")
    
# shopping_list.sort() # Sort the list in alphabetical order
# shopping_list.reverse() # Reverse the order
# shopping_list.clear() # Clear the list


shopping_list = []

def view_items():
    if not shopping_list:
        messagebox.showinfo("Shopping List", "The shopping list is empty.")
    else:
        items = "\n".join([f"{index + 1}. {item}" for index, item in enumerate(shopping_list)])
        messagebox.showinfo("Shopping List", items)

def add_item():
    item = entry.get()
    if item:
        shopping_list.append(item)
        messagebox.showinfo("Shopping List", f"{item} has been added to the shopping list.")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter an item.")

def remove_item():
    item = entry.get()
    if item in shopping_list:
        shopping_list.remove(item)
        messagebox.showinfo("Shopping List", f"{item} has been removed from the shopping list.")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Item not found in the shopping list.")

def sort_list():
    if not shopping_list:
        messagebox.showinfo("Shopping List", "The shopping list is empty.")
    else:
        shopping_list.sort()
        messagebox.showinfo("Shopping List", "The shopping list has been sorted.")

def clear_list():
    shopping_list.clear()
    messagebox.showinfo("Shopping List", "The shopping list has been cleared.")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Shopping List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=0, padx=10)

add_button = tk.Button(frame, text="Add Item", command=add_item)
add_button.grid(row=0, column=1)

view_button = tk.Button(root, text="View Items", command=view_items)
view_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Item", command=remove_item)
remove_button.pack(pady=5)

sort_button = tk.Button(root, text="Sort List", command=sort_list)
sort_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear List", command=clear_list)
clear_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=5)

root.mainloop()