import os, sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('File Opener')
        self.le = QtWidgets.QLineEdit()
        self.b = QtWidgets.QPushButton('Open Files')

        self.b.clicked.connect(self, self.file_opener(r'E:\Steam\steamapps\common\FSX\fsx.exe'))

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b)

        self.setLayout(v_box)

        self.show()

    def file_opener(self, *args):
        # List all of the files you want to open here.
        self.files = []

        # For adding the arguments to the list.
        for a in args:
            self.files.append(a)
            # This is for opening all of my fsx files at once with one click.
            for b in self.files:
                os.startfile(b)
                # The print statement shows me if everything was read ok, if something
                # isn't opening correctly for example.
                print(b)


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
