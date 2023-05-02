import tkinter as tk

root = tk.Tk()

text = tk.Text(root, height=10, width=50)
text.pack()

# List of texts to insert into the text widget
texts = ["This is row 1", "This is row 2", "This is row 3"]

# Insert each text into a new row in the text widget
for text in enumerate(texts):
    text_row = str(i + 1) + ".0"
    text_col = "end"
    text_index = text_row + "." + text_col
    text_widget.insert(text_index, text + "\n")

root.mainloop()
