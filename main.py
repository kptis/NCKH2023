import sys
from PyQt5 import QtWidgets, uic
from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.original_FileDialog= QtWidgets.QFileDialog(self.centralwidget)
        self.pushButton_originfile.clicked.connect(self.open_file_dialog)
        self.file_list_originfile = QtWidgets.QFileDialog(self.centralwidget) 
    def open_file_dialog(self):
        dialog = self.original_FileDialog
        dialog.setDirectory(r'.\\')
        dialog.setFileMode(dialog.FileMode.ExistingFiles)  # existing files
        dialog.setNameFilter("All Files (*.*)") 
        dialog.setViewMode(dialog.ViewMode.List)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                self.file_list.addItems([str(Path(filename)) for filename in filenames])
def ShowWindow():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    ShowWindow()