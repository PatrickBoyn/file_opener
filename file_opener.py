import tkinter
import os

root = tkinter.Tk()

text_var = tkinter.StringVar()
text_var2 = tkinter.StringVar()
text_var3 = tkinter.StringVar()

# This is hard coded because these are the main ones
# I will use with this program. I wanted a GUI for easy change if I wanted to add,
# or change these files in the future.
path1 = r'E:\Steam\steamapps\common\FSX\fsx.exe'
path2 = r'C:\Program Files (x86)\HiFi\AS16_FSX\AS16.exe'
path3 = r'C:\Program Files (x86)\rcv4x\rcv4.exe'


def main():
	# Window title, dimensions.
	window_conf('File Opener', '180x70')

	# Textvariable, index, path, row, column
	text_box(text_var, 0, path1, 0, 0)
	text_box(text_var2, 1, path2, 1, 0)
	text_box(text_var3, 2, path3, 2, 0)

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
	print(path)


# TODO simplify this so that there is no repeated code.
def start_file():
	os.startfile(text_var.get())
	os.startfile(text_var2.get())
	os.startfile(text_var3.get())

if __name__ == '__main__':
	main()
