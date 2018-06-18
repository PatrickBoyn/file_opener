import os
from window_conf import *


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


def start_file():
	for i in text_variable:
		os.startfile(i.get())


if __name__ == '__main__':
	main()
