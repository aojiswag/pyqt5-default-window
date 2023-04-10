from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import os


UI_PATH = os.path.dirname(os.path.realpath(__file__)) + "\\gui\\main.ui"


class MainWindow(QMainWindow, uic.loadUiType(UI_PATH)[0]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = MainWindow()
    myApp.show()
    sys.exit(app.exec_())