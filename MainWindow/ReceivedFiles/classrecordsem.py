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
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1245, 1080))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 1080))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        style_sheet = """
                            QScrollBar:vertical {
                                width: 12px;
                                background: #f0f0f0;
                                border-radius: 10px;
                            }

                            QScrollBar::handle:vertical {
                                background: #808080;
                                border-radius: 6px;
                            }

                            QScrollBar::handle:vertical:hover,
                            QScrollBar::handle:vertical:pressed {
                                background: #606060;
                            }
                        """
        self.scrollArea.verticalScrollBar().setStyleSheet(style_sheet)

        # Set the widget for the scroll area
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Set up the layout for your central widget
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setMaximumSize(QtCore.QSize(490, 100))
        self.label.setStyleSheet("background-color: transparent;\n"
"")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../Downloads/PSU LOGO WITH WORDMARK (1).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setMaximumSize(QtCore.QSize(400, 75))
        self.label_2.setStyleSheet("background-color: transparent;\n"
"")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../Downloads/HEADER TEXT (1).png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
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
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.profile_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.profile_2.setAutoFillBackground(False)
        self.profile_2.setStyleSheet("QPushButton {\n"
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
        self.profile_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../Downloads/BackBtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profile_2.setIcon(icon1)
        self.profile_2.setIconSize(QtCore.QSize(60, 60))
        self.profile_2.setShortcut("")
        self.profile_2.setObjectName("profile_2")
        self.horizontalLayout_6.addWidget(self.profile_2)
        spacerItem3 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setStyleSheet("font: 75 25pt \"Gotham Black\";\n"
"background-color: transparent;\n"
"")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setStyleSheet("font: 75 15pt \"Gotham\";\n"
"background-color: transparent;\n"
"")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.gridLayout_9.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(150, -1, 200, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: transparent;\n"
"")
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)
        self.CourseCode_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.CourseCode_2.setStyleSheet("QLineEdit {\n"
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
        self.CourseCode_2.setObjectName("CourseCode_2")
        self.gridLayout_4.addWidget(self.CourseCode_2, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: transparent;\n"
"")
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 1, 0, 1, 1)
        self.Period_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.Period_2.setStyleSheet("QLineEdit {\n"
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
        self.Period_2.setObjectName("Period_2")
        self.gridLayout_4.addWidget(self.Period_2, 0, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setStyleSheet("QLabel {\n"
"    font: 700 9pt \"Gotham\";\n"
"    color: #002F6C;\n"
"background-color: transparent;\n"
"}\n"
"\n"
"\n"
"")
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 3, 0, 1, 1)
        self.Subject_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.Subject_2.setStyleSheet("QLineEdit {\n"
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
        self.Subject_2.setObjectName("Subject_2")
        self.gridLayout_4.addWidget(self.Subject_2, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: transparent;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 2, 0, 1, 1)
        self.YrandSection_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.YrandSection_2.setStyleSheet("QLineEdit {\n"
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
        self.YrandSection_2.setObjectName("YrandSection_2")
        self.gridLayout_4.addWidget(self.YrandSection_2, 3, 1, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_4)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(200, -1, 150, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: transparent;")
        self.label_19.setObjectName("label_19")
        self.gridLayout_6.addWidget(self.label_19, 1, 0, 1, 1)
        self.numberofstudents_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.numberofstudents_2.setStyleSheet("QLineEdit {\n"
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
        self.numberofstudents_2.setObjectName("numberofstudents_2")
        self.gridLayout_6.addWidget(self.numberofstudents_2, 2, 1, 1, 1)
        self.AcademicYEar_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.AcademicYEar_2.setStyleSheet("QLineEdit {\n"
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
        self.AcademicYEar_2.setObjectName("AcademicYEar_2")
        self.gridLayout_6.addWidget(self.AcademicYEar_2, 0, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: transparent;")
        self.label_20.setObjectName("label_20")
        self.gridLayout_6.addWidget(self.label_20, 0, 0, 1, 1)
        self.Semester_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.Semester_2.setStyleSheet("QLineEdit {\n"
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
        self.Semester_2.setObjectName("Semester_2")
        self.gridLayout_6.addWidget(self.Semester_2, 1, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: transparent;")
        self.label_21.setObjectName("label_21")
        self.gridLayout_6.addWidget(self.label_21, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: transparent;")
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 2, 0, 1, 1)
        self.instructor_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.instructor_2.setStyleSheet("QLineEdit {\n"
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
        self.instructor_2.setObjectName("instructor_2")
        self.gridLayout_6.addWidget(self.instructor_2, 3, 1, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_6)
        self.gridLayout_9.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)
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
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(20, 0, 20, 15)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setStyleSheet("font: 7pt \"Lucida Sans Typewriter\";\n"
"font: 600 9pt \"Lucida Sans Typewriter\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;")
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.gridLayout = QtWidgets.QGridLayout(self.tab1)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.tab1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab1, "")
        self.horizontalLayout_10.addWidget(self.tabWidget)
        self.gridLayout_9.addLayout(self.horizontalLayout_10, 5, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; color:#002f6c;\">BSCpE 111 | BSCpE 2A</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0000ff;\">CLASS RECORD</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Period:</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Course Code:</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Yr &amp; Section:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Subject:</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Semester:</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Academic Year:</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Instructor:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#1b1159;\">No. of Students:</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "SEMESTRAL"))

        table = QTableWidget()
        table.setRowCount(69)
        table.setColumnCount(9)
        # Hide the horizontal and vertical headers
        table.horizontalHeader().setVisible(False)
        table.verticalHeader().setVisible(False)

        # NO. COLUMN
        no_item = QTableWidgetItem('NO.')
        no_item.setTextAlignment(4 | 0x80)
        table.setItem(0, 0, no_item)
        table.setSpan(0, 0, 2, 1)

        # AME OF STUDENT COLUMN
        name_item = QTableWidgetItem('Name of Student')
        name_item.setTextAlignment(4 | 0x80)
        table.setItem(0, 1, name_item)
        table.setSpan(0, 1, 2, 1)

        # MIDTERM COLUMN
        mid_item = QTableWidgetItem('MIDTERM')
        mid_item.setTextAlignment(4 | 0x80)
        table.setItem(0, 2, mid_item)
        table.setSpan(0, 2, 1, 2)

        # CELLS UNDER OTHERS
        mgrade_item = QTableWidgetItem('GRADE')
        mgrade_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 2, mgrade_item)
        table.setSpan(1, 2, 1, 1)

        eqv_item = QTableWidgetItem('NUMERICAL EUIVALENT')
        eqv_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 3, eqv_item)
        table.setSpan(1, 3, 1, 1)

        # FINAL COLUMN
        final_item = QTableWidgetItem('FINAL TERM')
        final_item.setTextAlignment(4 | 0x80)
        table.setItem(0, 4, final_item)
        table.setSpan(0, 4, 1, 2)

        # CELLS UNDER OTHERS
        fgrade_item = QTableWidgetItem('GRADE')
        fgrade_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 4, fgrade_item)
        table.setSpan(1, 4, 1, 1)

        eqv_item = QTableWidgetItem('NUMERICAL EUIVALENT')
        eqv_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 5, eqv_item)
        table.setSpan(1, 5, 1, 1)

        # SEMESTRAL COLUMN
        sem_item = QTableWidgetItem('SEMESTRAL')
        sem_item.setTextAlignment(4 | 0x80)
        table.setItem(0, 6, sem_item)
        table.setSpan(0, 6, 1, 2)

        # CELLS UNDER OTHERS
        sgrade_item = QTableWidgetItem('GRADE')
        sgrade_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 6, sgrade_item)
        table.setSpan(1, 6, 1, 1)

        eqv_item = QTableWidgetItem('NUMERICAL EUIVALENT')
        eqv_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 7, eqv_item)
        table.setSpan(1, 7, 1, 1)

        # REMARKS COLUMN
        rem_item = QTableWidgetItem('REMARKS')
        rem_item.setTextAlignment(4 | 0x80)
        table.setItem(0, 8, rem_item)
        table.setSpan(0, 8, 2, 1)

        self.tableWidget = table
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
