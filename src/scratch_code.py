import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()  # Hide the main window

var1 = '1'
var2 = '2'
var3 = '3'
var4 = '4'

variables = [var1, var2, var3, var4]
variable_names = [f'Variable {i+1}' for i in range(len(variables))]

selection = simpledialog.askstring("Input", f"Please select a variable: {', '.join(variable_names)}")
selected_var = variables[variable_names.index(selection)]
