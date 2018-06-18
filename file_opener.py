# It's bad practice to import *, but I think it's ok
# in this case since it's such a small file.
from window_conf import *
import startup


def main():
	# Window title, dimensions.
	window_conf('File Opener', '180x70')

	# Textvariable, index, path, row, column
	text_box(text_var, 0, path1, 0, 0)
	text_box(text_var2, 1, path2, 1, 0)
	text_box(text_var3, 2, path3, 2, 0)

	button('Open', 0, 1, startup.start_file)

	root.mainloop()


if __name__ == '__main__':
	main()
