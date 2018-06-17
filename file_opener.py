import tkinter
import os

root = tkinter.Tk()

text_var = tkinter.StringVar()
text_var2 = tkinter.StringVar()

path1 = r'C:\Users\dakil\Desktop\Arabic.txt'
path2 = r'C:\Users\dakil\Desktop\Italian.txt'


def main():
	window_conf('Test.', '180x50')

	# Textvariable, index, path, row, column
	text_box(text_var, 0, path1, 0, 0)
	text_box(text_var2, 1, path2, 1, 0)

	btn = tkinter.Button(text='Open', command=start_file)
	btn.grid(row=0, column=1)

	root.mainloop()


def window_conf(title, geometry):
	root.title(title)
	root.geometry(geometry)


def text_box(variable, index, path, row, column):
	box = tkinter.Entry(textvariable=variable)
	box.insert(index, path)
	box.grid(row=row, column=column, padx=5)

def start_file():
	os.startfile(text_var.get())
	os.startfile(text_var2.get())


if __name__ == '__main__':
	main()
