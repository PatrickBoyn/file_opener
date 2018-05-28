import os, sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('File Opener')
        self.show()


def file_opener(*args):
    # List all of the files you want to open here. 
    files = []

    # For adding the arguments to the list.
    for a in args:
        files.append(a)
    # This is for opening all of my fsx files at once with one click.
    for b in files:
        os.startfile(b)
        # The print statement shows me if everything was read ok, if something
        # isn't opening correctly for example. 
        print(b)


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())

# Put the files paths in as parameters.
# file_opener(r'E:\Steam\steamapps\common\FSX\fsx.exe',
#             r'C:\Aerosoft\FSC9\FSC.exe', 
#             r'C:\Program Files (x86)\HiFi\AS16_FSX\AS16.exe',
#             r'C:\Program Files (x86)\rcv4x\rcv4.exe')
