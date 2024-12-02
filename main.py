import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the title of the window
root.title("Basic RPG by Nate")

# Set window size (width x height)
root.geometry("500x500")

# Add a label to the window
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=50)

# Add a button to the window
button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
button.pack()

# Run the application
root.mainloop()