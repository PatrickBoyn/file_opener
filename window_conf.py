import tkinter

root = tkinter.Tk()

# TODO find a way of making this simpler.
text_var = tkinter.StringVar()
text_var2 = tkinter.StringVar()
text_var3 = tkinter.StringVar()

text_variable = [text_var, text_var2, text_var3]

# This is hard coded because these are the main ones
# I will use with this program. I wanted a GUI for easy change if I wanted to add,
# or change these files in the future.
path1 = r'C:\Users\dakil\Desktop\Italian.txt'
path2 = r'C:\Users\dakil\Desktop\test.txt'
path3 = r'C:\Program Files (x86)\rcv4x\rcv4.exe'

paths = [path1, path2, path3]


def window_conf(title, geometry):
	root.title(title)
	root.geometry(geometry)


def text_box(variable, index, path, row, column):
	box = tkinter.Entry(textvariable=variable)
	box.insert(index, path)
	box.grid(row=row, column=column, padx=5)
	print(path)


def button(text, row, column, command=None):
	btn = tkinter.Button(text=text, command=command)
	btn.grid(row=row, column=column)


def add_text_box():
	pass
