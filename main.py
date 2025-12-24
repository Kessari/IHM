from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from PySide6.QtUiTools import loadUiType
MainUI , _ = loadUiType('./mainui.ui')



class MainApp(QMainWindow,MainUI):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)





def main():
    app = QApplication()
    win = MainApp()
    win.show()
    app.exec()
if '__main__'  ==  __name__:
    main()
