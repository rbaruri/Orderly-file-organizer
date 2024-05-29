import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from ttkbootstrap import Style
from tkinter import ttk


def organize_files(path):
    try:
        files = os.listdir(path)
    except FileNotFoundError:
        messagebox.showerror("Error", "The specified directory does not exist.")
        return

    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]  

        if extension:  
            dest_dir = os.path.join(path, extension)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            shutil.move(os.path.join(path, file), os.path.join(dest_dir, file))

    messagebox.showinfo("Success", "Files have been organized.")


def select_directory():
    path = filedialog.askdirectory()
    if path:
        organize_files(path)


root = tk.Tk()
style = Style(theme='superhero')  
root.title("Orderly")
root.iconbitmap("myicon.ico")


window_width = 300
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 3


root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.resizable(False, False)



frame = ttk.Frame(root, padding="20 20 20 20")
frame.pack(expand=True, fill='both')

label = ttk.Label(frame, text="Select a directory to organize files")
label.pack(pady=10)

select_btn = ttk.Button(frame, text="Select Directory", command=select_directory)
select_btn.pack(pady=10)


root.mainloop()
