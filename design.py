# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(852, 671)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #ADD8E6; color: #333;")  # Light blue background

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(430, 100, 401, 141))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setStyleSheet("color: #FFF;")

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 371, 21))
        self.label_3.setFont(QtGui.QFont("Arial", 12))
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 381, 31))
        self.lineEdit.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit.setObjectName("lineEdit")

        self.parse = QtWidgets.QPushButton(self.groupBox)
        self.parse.setGeometry(QtCore.QRect(270, 90, 121, 41))
        self.parse.setObjectName("parse")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 270, 811, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setStyleSheet("color: #FFF;")

        self.display = QtWidgets.QPushButton(self.groupBox_2)
        self.display.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.display.setObjectName("display")

        self.first = QtWidgets.QPushButton(self.groupBox_2)
        self.first.setGeometry(QtCore.QRect(170, 10, 111, 31))
        self.first.setObjectName("first")

        self.lr1 = QtWidgets.QPushButton(self.groupBox_2)
        self.lr1.setGeometry(QtCore.QRect(340, 10, 111, 31))
        self.lr1.setObjectName("lr1")

        self.lalr = QtWidgets.QPushButton(self.groupBox_2)
        self.lalr.setGeometry(QtCore.QRect(510, 10, 111, 31))
        self.lalr.setObjectName("lalr")

        self.parse_table = QtWidgets.QPushButton(self.groupBox_2)
        self.parse_table.setGeometry(QtCore.QRect(680, 10, 111, 31))
        self.parse_table.setObjectName("parse_table")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 330, 811, 301))
        self.textBrowser.setFont(QtGui.QFont("Arial", 12))
        self.textBrowser.setObjectName("textBrowser")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(23, 80, 381, 181))
        self.plainTextEdit.setFont(QtGui.QFont("Arial", 12))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 151, 21))
        self.label_2.setFont(QtGui.QFont("Arial", 12))
        self.label_2.setObjectName("label_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Gungsuh")
        font.setPointSize(26)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(730, 60, 101, 31))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setStyleSheet("color: #FFF;")

        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 91, 31))
        self.label_4.setFont(QtGui.QFont("Arial", 12))
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 21))
        self.menubar.setObjectName("menubar")

        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menu_About = QtWidgets.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.action_Open = QtWidgets.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")

        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")

        self.actionAuthor = QtWidgets.QAction(MainWindow)
        self.actionAuthor.setObjectName("actionAuthor")

        self.menu_File.addAction(self.action_Open)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)

        self.menu_About.addAction(self.actionAuthor)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())

        self.label_3.setBuddy(self.lineEdit)
        self.label_2.setBuddy(self.plainTextEdit)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setTabOrder(self.plainTextEdit, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.parse)
        MainWindow.setTabOrder(self.parse, self.display)
        MainWindow.setTabOrder(self.display, self.first)
        MainWindow.setTabOrder(self.first, self.lr1)
        MainWindow.setTabOrder(self.lr1, self.lalr)
        MainWindow.setTabOrder(self.lalr, self.parse_table)
        MainWindow.setTabOrder(self.parse_table, self.textBrowser)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Enter expression to evaluate :"))
        self.parse.setText(_translate("MainWindow", "Parse"))
        self.display.setText(_translate("MainWindow", "Display"))
        self.first.setText(_translate("MainWindow", "First"))
        self.lr1.setText(_translate("MainWindow", "LR(1) items"))
        self.lalr.setText(_translate("MainWindow", "LALR items"))
        self.parse_table.setText(_translate("MainWindow", "Parsing Table"))
        self.label_2.setText(_translate("MainWindow", "Enter grammar :"))
        self.label.setText(_translate("MainWindow", "LALR Parser"))
        self.label_4.setText(_translate("MainWindow", "'e' : epsilon"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_About.setTitle(_translate("MainWindow", "&About"))
        self.action_Open.setText(_translate("MainWindow", "&Open"))
        self.action_Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAuthor.setText(_translate("MainWindow", "Author"))
