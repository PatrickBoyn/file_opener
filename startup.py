from os import startfile
from file_opener import text_variable


def start_file():
	for i in text_variable:
		startfile(i.get())
