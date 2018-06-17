import tkinter
import os

root = tkinter.Tk()

text_var = tkinter.StringVar()
text_var2 = tkinter.StringVar()

path1 = r'C:\Users\dakil\Desktop\Arabic.txt'
path2 = r'C:\Users\dakil\Desktop\French.txt'


def main():
	window_conf('Test.', '180x50')

	box1 = tkinter.Entry(textvariable=text_var)
	box1.insert(0, path1)
	box1.grid(row=0, column=0, padx=5)

	box2 = tkinter.Entry(textvariable=text_var2)
	box2.insert(0, path2)
	box2.grid(row=1, column=0, padx=5)

	btn = tkinter.Button(text='Open', command=start_file)
	btn.grid(row=0, column=1, sticky='w')

	root.mainloop()


def window_conf(title, geometry):
	root.title(title)
	root.geometry(geometry)


def start_file():
	os.startfile(text_var.get())
	os.startfile(text_var2.get())


if __name__ == '__main__':
	main()
