from widgets.main_screen import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

#the proper way would be make a folder inside here and store all the ui and ui components inside 
#a folder. You want to manade the comps from a python file; create class called main screen;

#    app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = MainWindow()
    app.exec()
