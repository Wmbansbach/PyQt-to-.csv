from PyQt5.QtWidgets import QWidget, QMessageBox
import sys


class App(QWidget):
 
    def __init__(self, msg="", _state=False):
        super().__init__()
        self.msg = msg
        self.reset = False
        self.title = 'Error'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        if _state:
            self.setupUI()
        else:
            self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        buttonReply = QMessageBox.question(self, 'Input Error', self.msg, QMessageBox.Ok)
        self.show()



    def setupUI(self):
        buttonReply = QMessageBox.question(self, 'Finished?', "Would you like to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply != QMessageBox.Yes:
            sys.exit()
        else:
            self.reset = True
        
 
        