from widgets.main_screen import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys
from PyQt5 import QtGui as qtg


#the proper way would be make a folder inside here and store all the ui and ui components inside 
#a folder. You want to manage the comps from a python file; create class called main screen;

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
        self.file_select_button.clicked.connect(self.show_text)
        self.add_code_button.clicked.connect(self.add_code)
        #self.tag_it_button.clicked.connect(self.assign_code)
        self.show()
    
    def show_text(self):
        print('click')
        fname = qtw.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Text Files (*.txt *.pdf)")
        print(fname)
        lines = ''
        with open(fname[0]) as f:
            lines = f.read()
            print(lines)
        self.file_viewer.setPlainText(lines)
    
    # def show_img(self):
    #     print('click2')
    #     fname = qtw.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Text Files (*.txt *.png)")
    #     print(fname)
    #     lines = ''
    #     with open(fname[0]) as f:
    #         lines = f.read()
    #         print(lines)
    #     self.file_viewer.setPlainText(lines)
    
    def add_code(self):
        x = self.code_input_box.toPlainText() 
        print(x)
#        item = qtg.QListWidgetItem(x)
        self.code_list.addItem(x)
        self.code_input_box.setPlainText('')

    # def assign_code(self):
    #     cursor = qtg.QTextCursor.selectedText()
    #     print (cursor)


# class Highlighter(QSyntaxHighlighter):
#     def __init__(self, parent -> None):
#         super().__init__(parent)
#         self._mapping -> {}
#     
#     def add_mapping(self, pattern, pattern_format):
#         self._mapping[pattern] -> pattern_format
#     
#     def highlightBlock(self, text_block):
#         for patter, fmt in self._mapping.items(): 
# #fix_me!! based on syntax highlighting youtube video  


    

if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = MainWindow()
    app.exec()
