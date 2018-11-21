import tools
import rbgui
import msgbox
from PyQt5.QtGui import *
from PyQt5 import QtWidgets


class RBWindow(rbgui.Ui_MainWindow):
    """ Wrapper Class for PyQt Window script

        Contains methods for events driven by
        GUI buttons
    """
    
    def __init__(self):
        super(RBWindow, self).__init__()
        self.extraExpenses = {}         # Container for any extra expenses
        self.toolbox = tools.tools()    # Tools container class


    def OnStartClick(self):
        # Enable and disable starting gui objects
        self.primaryValuesBox.setEnabled(True)
        self.ExtraExpButton.setEnabled(True)
        self.StartButton.setEnabled(False)
        

    def OnSubmitClick(self):
        # Parse text values from gui
        name = self.lineEdit.text()
        value = self.lineEdit_2.text()

        # Simple input validation
        if  name == "" or  value == "":
            msgbox.App("Ensure you enter a Name and Value")
        else:
            self.extraExpenses[name] = value        # Update expenses dictionary

        # Clear the old values from the edit boxes
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
                  

    def OnEEClick(self):
        # Enable and diable gui objects pertaining to the extra expenses group
        self.ExtraExpensesBox.setEnabled(True)
        self.ExtraExpButton.setEnabled(False)
        self.DoneButton.setEnabled(True)

    
    def OnDoneClick(self):
        # Parse values for primary stats
        chkamt = self.amtEdit.text()
        date = self.dateEdit.text()
        gas = self.gasEdit.text()

        # Simple input validation for empty slots
        if chkamt == "" or date == "" or gas == "":
            self.amtEdit.setText("")
            self.gasEdit.setText("")
            self.dateEdit.setText("")
            msgbox.App("Ensure you enter all three values")
        else:
            # Push parsed values to dataframe creator
            self.toolbox.PdFrameCreator(date, chkamt, 
                                       (float(chkamt) * .2),
                                       gas,
                                       self.extraExpenses)

            self.toolbox.PushtoFile()       # Push dataframe file to newly created or existing .csv file
            rMsg = msgbox.App(_state= True)
            if rMsg.reset:
                self.AppReset()                 # Reset both toolbox and gui values for reentry               

    def AppReset(self):
        self.toolbox.Reset()
        self.extraExpenses = {}
        self.amtEdit.setText("")
        self.gasEdit.setText("")
        self.dateEdit.setText("")


      
        

        