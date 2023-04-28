import tkinter as tk
import json

# create a tkinter window
root = tk.Tk()

# read the JSON file and parse it into a Python data structure
with open('test_nimekirjad.json', 'r') as f:
    data = json.load(f)

# create a frame to hold the buttons
button_frame = tk.Frame(root)

# create a button for each entry in the JSON file
for entry in data:
    button = tk.Button(button_frame, text=entry)
    button.pack(side=tk.LEFT)

# pack the button frame in the window
button_frame.pack()

# start the tkinter event loop
root.mainloop()
