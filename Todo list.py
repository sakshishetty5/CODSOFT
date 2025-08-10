import tkinter as tk
from tkinter import messagebox

# Functions
def add_task():
    task = entry_task.get().strip()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        new_task = entry_task.get().strip()
        if new_task:
            listbox_tasks.delete(selected_index)
            listbox_tasks.insert(selected_index, new_task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter updated text.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

# GUI Setup
root = tk.Tk()
root.title("To-Do List")

frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=40)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=5)

button_add = tk.Button(root, text="Add Task", width=15, command=add_task)
button_add.pack(pady=2)

button_update = tk.Button(root, text="Update Task", width=15, command=update_task)
button_update.pack(pady=2)

button_delete = tk.Button(root, text="Delete Task", width=15, command=delete_task)
button_delete.pack(pady=2)

root.mainloop()
