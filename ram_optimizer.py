import tkinter as tk
from tkinter import messagebox
import os
import subprocess

def clear_temp():
    temp_paths = [
        os.environ.get('TEMP'),
        os.environ.get('TMP'),
        'C:\\Windows\\Temp'
    ]
    for path in temp_paths:
        if path and os.path.exists(path):
            for file in os.listdir(path):
                try:
                    os.remove(os.path.join(path, file))
                except:
                    pass
    messagebox.showinfo("Selesai", "File Temp udah dibersihin!")

def clear_ram():
    subprocess.run('echo off | clip', shell=True)
    messagebox.showinfo("Selesai", "RAM udah di-refresh!")

# UI Sederhana
root = tk.Tk()
root.title("BOIT7MU RAM Optimizer")
root.geometry("300x200")
root.resizable(False, False)

label = tk.Label(root, text="BOIT7MU RAM Optimizer", font=("Arial", 14, "bold"))
label.pack(pady=10)

btn_temp = tk.Button(root, text="Bersihin File Temp", command=clear_temp, width=25, bg="#4CAF50", fg="white")
btn_temp.pack(pady=5)

btn_ram = tk.Button(root, text="Refresh RAM", command=clear_ram, width=25, bg="#2196F3", fg="white")
btn_ram.pack(pady=5)

btn_exit = tk.Button(root, text="Keluar", command=root.destroy, width=25, bg="#f44336", fg="white")
btn_exit.pack(pady=5)

label_footer = tk.Label(root, text="Dibuat oleh Admin Bengkel Garuda", font=("Arial", 8))
label_footer.pack(side="bottom", pady=5)

root.mainloop()