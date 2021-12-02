from widgets.main_screen import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys
from PyQt5 import QtGui as qtg


#from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.Qt import QHelpEvent
from PyQt5.QtCore import Qt  # for context menu
from PyQt5.QtGui import QBrush, QColor, QSyntaxHighlighter, QTextCharFormat, QTextCursor
from codebook import CodeBook


#the proper way would be make a folder inside here and store all the ui and ui components inside 
#a folder. You want to manage the comps from a python file; create class called main screen;

#    app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

#below is aborted attempt to use QSyntaxHighlighter; 
# class SyntaxHighlighter(QSyntaxHighlighter):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.highlight_lines = {}
#         self.highlight_block = {}

#     def highlight_line(self, line_num, fmt):
#         if isinstance(line_num, int) and line_num >= 0 and isinstance(fmt, QTextCharFormat):
#             self.highlight_lines[line_num] = fmt # I don't undertand this line of code
#             block = self.document().findBlockByLineNumber(line_num)
#             self.rehighlightBlock(block)

#     def clear_highlight(self):
#         self.highlight_lines = {}
#         self.rehighlight()
    
#     def highlightBlock(self, block, fmt):
#         if isinstance(block, int) and block >= 0 and isinstance(fmt, QTextCharFormat):
#             self.highlight_lines[block] = fmt # I don't undertand this line of code
#             target_block = self.document().findBlock(block)
#             self.rehighlightBlock(target_block)
    
#     def highlightSelection(self, start_pos, end_pos):
#         print(start_pos)
#         print(end_pos)
#         return
        
    


    





class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.file_select_button.clicked.connect(self.show_text)
        self.add_code_button.clicked.connect(self.add_code)
        self.tag_it_button.clicked.connect(self.assign_code)
        self.code_list.clicked.connect(self.show_group_info)
        self.save_project_button.clicked.connect(self.save_project)
        #self.tag_it_button.clicked.connect(self.highlight_selection)
        self.codebook = CodeBook()
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

    def save_project(self):
        print('saving')
        progress = self.codebook.saveProject()
        print(progress)
    
    #fixme work on show_img todo
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
        z = len(self.code_list)
        print(z)
        self.codebook.addGroup(x)
        #item = QListWidgetItem(x) 
        self.code_list.addItem(x)
        self.code_input_box.setPlainText('')
        #I was making progress on setting different colors but I got stuck because I don't understand how to use the dictionary? 
        #I tried to use a list at first, but then I thought that I should be able to use the dictionary 
        # like with Tags, but I broke it; see also codebook and highlightColor classes;
        # 
        #colors = ['aliceblue', 'antiquewhite','aquamarine','azure','beige','lavender'] 	
        #nextColor = colors[z]
        #tag_colors_list = []
        #self.codebook.addTagColor(tag_colors_list)
        #self.codebook.setTagColor(nextColor)

        # y = self.codebook# this is a rabbit hole; there should be an easier way usinghte dictionary that R set up; fixme!
        # print(y)
        #w = self.codebook.getTagColors()
        #print('w:')
        #print(w)
        #print('')
        #print('test1:')
        #q = self.codebook.getGroupNameIndex(x)
        #print(q)
        
       

        #self.code_list.setCurrentItem()
        #self.show_group_info()

    def assign_code(self):
        select_text = self.file_viewer.textCursor()#I have now slected text! 
        z = select_text.selectedText()
        print(z)
        
        value = self.code_list.currentItem()
        group_name = value.text()
        tag_data = z

        self.codebook.addTag(tag_data, group_name)
        self.show_group_info()
        fmt = QTextCharFormat()
        # index_group_name = index(self.codebook[group_name])
        # print('index group name:')
        # print(index_group_name)
        #highlightColor = QColor('yellow')
        
        highlightColor = QColor(self.codebook.getColor(group_name))
        
        #highlightColor = QColor(nextColor)
        fmt.setBackground(highlightColor)
        #fmt.setBackground(QColor('yellow'))
        #self.file_viewer.setStyleSheet("selection-color: rgb(0,255,0); selection-background-color: rgb(255,0,0)") #this highlights selected text while it is selected...
        self.file_viewer.setCurrentCharFormat(fmt)

        
    def highlight_selection(self):
        selected_text = self.file_viewer.textCursor()
        x = selected_text.position()
        # blockNumber = self.file_viewer.textCursor()#blocks are separated by returns
        # x = blockNumber.blockNumber()
        print(x)
       
    def show_group_info(self):
        print("object")
        print(self.code_list)
        print("item")
        value = self.code_list.currentItem()
        group_name = value.text()
        print(group_name)
        print(self.codebook.getGroupInfo(group_name))
        self.memo_text.setPlainText(self.codebook.getPlainTextGroupInfo(group_name))
        print(self.codebook.getPlainTextGroupInfo(group_name))
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

# ['aliceblue', 'antiquewhite','aquamarine','azure','beige','lavender'] 	
#  			bisque		black(Safe 16 Hex3)	
# blanchedalmond	
#  	blue(Safe 16 Hex3)		blueviolet		brown	
# burlywood	
#  	cadetblue		chartreuse		chocolate	
# coral	
#  	cornflowerblue		cornsilk		crimson	
# cyan(Safe 16=aqua Hex3)	
#  	darkblue		darkcyan		darkgoldenrod	
# darkgray	
#  	darkgreen		darkgrey		darkkhaki	
# darkmagenta	
#  	darkolivegreen		darkorange		darkorchid	
# darkred	
#  	darksalmon		darkseagreen		darkslateblue	
# darkslategray	
#  	darkslategrey		darkturquoise		darkviolet	
# deeppink	
#  	deepskyblue		dimgray		dimgrey	
# dodgerblue	
#  	firebrick		floralwhite		forestgreen	
# fuchsia(Safe 16 Hex3)	
#  	gainsboro		ghostwhite		gold	
# goldenrod	
#  	gray(16)		green(16)		greenyellow	
# grey(16)	
#  	honeydew		hotpink		indianred	
# indigo	
#  	ivory		khaki			
# lavenderblush	
#  	lawngreen		lemonchiffon		lightblue	
# lightcoral	
#  	lightcyan		lightgoldenrodyellow		lightgray	
# lightgreen	
#  	lightgrey		lightpink		lightsalmon	
# lightseagreen	
#  	lightskyblue		lightslategray(Hex3)		lightslategrey(Hex3)	
# lightsteelblue	
#  	lightyellow		lime(Safe 16 Hex3)		limegreen	
# linen	
#  	magenta(Safe 16=fuchsia Hex3)		maroon(16)		mediumaquamarine	
# mediumblue	
#  	mediumorchid		mediumpurple		mediumseagreen	
# mediumslateblue	
#  	mediumspringgreen		mediumturquoise		mediumvioletred	
# midnightblue	
#  	mintcream		mistyrose		moccasin	
# navajowhite	
#  	navy(16)		oldlace		olive(16)	
# olivedrab	
#  	orange		orangered		orchid	
# palegoldenrod	
#  	palegreen		paleturquoise		palevioletred	
# papayawhip	
#  	peachpuff		peru		pink	
# plum	
#  	powderblue		purple(16)		red(Safe 16 Hex3)	
# rosybrown	
#  	royalblue		saddlebrown		salmon	
# sandybrown	
#  	seagreen		seashell		sienna	
# silver(16)	
#  	skyblue		slateblue		slategray	
# slategrey	
#  	springgreen		steelblue	
# tan	
#  	teal(16)			tomato	
# turquoise	
#  	violet	
    

if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = MainWindow()
    app.exec()
