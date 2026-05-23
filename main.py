# Create a random password generator that returns passwords composed of lowercase letters, uppercase letters, digits, and punctuations

import tkinter as tk
from tkinter import messagebox
import random as r

# commands
def password_generator():
        password = []
        uppercase = ["A", "B", "C", "D", "E", "F", "G", "H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        lowercase = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
        numbers = ["0", "1","2","3","4","5","6","7","8","9","10",]
        special = ["!","@","#","$","%","&"]
        length = r.randint(8, 20)
        for i in range(length):
                character = r.randint(1,4)
                if character == 1:
                        password.append(uppercase[r.randint(0, len(uppercase)-1)])
                elif character == 2:
                        password.append(lowercase[r.randint(0, len(lowercase)-1)])
                elif character == 3:
                        password.append(numbers[r.randint(0, len(numbers)-1)])
                else:
                        password.append(special[r.randint(0, len(special)-1)])
        print(password)

def show():
        messagebox.showinfo("password", password_generator())

# window parameters
window = tk.Tk()
window.title("Random Password Generator")
window.geometry("200x200")

# button
tk.Button(window, text = "Click to generate a random password!", width = 100, height = 50, command = show).pack()

window.mainloop()