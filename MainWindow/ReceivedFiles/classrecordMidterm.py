import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QScrollArea


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(0, 700))
        MainWindow.setStyleSheet("\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #CBE2FC, stop:1 #D8D8D8);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 550))
        self.scrollArea.setStyleSheet("QScrollBar:vertical {\n"
"    width: 12px; /* Set your desired width */\n"
"    background: #f0f0f0; /* Set your desired gray color */\n"
"    border-radius: 10px; /* Set a border-radius to make it oval */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #808080; /* Set your desired initial handle color */\n"
"    border-radius: 6px; /* Set the same border-radius as above */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover,\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background: #606060; /* Set your desired darker handle color when pressed or hovered */\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    width: 12px; /* Set your desired width */\n"
"    background: #f0f0f0; /* Set your desired gray color */\n"
"    border-radius: 10px; /* Set a border-radius to make it oval */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #808080; /* Set your desired initial handle color */\n"
"    border-radius: 6px; /* Set the same border-radius as above */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover,\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background: #606060; /* Set your desired darker handle color when pressed or hovered */\n"
"}\n"
"")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1262, 1080))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 1080))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(20, 0, 20, 15)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setStyleSheet("font: 7pt \"Lucida Sans Typewriter\";\n"
"font: 600 9pt \"Lucida Sans Typewriter\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;")
        self.tabWidget.setObjectName("tabWidget")
        self.lecTab = QtWidgets.QWidget()
        self.lecTab.setObjectName("lecTab")
        self.gridLayout = QtWidgets.QGridLayout(self.lecTab)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.lecTab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.lecTab, "")
        self.labtab = QtWidgets.QWidget()
        self.labtab.setObjectName("labtab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.labtab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.labtab)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout_7.addWidget(self.tableWidget_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.labtab, "")
        self.summaryTab = QtWidgets.QWidget()
        self.summaryTab.setObjectName("summaryTab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.summaryTab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.summaryTab)
        self.tableWidget_3.setMinimumSize(QtCore.QSize(1000, 150))
        self.tableWidget_3.setMaximumSize(QtCore.QSize(1920, 1080))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.gridLayout_8.addWidget(self.tableWidget_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.summaryTab, "")
        self.horizontalLayout_10.addWidget(self.tabWidget)
        self.gridLayout_9.addLayout(self.horizontalLayout_10, 5, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PSULOGO = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.PSULOGO.setMaximumSize(QtCore.QSize(490, 100))
        self.PSULOGO.setStyleSheet("background-color: transparent;\n"
"")
        self.PSULOGO.setText("")
        self.PSULOGO.setPixmap(QtGui.QPixmap("../../../../Downloads/PSU Logo Wordmark.png"))
        self.PSULOGO.setScaledContents(True)
        self.PSULOGO.setObjectName("PSULOGO")
        self.horizontalLayout.addWidget(self.PSULOGO)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.PSU = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.PSU.setMaximumSize(QtCore.QSize(400, 75))
        self.PSU.setStyleSheet("background-color: transparent;\n"
"")
        self.PSU.setText("")
        self.PSU.setPixmap(QtGui.QPixmap("../../../../Downloads/HEADER TEXT (1).png"))
        self.PSU.setScaledContents(True)
        self.PSU.setObjectName("PSU")
        self.horizontalLayout.addWidget(self.PSU)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.profile = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.profile.setAutoFillBackground(False)
        self.profile.setStyleSheet("QPushButton {\n"
"    border-radius: 10px; \n"
"    background-color: #00FFFFFF;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:pressed,\n"
"QPushButton:checked,\n"
"QPushButton:hover {\n"
"    background-color: #949494; \n"
"}\n"
"")
        self.profile.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Downloads/PROFILE BUTTON.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profile.setIcon(icon)
        self.profile.setIconSize(QtCore.QSize(60, 60))
        self.profile.setShortcut("")
        self.profile.setObjectName("profile")
        self.horizontalLayout.addWidget(self.profile, 0, QtCore.Qt.AlignRight)
        self.gridLayout_9.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(150, -1, 200, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.periodLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.periodLabel.setFont(font)
        self.periodLabel.setStyleSheet("background-color: transparent;\n"
"")
        self.periodLabel.setObjectName("periodLabel")
        self.gridLayout_4.addWidget(self.periodLabel, 0, 0, 1, 1)
        self.CourseCode = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.CourseCode.setStyleSheet("QLineEdit {\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white; /* Set the default background color */\n"
"}\n"
"\n"
"QLineEdit:hover,\n"
"QLineEdit:focus {\n"
"    background-color: #F9F9F9; /* Set the background color on hover and focus */\n"
"    border: 1px solid #000000;\n"
"}\n"
"\n"
"")
        self.CourseCode.setObjectName("CourseCode")
        self.gridLayout_4.addWidget(self.CourseCode, 1, 1, 1, 1)
        self.courseCodeLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.courseCodeLabel.setFont(font)
        self.courseCodeLabel.setStyleSheet("background-color: transparent;\n"
"")
        self.courseCodeLabel.setObjectName("courseCodeLabel")
        self.gridLayout_4.addWidget(self.courseCodeLabel, 1, 0, 1, 1)
        self.Period = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Period.setStyleSheet("QLineEdit {\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white; /* Set the default background color */\n"
"}\n"
"\n"
"QLineEdit:hover,\n"
"QLineEdit:focus {\n"
"    background-color: #F9F9F9; /* Set the background color on hover and focus */\n"
"    border: 1px solid #000000;\n"
"}\n"
"")
        self.Period.setObjectName("Period")
        self.gridLayout_4.addWidget(self.Period, 0, 1, 1, 1)
        self.yrAndSectionLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.yrAndSectionLabel.setStyleSheet("QLabel {\n"
"    font: 700 9pt \"Gotham\";\n"
"    color: #002F6C;\n"
"background-color: transparent;\n"
"}\n"
"\n"
"\n"
"")
        self.yrAndSectionLabel.setObjectName("yrAndSectionLabel")
        self.gridLayout_4.addWidget(self.yrAndSectionLabel, 3, 0, 1, 1)
        self.Subject = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.Subject.setStyleSheet("QLineEdit {\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white; /* Set the default background color */\n"
"}\n"
"\n"
"QLineEdit:hover,\n"
"QLineEdit:focus {\n"
"    background-color: #F9F9F9; /* Set the background color on hover and focus */\n"
"    border: 1px solid #000000;\n"
"}\n"
"")
        self.Subject.setObjectName("Subject")
        self.gridLayout_4.addWidget(self.Subject, 2, 1, 1, 1)
        self.subjectLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.subjectLabel.setFont(font)
        self.subjectLabel.setStyleSheet("background-color: transparent;")
        self.subjectLabel.setObjectName("subjectLabel")
        self.gridLayout_4.addWidget(self.subjectLabel, 2, 0, 1, 1)
        self.YrandSection = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.YrandSection.setStyleSheet("QLineEdit {\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white; /* Set the default background color */\n"
"}\n"
"\n"
"QLineEdit:hover,\n"
"QLineEdit:focus {\n"
"    background-color: #F9F9F9; /* Set the background color on hover and focus */\n"
"    border: 1px solid #000000;\n"
"}\n"
"\n"
"")
        self.YrandSection.setObjectName("YrandSection")
        self.gridLayout_4.addWidget(self.YrandSection, 3, 1, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_4)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(200, -1, 150, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.semesterLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.semesterLabel.setFont(font)
        self.semesterLabel.setStyleSheet("background-color: transparent;")
        self.semesterLabel.setObjectName("semesterLabel")
        self.gridLayout_6.addWidget(self.semesterLabel, 1, 0, 1, 1)
        self.numberofstudents = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.numberofstudents.setStyleSheet("QLineEdit {\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white; /* Set the default background color */\n"
"}\n"
"\n"
"QLineEdit:hover,\n"
"QLineEdit:focus {\n"
"    background-color: #F9F9F9; /* Set the background color on hover and focus */\n"
"    border: 1px solid #000000;\n"
"}\n"
"")
        self.numberofstudents.setObjectName("numberofstudents")
        self.gridLayout_6.addWidget(self.numberofstudents, 2, 1, 1, 1)
        self.acadYear = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.acadYear.setStyleSheet("QLineEdit {\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white; /* Set the default background color */\n"
"}\n"
"\n"
"QLineEdit:hover,\n"
"QLineEdit:focus {\n"
"    background-color: #F9F9F9; /* Set the background color on hover and focus */\n"
"    border: 1px solid #000000;\n"
"}\n"
"")
        self.acadYear.setObjectName("acadYear")
        self.gridLayout_6.addWidget(self.acadYear, 0, 1, 1, 1)
        self.acadYearLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.acadYearLabel.setFont(font)
        self.acadYearLabel.setStyleSheet("background-color: transparent;")
        self.acadYearLabel.setObjectName("acadYearLabel")
        self.gridLayout_6.addWidget(self.acadYearLabel, 0, 0, 1, 1)
        self.Semester = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.Semester.setStyleSheet("QLineEdit {\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white; /* Set the default background color */\n"
"}\n"
"\n"
"QLineEdit:hover,\n"
"QLineEdit:focus {\n"
"    background-color: #F9F9F9; /* Set the background color on hover and focus */\n"
"    border: 1px solid #000000;\n"
"}\n"
"")
        self.Semester.setObjectName("Semester")
        self.gridLayout_6.addWidget(self.Semester, 1, 1, 1, 1)
        self.instructorLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.instructorLabel.setFont(font)
        self.instructorLabel.setStyleSheet("background-color: transparent;")
        self.instructorLabel.setObjectName("instructorLabel")
        self.gridLayout_6.addWidget(self.instructorLabel, 3, 0, 1, 1)
        self.noOfstudentsLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        self.noOfstudentsLabel.setFont(font)
        self.noOfstudentsLabel.setStyleSheet("background-color: transparent;")
        self.noOfstudentsLabel.setObjectName("noOfstudentsLabel")
        self.gridLayout_6.addWidget(self.noOfstudentsLabel, 2, 0, 1, 1)
        self.instructor = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.instructor.setStyleSheet("QLineEdit {\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white; /* Set the default background color */\n"
"}\n"
"\n"
"QLineEdit:hover,\n"
"QLineEdit:focus {\n"
"    background-color: #F9F9F9; /* Set the background color on hover and focus */\n"
"    border: 1px solid #000000;\n"
"}\n"
"\n"
"")
        self.instructor.setObjectName("instructor")
        self.gridLayout_6.addWidget(self.instructor, 3, 1, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_6)
        self.gridLayout_9.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.backkButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.backkButton.setAutoFillBackground(False)
        self.backkButton.setStyleSheet("QPushButton {\n"
"    border-radius: 10px; \n"
"    background-color: #00FFFFFF;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:pressed,\n"
"QPushButton:checked,\n"
"QPushButton:hover {\n"
"    background-color: #949494; \n"
"}\n"
"")
        self.backkButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../Downloads/BackBtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backkButton.setIcon(icon1)
        self.backkButton.setIconSize(QtCore.QSize(60, 60))
        self.backkButton.setShortcut("")
        self.backkButton.setObjectName("backkButton")
        self.horizontalLayout_6.addWidget(self.backkButton)
        spacerItem3 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.BSCPELabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.BSCPELabel.setStyleSheet("font: 75 25pt \"Gotham Black\";\n"
"background-color: transparent;\n"
"")
        self.BSCPELabel.setObjectName("BSCPELabel")
        self.horizontalLayout_6.addWidget(self.BSCPELabel)
        self.classrecordLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.classrecordLabel.setStyleSheet("font: 75 15pt \"Gotham\";\n"
"background-color: transparent;\n"
"")
        self.classrecordLabel.setObjectName("classrecordLabel")
        self.horizontalLayout_6.addWidget(self.classrecordLabel)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.editButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(15)
        self.editButton.setFont(font)
        self.editButton.setStyleSheet("QPushButton {\n"
"    border-radius: 10px; \n"
"    background-color: #00FFFFFF;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:pressed,\n"
"QPushButton:checked,\n"
"QPushButton:hover {\n"
"    background-color: #949494; \n"
"}\n"
"")
        self.editButton.setFlat(True)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout_6.addWidget(self.editButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.gridLayout_9.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setStyleSheet("QFrame {\n"
"    border: 2px solid rgb(185, 190, 255); /* Border color and width */\n"
"    border-radius: 5px; /* Border corner radius */\n"
"\n"
"}\n"
"/* Horizontal line */\n"
"QFrame[orientation=\"horizontal\"] {\n"
"    height: 0px; /* Set the height to create a horizontal line */\n"
"}\n"
"\n"
"/* Vertical line */\n"
"QFrame[orientation=\"vertical\"] {\n"
"    width: 0px; /* Set the width to create a vertical line */\n"
"}\n"
"")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_9.addWidget(self.line_2, 4, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setStyleSheet("QFrame {\n"
"    border: 2px solid rgb(185, 190, 255); /* Border color and width */\n"
"    border-radius: 5px; /* Border corner radius */\n"
"\n"
"}\n"
"/* Horizontal line */\n"
"QFrame[orientation=\"horizontal\"] {\n"
"    height: 0px; /* Set the height to create a horizontal line */\n"
"}\n"
"\n"
"/* Vertical line */\n"
"QFrame[orientation=\"vertical\"] {\n"
"    width: 0px; /* Set the width to create a vertical line */\n"
"}\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_9.addWidget(self.line, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lecTab), _translate("MainWindow", "LEC"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.labtab), _translate("MainWindow", "LAB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.summaryTab), _translate("MainWindow", "SUMMARY"))
        self.periodLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Period:</span></p></body></html>"))
        self.courseCodeLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Course Code:</span></p></body></html>"))
        self.yrAndSectionLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Yr &amp; Section:</span></p></body></html>"))
        self.subjectLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Subject:</span></p></body></html>"))
        self.semesterLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Semester:</span></p></body></html>"))
        self.acadYearLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Academic Year:</span></p></body></html>"))
        self.instructorLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Instructor:</span></p></body></html>"))
        self.noOfstudentsLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#1b1159;\">No. of Students:</span></p></body></html>"))
        self.BSCPELabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; color:#002f6c;\">BSCpE 111 | BSCpE 2A</span></p></body></html>"))
        self.classrecordLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0000ff;\">CLASS RECORD</span></p></body></html>"))
        self.editButton.setText(_translate("MainWindow", "..."))

        table = QTableWidget()
        table.setRowCount(69)
        table.setColumnCount(33)
        # Hide the horizontal and vertical headers
        table.horizontalHeader().setVisible(False)
        table.verticalHeader().setVisible(False)

        # NO. COLUMN
        no_item = QTableWidgetItem('NO.')
        no_item.setTextAlignment(4 | 0x80)
        table.setItem(0, 0, no_item)
        table.setSpan(0, 0, 4, 1)

        # AME OF STUDENT COLUMN
        name_item = QTableWidgetItem('Name of Student')
        name_item.setTextAlignment(4 | 0x80)
        table.setItem(0, 1, name_item)
        table.setSpan(0, 1, 4, 1)

        # OTHERS COLUMN
        others_item = QTableWidgetItem('OTHERS(30%)')
        others_item.setTextAlignment(4 | 0x80)
        table.setItem(0, 2, others_item)
        table.setSpan(0, 2, 1, 19)

        # CELLS UNDER OTHERS
        homeworkorseatwork_item = QTableWidgetItem('HOMEWORK/SEATWORK(15%)')
        homeworkorseatwork_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 2, homeworkorseatwork_item)
        table.setSpan(1, 2, 1, 8)

        # CELLS UNDER HOMEWORK
        h1_item = QTableWidgetItem('1')
        h1_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 2, h1_item)
        table.setSpan(2, 2, 1, 1)

        eqv1_item = QTableWidgetItem('EQV')
        eqv1_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 3, eqv1_item)
        table.setSpan(2, 3, 2, 1)

        h2_item = QTableWidgetItem('2')
        h2_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 4, h2_item)
        table.setSpan(2, 4, 1, 1)

        eqv2_item = QTableWidgetItem('EQV')
        eqv2_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 5, eqv2_item)
        table.setSpan(2, 5, 2, 1)

        h3_item = QTableWidgetItem('3')
        h3_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 6, h3_item)
        table.setSpan(2, 6, 1, 1)

        eqv3_item = QTableWidgetItem('EQV')
        eqv3_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 7, eqv3_item)
        table.setSpan(2, 7, 2, 1)

        ave1_item = QTableWidgetItem('AVE')
        ave1_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 8, ave1_item)
        table.setSpan(2, 8, 2, 1)

        weightedscore1_item = QTableWidgetItem('WEIGHTED SCORE')
        weightedscore1_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 9, weightedscore1_item)
        table.setSpan(2, 9, 2, 1)

        recitationorattendance_item = QTableWidgetItem('RECITATION/ATTENDANCE(15%)')
        recitationorattendance_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 10, recitationorattendance_item)
        table.setSpan(1, 10, 1, 10)

        # CELLS UNDER RECITATION/ATTENDANCE
        r1_item = QTableWidgetItem('1')
        r1_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 10, r1_item)
        table.setSpan(2, 10, 1, 1)

        eqv4_item = QTableWidgetItem('EQV')
        eqv4_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 11, eqv4_item)
        table.setSpan(2, 11, 2, 1)

        r2_item = QTableWidgetItem('2')
        r2_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 12, r2_item)
        table.setSpan(2, 12, 1, 1)

        eqv5_item = QTableWidgetItem('EQV')
        eqv5_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 13, eqv5_item)
        table.setSpan(2, 13, 2, 1)

        r3_item = QTableWidgetItem('3')
        r3_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 14, r3_item)
        table.setSpan(2, 14, 1, 1)

        eqv6_item = QTableWidgetItem('EQV')
        eqv6_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 15, eqv6_item)
        table.setSpan(2, 15, 2, 1)

        att1_item = QTableWidgetItem('ATT')
        att1_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 16, att1_item)
        table.setSpan(2, 16, 2, 1)

        eqv7_item = QTableWidgetItem('EQV')
        eqv7_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 17, eqv7_item)
        table.setSpan(2, 17, 2, 1)

        ave2_item = QTableWidgetItem('AVE')
        ave2_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 18, ave2_item)
        table.setSpan(2, 18, 2, 1)

        weightedscore2_item = QTableWidgetItem('WEIGHTED SCORE')
        weightedscore2_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 19, weightedscore2_item)
        table.setSpan(2, 19, 2, 1)

        grade_item = QTableWidgetItem('GRADE')
        grade_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 20, grade_item)
        table.setSpan(1, 20, 3, 1)

        # CELLS FOR QUIZ
        quiz_item = QTableWidgetItem('QUIZ(30%)')
        quiz_item.setTextAlignment(4 | 0x80)
        table.setItem(0, 21, quiz_item)
        table.setSpan(0, 21, 1, 8)

        q1_item = QTableWidgetItem('QUIZ 1')
        q1_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 21, q1_item)
        table.setSpan(1, 21, 2, 1)

        eqv8_item = QTableWidgetItem('EQV')
        eqv8_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 22, eqv8_item)
        table.setSpan(1, 22, 3, 1)

        q2_item = QTableWidgetItem('QUIZ 2')
        q2_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 23, q2_item)
        table.setSpan(1, 23, 2, 1)

        eqv9_item = QTableWidgetItem('EQV')
        eqv9_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 24, eqv9_item)
        table.setSpan(1, 24, 3, 1)

        q3_item = QTableWidgetItem('QUIZ 3')
        q3_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 25, q3_item)
        table.setSpan(1, 25, 2, 1)

        eqv10_item = QTableWidgetItem('EQV')
        eqv10_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 26, eqv10_item)
        table.setSpan(1, 26, 3, 1)

        ave3_item = QTableWidgetItem('AVE')
        ave3_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 27, ave3_item)
        table.setSpan(1, 27, 3, 1)

        weightedscore3_item = QTableWidgetItem('WEIGHTED SCORE')
        weightedscore3_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 28, weightedscore3_item)
        table.setSpan(1, 28, 3, 1)

        # CELLS FOR EXAM
        exam_item = QTableWidgetItem('EXAM(30%)')
        exam_item.setTextAlignment(4 | 0x80)
        table.setItem(0, 29, exam_item)
        table.setSpan(0, 29, 1, 3)

        score_item = QTableWidgetItem('SCORE')
        score_item.setTextAlignment(4 | 0x80)
        table.setItem(1, 29, score_item)
        table.setSpan(1, 29, 2, 1)

        eqv11_item = QTableWidgetItem('EQV')
        eqv11_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 30, eqv11_item)
        table.setSpan(1, 30, 3, 1)

        weightedscore4_item = QTableWidgetItem('WEIGHTED SCORE/GRADE')
        weightedscore4_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 31, weightedscore4_item)
        table.setSpan(1, 31, 3, 1)

        lec_item = QTableWidgetItem('LEC GRADE')
        lec_item.setTextAlignment(4 | 0x80)
        table.setItem(0, 32, lec_item)
        table.setSpan(0, 32, 4, 1)

        self.tableWidget = table
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        table2 = QTableWidget()
        table2.setRowCount(69)
        table2.setColumnCount(27)
        table2.horizontalHeader().setVisible(False)
        table2.verticalHeader().setVisible(False)

        no_item = QTableWidgetItem('No.')
        no_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(0, 0, no_item)
        table2.setSpan(0, 0, 3, 1)

        name_item = QTableWidgetItem('NAME OF STUDENT')
        name_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(0, 1, name_item)
        table2.setSpan(0, 1, 3, 1)

        # Input "LAB" in the first row and center-align it, spanning both columns
        lab_item = QTableWidgetItem('LABORATORY REPORT (80%)')
        lab_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(0, 2, lab_item)
        table2.setSpan(0, 2, 1, 16)

        # Input "Quiz 1" and "Quiz 2" in the second row and center-align them
        lab1_item = QTableWidgetItem('LAB 1')
        lab1_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 2, lab1_item)
        table2.setSpan(1, 2, 1, 1)

        labb1_item = QTableWidgetItem('50')
        labb1_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(2, 2, labb1_item)

        eqv_item = QTableWidgetItem('EQV')
        eqv_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 3, eqv_item)
        table2.setSpan(1, 3, 2, 1)

        lab2_item = QTableWidgetItem('LAB 2')
        lab2_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 4, lab2_item)
        table2.setSpan(1, 4, 1, 1)

        labb2_item = QTableWidgetItem('50')
        labb2_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(2, 4, labb2_item)

        eqv2_item = QTableWidgetItem('EQV')
        eqv2_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 5, eqv2_item)
        table2.setSpan(1, 5, 2, 1)

        lab3_item = QTableWidgetItem('LAB 3')
        lab3_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 6, lab3_item)
        table2.setSpan(1, 6, 1, 1)

        labb3_item = QTableWidgetItem('50')
        labb3_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(2, 6, labb3_item)

        eqv3_item = QTableWidgetItem('EQV')
        eqv3_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 7, eqv3_item)
        table2.setSpan(1, 7, 2, 1)

        lab4_item = QTableWidgetItem('LAB 4')
        lab4_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 8, lab4_item)
        table2.setSpan(1, 8, 1, 1)

        labb4_item = QTableWidgetItem('50')
        labb4_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(2, 8, labb4_item)

        eqv4_item = QTableWidgetItem('EQV')
        eqv4_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 9, eqv4_item)
        table2.setSpan(1, 9, 2, 1)

        lab5_item = QTableWidgetItem('LAB 5')
        lab5_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 10, lab5_item)
        table2.setSpan(1, 10, 1, 1)

        labb5_item = QTableWidgetItem('50')
        labb5_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(2, 10, labb5_item)

        eqv5_item = QTableWidgetItem('EQV')
        eqv5_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 11, eqv5_item)
        table2.setSpan(1, 11, 2, 1)

        lab6_item = QTableWidgetItem('LAB 6')
        lab6_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 12, lab6_item)
        table2.setSpan(1, 12, 1, 1)

        labb6_item = QTableWidgetItem('50')
        labb6_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(2, 12, labb6_item)

        eqv6_item = QTableWidgetItem('EQV')
        eqv6_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 13, eqv6_item)
        table2.setSpan(1, 13, 2, 1)

        lab7_item = QTableWidgetItem('LAB 7')
        lab7_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 14, lab7_item)
        table2.setSpan(1, 14, 1, 1)

        labb7_item = QTableWidgetItem('50')
        labb7_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(2, 14, labb7_item)

        eqv7_item = QTableWidgetItem('EQV')
        eqv7_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 15, eqv7_item)
        table2.setSpan(1, 15, 2, 1)

        ave_item = QTableWidgetItem('AVERAGE')
        ave_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 16, ave_item)
        table2.setSpan(1, 16, 2, 1)

        score_item = QTableWidgetItem('WEIGHTED SCORE / GRADE')
        score_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 17, score_item)
        table2.setSpan(1, 17, 2, 1)

        # Input "participation" in the first row and center-align it, spanning both columns
        par_item = QTableWidgetItem('PARTICIPATION (20%)')
        par_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(0, 18, par_item)
        table2.setSpan(0, 18, 1, 8)

        # Input "Quiz 1" and "Quiz 2" in the second row and center-align them
        p1_item = QTableWidgetItem('P1')
        p1_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 18, p1_item)
        table2.setSpan(1, 18, 1, 1)

        par1_item = QTableWidgetItem('50')
        par1_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(2, 18, par1_item)

        eqvp_item = QTableWidgetItem('EQV')
        eqvp_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 19, eqvp_item)
        table2.setSpan(1, 19, 2, 1)

        p2_item = QTableWidgetItem('P2')
        p2_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 20, p2_item)
        table2.setSpan(1, 20, 1, 1)

        par2_item = QTableWidgetItem('50')
        par2_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(2, 20, par2_item)

        eqvp2_item = QTableWidgetItem('EQV')
        eqvp2_item.setTextAlignment(4 | 0x80)  # Alig
        table2.setItem(1, 21, eqvp2_item)
        table2.setSpan(1, 21, 2, 1)

        p3_item = QTableWidgetItem('P3')
        p3_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 22, p3_item)
        table2.setSpan(1, 22, 1, 1)

        par3_item = QTableWidgetItem('50')
        par3_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(2, 22, par3_item)

        eqvp3_item = QTableWidgetItem('EQV')
        eqvp3_item.setTextAlignment(4 | 0x80)  # Alig
        table2.setItem(1, 23, eqvp3_item)
        table2.setSpan(1, 23, 2, 1)

        avep_item = QTableWidgetItem('AVE')
        avep_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 24, avep_item)
        table2.setSpan(1, 24, 2, 1)

        pscore_item = QTableWidgetItem('WEIGHTED MEAN / SCORE')
        pscore_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(1, 25, pscore_item)
        table2.setSpan(1, 25, 2, 1)

        labgrade_item = QTableWidgetItem('LABORATORY GRADE')
        labgrade_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table2.setItem(0, 26, labgrade_item)
        table2.setSpan(0, 26, 3, 1)

        self.tableWidget_2 = table2
        self.gridLayout_7.addWidget(self.tableWidget_2, 0, 0, 1, 1)

        table3 = QTableWidget()
        table3.setRowCount(69)
        table3.setColumnCount(8)
        table3.horizontalHeader().setVisible(False)
        table3.verticalHeader().setVisible(False)

        # Allow manual resizing of columns and rows
        table3.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        table3.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        no_item = QTableWidgetItem('No.')
        no_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table3.setItem(0, 0, no_item)
        table3.setSpan(0, 0, 1, 1)

        name_item = QTableWidgetItem('NAME OF STUDENT')
        name_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table3.setItem(0, 1, name_item)
        table3.setSpan(0, 1, 1, 1)

        # Input "LAB" in the first row and center-align it, spanning both columns
        lec_item = QTableWidgetItem('LECTURE GRADE')
        lec_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table3.setItem(0, 2, lec_item)
        table3.setSpan(0, 2, 1, 1)

        # Input "participation" in the first row and center-align it, spanning both columns
        lab_item = QTableWidgetItem('LABORATORY GRADE')
        lab_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table3.setItem(0, 3, lab_item)
        table3.setSpan(0, 3, 1, 1)

        mid_item = QTableWidgetItem('MIDTERM GRADE (LEC+LAB)')
        mid_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table3.setItem(0, 4, mid_item)
        table3.setSpan(0, 4, 1, 2)

        num_item = QTableWidgetItem('NUMERICAL EQUIVALENT')
        num_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table3.setItem(0, 6, num_item)

        rem_item = QTableWidgetItem('REMARKS')
        rem_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table3.setItem(0, 7, rem_item)

        self.tableWidget_3 = table3
        self.gridLayout_8.addWidget(self.tableWidget_3, 0, 0, 1, 1)
        # Set the stretch factor for the table in the layout
        self.gridLayout_8.addWidget(table3, 0, 0, 1, 1)
        self.gridLayout_8.setColumnStretch(0, 1)
        self.gridLayout_8.setRowStretch(0, 1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
