# Create a random password generator that returns passwords composed of lowercase letters, uppercase letters, digits, and punctuations

import tkinter as tk
import random as r

#command
# def password_generator():
#     for characters in range(r.randrange(8, 13)):
#         print(characters)


# # window parameters
# window = tk.Tk()
# window.title("Random Password Generator")
# window.geometry("200x200")

# # button
# tk.Button(window, text = "Click to generate a random password!", width = 100, height = 100, command = password_generator).pack()



# window.mainloop()

for characters in range(8, r.randint(8, 13)):
        print(characters)
