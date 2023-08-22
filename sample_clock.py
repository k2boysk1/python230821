import tkinter as tk
from time import strftime

def update_time():
    time_str = strftime('%Y-%m-%d %H:%M:%S %p')
    time_label.config(text=time_str)
    time_label.after(1000, update_time)  # Update every 1000ms (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the time
time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
time_label.pack(anchor='center')

# Update the time label
update_time()

# Run the main loop
root.mainloop()
