import os
import sys
import datetime
import pandas as pd

class tools:
    """
        Contains all the utility methods for the application
    """
    def __init__(self):
        self.indexList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                         15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
        self.date = self.getDate()
        self.docsDir = ""
        self.rabtax = ""
        self.temp = ""
        self.controlState = ""
        self.indCounter = ""
        self.fileSearch()
        pass
    
    def getDate(self):
        cDate = datetime.date.today()
        return cDate.strftime("%d/%m/%Y")


    def fileSearch(self):
        # Move to the Documents directory within the current user account
        rPath = self.FrozenFile("")
        pList = rPath.split("\\")
        rPath = os.path.join(pList[0], "\\" + str(pList[1]))
        self.docsDir = os.path.join(rPath, pList[2] + "\\Documents")

        # Try to open the .csv file with pandas,
        # file is stored in /Documents/RABTAX.
        # Date is set for 2017, after this date
        # the condition will always fail leaving 
        # new years to be updated dynamically later
        try:
            os.chdir(os.path.join(self.docsDir, "RABTAX"))               
            rabtax = pd.read_csv('RABTAX2017.csv', index_col=0)
        
        # Catch exception (No file exists)  
        except FileNotFoundError:
            controlState = 0
            indCounter = self.indexList[0]
            rabtax = None
        
        # (File exists) Find the current index of the file
        else:
            controlState = 1                            # State indicating file exists
            indCounter = rabtax.index.max()             # Get maximum index of the dataframe
            if indCounter == 26:                        # Max value is 26 (Full year)
                indCounter = self.indexList[0]          # Reset counter to first element
                controlState = 2                        
            else:
                newIndex = self.indexList[0]            # Max value is not 26
                x = 0
                while newIndex != indCounter:           # Iterate through each index
                    newIndex = self.indexList[x + 1]    # until the current index is found
                    x += 1
                    continue
                else:
                    indCounter = self.indexList[x + 1]
        finally:                                        # Update object values with local values
            self.controlState = controlState
            self.indCounter = indCounter
            self.rabtax = rabtax

    def PdFrameCreator(self, date, rbchk, txded,
                       gas, extraExp):

        # Create new dictionary to more easily convert to Dataframe
        dFrameDict = {'Date': pd.Series([date], index=[self.indCounter]),
                      'Paycheck': pd.Series([rbchk], index=[self.indCounter]),
                      'TaxDeducted': pd.Series([txded], index=[self.indCounter]),
                      'Gas': pd.Series([gas], index=[self.indCounter])}

        # Add extra expenses given to the dictionary if any exist
        if extraExp:
            for key, val in extraExp.items():
                dFrameDict[key] = pd.Series([val], index=[self.indCounter])

        # Convert the dictionary to a Pandas dataframe
        self.temp = pd.DataFrame(dFrameDict)

    def PushtoFile(self):
        # Create new directory RABTAX, save dataframe to new file
        if self.controlState == 0:
            os.chdir(self.docsDir)
            os.mkdir('RABTAX')
            os.chdir(os.path.join(self.docsDir, 'RABTAX'))
            self.temp.to_csv('RABTAX2017.csv')

        # Updates existing file by appending dataframe to it
        elif self.controlState == 1:
            rbtax = self.rabtax.append(self.temp)
            os.chdir(os.path.join(self.docsDir, 'RABTAX'))
            rbtax.to_csv('RABTAX2017.csv')

        # Create new .csv file with name RABTAX + (New Year)
        if self.controlState == 2:
            newDate = datetime.strftime('%Y')
            os.chdir(os.path.join(self.docsDir, 'RABTAX'))
            df.to_csv('RABTAX' + str(newDate) + '.csv')

    def Reset(self):
        self.docsDir = ""
        self.rabtax = ""
        self.temp = ""
        self.controlState = ""
        self.indCounter = ""
