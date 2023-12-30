import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QScrollArea



class Ui_MainWindow(object):

    def update_text_from_database(self, column_name, text_widget):
        # Header
        connection = None
        cursor = None

        try:
            connection = sqlite3.connect('ryan_test_db_1.db')  # Use your own db
            cursor = connection.cursor()

            query = f"SELECT {column_name} FROM header LIMIT 1"  # Replace header with the actual table name
            cursor.execute(query)
            row = cursor.fetchone()

            if row:
                value = row[0]
                text_widget.setText(QtCore.QCoreApplication.translate("MainWindow", str(value)))
            else:
                text_widget.setText(QtCore.QCoreApplication.translate("MainWindow", "No data"))

        except sqlite3.Error as e:
            print("Database error:", e)
            # Handle the error (e.g., show an error message)

        finally:
            cursor.close()
            connection.close()

    def update_all_text_fields(self):
        # Call this function to update all text fields in the header with values from the database
        self.update_text_from_database("course", self.courseText)
        self.update_text_from_database("subject", self.subjectText)
        self.update_text_from_database("yrandSection", self.yrandSectionText)
        self.update_text_from_database("acadyear", self.acadyearText)
        self.update_text_from_database("semester", self.semesterText)
        self.update_text_from_database("instructor", self.instructorText)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ACADEMETRICS LOGO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("QMainWindow {\n"
                                "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #CBE2FC, stop:1 #D8D8D8);\n"
                                "}\n"
                                "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 720))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setAutoFillBackground(False)
        self.backBtn.setStyleSheet("QPushButton {\n"
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
        self.backBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("back_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backBtn.setIcon(icon1)
        self.backBtn.setIconSize(QtCore.QSize(60, 60))
        self.backBtn.setShortcut("")
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout_5.addWidget(self.backBtn)
        spacerItem1 = QtWidgets.QSpacerItem(10, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.subjectCodeLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(28)
        self.subjectCodeLabel.setFont(font)
        self.subjectCodeLabel.setStyleSheet("QLabel {\n"
                                        "    color: #002F6C;\n"
                                        "    letter-spacing: -3px;\n"
                                        "    background-color: transparent;\n"
                                        "}\n"
                                        "")
        self.subjectCodeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.subjectCodeLabel.setObjectName("subjectCodeLabel")
        self.verticalLayout_5.addWidget(self.subjectCodeLabel)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.studetInfolabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.studetInfolabel.setFont(font)
        self.studetInfolabel.setStyleSheet("color: blue; letter-spacing: -1px;")
        self.studetInfolabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.studetInfolabel.setObjectName("studetInfolabel")
        self.horizontalLayout_5.addWidget(self.studetInfolabel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setContentsMargins(150, -1, 200, -1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.courseLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.courseLabel.setFont(font)
        self.courseLabel.setObjectName("courseLabel")
        self.gridLayout_8.addWidget(self.courseLabel, 1, 0, 1, 1)
        self.subjectlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.subjectlabel.setFont(font)
        self.subjectlabel.setObjectName("subjectlabel")
        self.gridLayout_8.addWidget(self.subjectlabel, 2, 0, 1, 1)
        self.subjectText = QtWidgets.QLabel(self.centralwidget)
        self.subjectText.setMinimumSize(QtCore.QSize(600, 0))
        self.subjectText.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.subjectText.setFont(font)
        self.subjectText.setStyleSheet("color:#1b1159;")
        self.subjectText.setObjectName("subjectText")
        self.gridLayout_8.addWidget(self.subjectText, 2, 1, 1, 1)
        self.courseText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.courseText.setFont(font)
        self.courseText.setStyleSheet("color:#1b1159;")
        self.courseText.setObjectName("courseText")
        self.gridLayout_8.addWidget(self.courseText, 1, 1, 1, 1)
        self.yrandSectionLabel = QtWidgets.QLabel(self.centralwidget)
        self.yrandSectionLabel.setStyleSheet("QLabel {\n"
                                        "    font: 700 9pt \"Gotham\";\n"
                                        "    color: #002F6C;\n"
                                        "}\n"
                                        "")
        self.yrandSectionLabel.setObjectName("yrandSectionLabel")
        self.gridLayout_8.addWidget(self.yrandSectionLabel, 3, 0, 1, 1)
        self.yrandSectionText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.yrandSectionText.setFont(font)
        self.yrandSectionText.setStyleSheet("color:#1b1159;")
        self.yrandSectionText.setObjectName("yrandSectionText")
        self.gridLayout_8.addWidget(self.yrandSectionText, 3, 1, 1, 1)
        self.horizontalLayout_12.addLayout(self.gridLayout_8)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setContentsMargins(200, -1, 150, -1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.semesterText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.semesterText.setFont(font)
        self.semesterText.setStyleSheet("color:#1b1159;")
        self.semesterText.setObjectName("semesterText")
        self.gridLayout_9.addWidget(self.semesterText, 1, 1, 1, 1)
        self.instructorLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.instructorLabel.setFont(font)
        self.instructorLabel.setObjectName("instructorLabel")
        self.gridLayout_9.addWidget(self.instructorLabel, 2, 0, 1, 1)
        self.acadyearLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.acadyearLabel.setFont(font)
        self.acadyearLabel.setObjectName("acadyearLabel")
        self.gridLayout_9.addWidget(self.acadyearLabel, 0, 0, 1, 1)
        self.acadyearText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.acadyearText.setFont(font)
        self.acadyearText.setStyleSheet("color:#1b1159;")
        self.acadyearText.setObjectName("acadyearText")
        self.gridLayout_9.addWidget(self.acadyearText, 0, 1, 1, 1)
        self.semesterLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.semesterLabel.setFont(font)
        self.semesterLabel.setObjectName("semesterLabel")
        self.gridLayout_9.addWidget(self.semesterLabel, 1, 0, 1, 1)
        self.instructorText = QtWidgets.QLabel(self.centralwidget)
        self.instructorText.setMinimumSize(QtCore.QSize(600, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.instructorText.setFont(font)
        self.instructorText.setStyleSheet("color:#1b1159;")
        self.instructorText.setLineWidth(0)
        self.instructorText.setTextFormat(QtCore.Qt.PlainText)
        self.instructorText.setObjectName("instructorText")
        self.gridLayout_9.addWidget(self.instructorText, 2, 1, 1, 1)
        self.horizontalLayout_12.addLayout(self.gridLayout_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.searchLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.searchLabel.setStyleSheet("QLabel {\n"
                                        "    font: 700 9pt \"Gotham\";\n"
                                        "    color: #002F6C;\n"
                                        "}\n"
                                        "")
        self.searchLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.searchLabel.setObjectName("searchLabel")
        self.horizontalLayout_4.addWidget(self.searchLabel)
        self.search_bar = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(sizePolicy)
        self.search_bar.setMinimumSize(QtCore.QSize(600, 0))
        self.search_bar.setMaximumSize(QtCore.QSize(600, 50))
        self.search_bar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.search_bar.setStyleSheet("QLineEdit:hover,\n"
                                        "QLineEdit:focus {\n"
                                        "    background-color: #F9F9F9;\n"
                                        "    border: 1px solid #000000;\n"
                                        "}\n"
                                        "QLineEdit {\n"
                                        "    border-radius: 10px;\n"
                                        "    padding: 5px\n"
                                        "}\n"
                                        "")
        self.search_bar.setText("")
        self.search_bar.setMaxLength(16)
        self.search_bar.setFrame(True)
        self.search_bar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.search_bar.setClearButtonEnabled(True)
        self.search_bar.setObjectName("search_bar")
        self.horizontalLayout_4.addWidget(self.search_bar)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.searchResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchResultLabel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.searchResultLabel.setStyleSheet("QLabel {\n"
                                        "    font: 700 9pt \"Gotham\";\n"
                                        "    color: #002F6C;\n"
                                        "}\n"
                                        "")
        self.searchResultLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.searchResultLabel.setObjectName("searchResultLabel")
        self.verticalLayout_2.addWidget(self.searchResultLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.studentnameLabel = QtWidgets.QLabel(self.centralwidget)
        self.studentnameLabel.setMaximumSize(QtCore.QSize(141, 16777215))
        self.studentnameLabel.setStyleSheet("QLabel {\n"
                                        "    font: 700 9pt \"Gotham\";\n"
                                        "    color: #002F6C;\n"
                                        "}\n"
                                        "")
        self.studentnameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.studentnameLabel.setObjectName("studentnameLabel")
        self.horizontalLayout.addWidget(self.studentnameLabel)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.studentnameText = QtWidgets.QLabel(self.centralwidget)
        self.studentnameText.setMinimumSize(QtCore.QSize(200, 0))
        self.studentnameText.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.studentnameText.setFont(font)
        self.studentnameText.setStyleSheet("color:#1b1159;")
        self.studentnameText.setObjectName("studentnameText")
        self.horizontalLayout.addWidget(self.studentnameText)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.studentIDlabel = QtWidgets.QLabel(self.centralwidget)
        self.studentIDlabel.setMaximumSize(QtCore.QSize(141, 16777215))
        self.studentIDlabel.setStyleSheet("QLabel {\n"
                                        "    font: 700 9pt \"Gotham\";\n"
                                        "    color: #002F6C;\n"
                                        "}\n"
                                        "")
        self.studentIDlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.studentIDlabel.setObjectName("studentIDlabel")
        self.horizontalLayout_2.addWidget(self.studentIDlabel)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.studentIDtext = QtWidgets.QLabel(self.centralwidget)
        self.studentIDtext.setMinimumSize(QtCore.QSize(200, 0))
        self.studentIDtext.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.studentIDtext.setFont(font)
        self.studentIDtext.setStyleSheet("color:#1b1159;")
        self.studentIDtext.setObjectName("studentIDtext")
        self.horizontalLayout_2.addWidget(self.studentIDtext)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.HLayout = QtWidgets.QHBoxLayout()
        self.HLayout.setObjectName("HLayout")
        self.grades_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.grades_tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.grades_tab.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.grades_tab.setDocumentMode(False)
        self.grades_tab.setObjectName("grades_tab")
        self.midterm_tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        font.setItalic(False)
        self.midterm_tab.setFont(font)
        self.midterm_tab.setObjectName("midterm_tab")
        self.grades_tab.addTab(self.midterm_tab, "")
        self.final_tab = QtWidgets.QWidget()
        self.final_tab.setObjectName("final_tab")
        self.grades_tab.addTab(self.final_tab, "")
        self.semestral_tab = QtWidgets.QWidget()
        self.semestral_tab.setObjectName("semestral_tab")
        self.grades_tab.addTab(self.semestral_tab, "")
        self.HLayout.addWidget(self.grades_tab)
        self.verticalLayout_2.addLayout(self.HLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.grades_tab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Academetrics | Individual Record"))
        self.subjectCodeLabel.setText(_translate("MainWindow", "ELEC 111 | BSCpE 2A"))
        self.studetInfolabel.setText(_translate("MainWindow", "INDIVIDUAL RECORD"))
        self.courseLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Course Code:</span></p></body></html>"))
        self.subjectlabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Subject:</span></p></body></html>"))
        self.yrandSectionLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Yr &amp; Section:</span></p></body></html>"))
        self.instructorLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Instructor:</span></p></body></html>"))
        self.acadyearLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Academic Year:</span></p></body></html>"))
        self.semesterLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Semester:</span></p></body></html>"))
        self.searchLabel.setText(_translate("MainWindow", "<html><head/><body><p>Search for Student:</p></body></html>"))
        self.search_bar.setPlaceholderText(_translate("MainWindow", "Enter Student ID or Student Name"))
        self.searchResultLabel.setText(_translate("MainWindow", "<html><head/><body><p>SHOWING RESULTS FOR:</p></body></html>"))
        self.studentnameLabel.setText(_translate("MainWindow", "<html><head/><body><p>Student Name:</p></body></html>"))
        self.studentnameText.setText(_translate("MainWindow", "Cabanela, Edriene Jay O."))
        self.studentIDlabel.setText(_translate("MainWindow", "<html><head/><body><p>Student ID:</p></body></html>"))
        self.studentIDtext.setText(_translate("MainWindow", "22-UR-xxxx"))
        self.grades_tab.setTabText(self.grades_tab.indexOf(self.midterm_tab), _translate("MainWindow", "Midterm"))
        self.grades_tab.setTabText(self.grades_tab.indexOf(self.final_tab), _translate("MainWindow", "Finals"))
        self.grades_tab.setTabText(self.grades_tab.indexOf(self.semestral_tab), _translate("MainWindow", "Semestral"))

        table = QTableWidget()
        table.setRowCount(3)
        table.setColumnCount(9)
        # Hide the horizontal and vertical headers
        table.horizontalHeader().setVisible(False)
        table.verticalHeader().setVisible(False)

        # Input "Others (30%)" in the first row and center-align it
        Homework = QTableWidgetItem('HOMEWORK')
        Homework.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table.setItem(0, 1, Homework)

        # Input "Quiz (30%)" in the first row and center-align it
        quiz = QTableWidgetItem('QUIZZES')
        quiz.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table.setItem(0, 2, quiz)

        # Input "Exam (40%)" in the first row and center-align it
        AttendanceReci = QTableWidgetItem('ATTENDANCE/RECITATION')
        AttendanceReci.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table.setItem(0, 3, AttendanceReci)

        # Input "LEC Grade" in the first row and center-align it
        MidtermExam = QTableWidgetItem('MIDTERM EXAM')
        MidtermExam.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table.setItem(0, 4, MidtermExam)

        LecGrade = QTableWidgetItem('LECTURE GRADE')
        LecGrade.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table.setItem(0, 5, LecGrade)

        LAB_REP = QTableWidgetItem('LABORATORY REPORTS')
        LAB_REP.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table.setItem(0, 6, LAB_REP)

        participation = QTableWidgetItem('PARTICIPATION')
        participation.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table.setItem(0, 7, participation)

        LAB_GRADE = QTableWidgetItem('LABORATORY GRADE')
        LAB_GRADE.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table.setItem(0, 8, LAB_GRADE)

        table.setRowHeight(0, 100)

        OGRADE = QTableWidgetItem('WEIGHTED GRADE/AVERAGE GRADE')
        OGRADE.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table.setItem(1, 0, OGRADE)
        table.setRowHeight(1, 100)

        Midtermsgrade = QTableWidgetItem('FINAL GRADE')
        Midtermsgrade.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table.setItem(2, 0, Midtermsgrade)
        table.setSpan(2, 1, 1, 8)
        table.setRowHeight(2, 100)

        table.setColumnWidth(0, 220)
        table.setColumnWidth(1, 200)
        table.setColumnWidth(2, 200)
        table.setColumnWidth(3, 200)
        table.setColumnWidth(4, 200)
        table.setColumnWidth(5, 200)
        table.setColumnWidth(6, 200)
        table.setColumnWidth(7, 200)
        table.setColumnWidth(8, 220)


        # For Midterm Tab
        self.midterm_tab_layout = QtWidgets.QVBoxLayout(self.midterm_tab)
        self.midterm_tab_layout.addWidget(table)
        self.grades_tab.setTabText(self.grades_tab.indexOf(self.midterm_tab), "Midterm")

        table2 = QTableWidget()
        table2.horizontalHeader().setVisible(False)
        table2.verticalHeader().setVisible(False)
        table2.setColumnCount(9)
        table2.setRowCount(3)


        # Input "Others (30%)" in the first row and center-align it
        Homework2 = QTableWidgetItem('HOMEWORK')
        Homework2.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table2.setItem(0, 1, Homework2)

        # Input "Quiz (30%)" in the first row and center-align it
        quiz2 = QTableWidgetItem('QUIZZES')
        quiz2.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table2.setItem(0, 2, quiz2)

        # Input "Exam (40%)" in the first row and center-align it
        AttendanceReci2 = QTableWidgetItem('ATTENDANCE/RECITATION')
        AttendanceReci2.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table2.setItem(0, 3, AttendanceReci2)

        # Input "LEC Grade" in the first row and center-align it
        MidtermExam2 = QTableWidgetItem('FINAL EXAM')
        MidtermExam2.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table2.setItem(0, 4, MidtermExam2)

        LecGrade2 = QTableWidgetItem('LECTURE GRADE')
        LecGrade2.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table2.setItem(0, 5, LecGrade2)

        LAB_REP2 = QTableWidgetItem('LABORATORY REPORTS')
        LAB_REP2.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table2.setItem(0, 6, LAB_REP2)
        table2.setRowHeight(0, 100)

        participation2 = QTableWidgetItem('PARTICIPATION')
        participation2.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table2.setItem(0, 7, participation2)

        LAB_GRADE2 = QTableWidgetItem('LABORATORY GRADE')
        LAB_GRADE2.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table2.setItem(0, 8, LAB_GRADE2)

        OGRADE2 = QTableWidgetItem('WEIGHTED GRADE/AVERAGE GRADE')
        OGRADE2.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table2.setItem(1, 0, OGRADE2)
        table2.setRowHeight(1, 100)

        Finalsgrade = QTableWidgetItem('FINAL GRADE')
        Finalsgrade.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        table2.setItem(2, 0, Finalsgrade)
        table2.setSpan(2, 1, 1, 8)
        table2.setRowHeight(2, 100)

        table2.setColumnWidth(0, 220)
        table2.setColumnWidth(1, 200)
        table2.setColumnWidth(2, 200)
        table2.setColumnWidth(3, 200)
        table2.setColumnWidth(4, 200)
        table2.setColumnWidth(5, 200)
        table2.setColumnWidth(6, 200)
        table2.setColumnWidth(7, 200)
        table2.setColumnWidth(8, 220)

        # For Finals Tab
        self.final_tab_layout = QtWidgets.QVBoxLayout(self.final_tab)
        self.final_tab_layout.addWidget(table2)
        self.grades_tab.setTabText(self.grades_tab.indexOf(self.final_tab), "Finals")

        table3 = QTableWidget()
        table3.horizontalHeader().setVisible(False)
        table3.verticalHeader().setVisible(False)
        table3.setRowCount(2)
        table3.setColumnCount(4)

        # Input "QUIZ" in the first row and center-align it, spanning both columns
        midtermgradesum = QTableWidgetItem('MIDTERM GRADE')
        midtermgradesum.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table3.setItem(0, 0, midtermgradesum)
        table3.setRowHeight(1, 100)

        finalgradesum = QTableWidgetItem('FINAL GRADE')
        finalgradesum.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table3.setItem(0, 1, finalgradesum)

        numericalval = QTableWidgetItem('NUMERICAL VALUE')
        numericalval.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table3.setItem(0, 2, numericalval)

        remarks = QTableWidgetItem('REMARKS')
        remarks.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table3.setItem(0, 3, remarks)

        table3.setColumnWidth(0, 450)
        table3.setColumnWidth(1, 450)
        table3.setColumnWidth(2, 450)
        table3.setColumnWidth(3, 450)

        # For semestral Tab
        self.semestral_tab_layout = QtWidgets.QVBoxLayout(self.semestral_tab)
        self.semestral_tab_layout.addWidget(table3)
        self.grades_tab.setTabText(self.grades_tab.indexOf(self.semestral_tab), "Semestral")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.update_all_text_fields()
    sys.exit(app.exec_())
