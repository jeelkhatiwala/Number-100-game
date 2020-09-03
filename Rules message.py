import tkinter
from tkinter import messagebox

# hide main window
root = tkinter.Tk()
root.withdraw()

# message box display
messagebox.showinfo("Rules", """ •	The game will be played by a single player.
•	3The number will be generated separately between 
                    1-9( Even numbers or odd numbers).
•	Each tile will get limited addition moves(20).
•	the player can't use the numbers from nearby tiles.
•	Addition of numbers only From random numbers
                     generated above in box.
•	The game will End after one tile gets filled with 100 or
                     more than 100 or all tiles move completed.
•	Grid will be 1*8/10.
""")

root.mainloop()