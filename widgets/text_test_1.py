# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text_test_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_text_widget_frame_1(object):
    def setupUi(self, text_widget_frame_1):
        text_widget_frame_1.setObjectName("text_widget_frame_1")
        text_widget_frame_1.resize(340, 309)
        self.text_widget_1 = QtWidgets.QTextBrowser(text_widget_frame_1)
        self.text_widget_1.setGeometry(QtCore.QRect(10, 10, 321, 291))
        self.text_widget_1.setObjectName("text_widget_1")

        self.retranslateUi(text_widget_frame_1)
        QtCore.QMetaObject.connectSlotsByName(text_widget_frame_1)

    def retranslateUi(self, text_widget_frame_1):
        _translate = QtCore.QCoreApplication.translate
        text_widget_frame_1.setWindowTitle(_translate("text_widget_frame_1", "Form"))
