import sys
import rbguiwrapper as gui
from PyQt5 import QtWidgets 


def main():
    application = QtWidgets.QApplication(sys.argv)
    windowObj = QtWidgets.QMainWindow()
    appWindow = gui.RBWindow()
    appWindow.setupUi(windowObj)
    windowObj.show()
    sys.exit(application.exec_())

if __name__ == "__main__":
    main()