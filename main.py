from pathlib import Path
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys 
from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.origin_file_list = []
        self.asm_file_list = []
        self.dot_file_list = []
        # self.filelist = []
        # self.asm_file_list = []
        # self.dot_file_list = []
        # adding list of items to combo box 
        
        self.FileDialog= QtWidgets.QFileDialog(self.centralwidget)
        self.pushButton_originfile.clicked.connect(self.event_pushbtn_originFile_handler)
        self.pushButton_asmfile.clicked.connect(self.event_pushbtn_asmFile_handler)
        self.pushButton_dotfile.clicked.connect(self.event_pushbtn_dotFile_handler)
        
    def open_file_dialog(self):
        dialog = self.FileDialog
        dialog.setDirectory(r'.\\')
        dialog.setFileMode(dialog.FileMode.ExistingFiles)  # existing files
        dialog.setNameFilter("All Files (*.*);;Executables (*.exe);;Images (*.png *.xpm *.jpg);;Text files (*.txt);;XML files (*.xml)") 
        dialog.setViewMode(dialog.ViewMode.List)
        filelist = []
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                filelist=[str(Path(filename)) for filename in filenames]
                # test print file name when it is chosen
                for filename in filelist:
                    print((filename))
            return filelist
        
    def event_pushbtn_originFile_handler(self):
        filelist= self.open_file_dialog()
        self.origin_file_list.append([str(filename) for filename in filelist])
        # self.comboBox_originfile.clear()
        item = filelist[0]
        print(item)
        # setting current item 
        self.comboBox_originfile.setCurrentText(item)

        # self.comboBox_originfile.setDuplicatesEnabled(False) 
        self.comboBox_originfile.insertItems(0,self.origin_file_list[::-1][0])
        # bug duplicate values added to the combobox
        
    def event_pushbtn_asmFile_handler(self):
        filelist= self.open_file_dialog()
        self.asm_file_list.append([str(filename) for filename in filelist])
        # self.comboBox_originfile.clear()
        item = filelist[0]
        print(item)
        # setting current item 
        self.comboBox_asmfile.setCurrentText(item)

        # self.comboBox_originfile.setDuplicatesEnabled(False) 
        self.comboBox_asmfile.insertItems(0,self.asm_file_list[::-1][0])
        # bug duplicate values added to the combobox
        
    def event_pushbtn_dotFile_handler(self):
        filelist= self.open_file_dialog()
        self.dot_file_list.append([str(filename) for filename in filelist])
        # self.comboBox_originfile.clear()
        item = filelist[0]
        print(item)
        # setting current item 
        self.comboBox_dotfile.setCurrentText(item)

        # self.comboBox_originfile.setDuplicatesEnabled(False) 
        self.comboBox_dotfile.insertItems(0,self.dot_file_list[::-1][0])
        # bug duplicate values added to the combobox

        
def ShowWindow():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    ShowWindow()