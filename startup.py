from os import startfile
from window_conf import text_variable


def start_file():
	for i in text_variable:
		startfile(i.get())
