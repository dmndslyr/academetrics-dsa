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
        self.update_text_from_database("period", self.periodText)  # Midterm will show bc midterm is in db
        self.update_text_from_database("course", self.courseText)
        self.update_text_from_database("subject", self.subjectText)
        self.update_text_from_database("yrandSection", self.yrandSectionText)
        self.update_text_from_database("acadyear", self.acadyearText)
        self.update_text_from_database("semester", self.semesterText)
        self.update_text_from_database("noofstudents", self.noofstudentsText)
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
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
        self.subjectCodeLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
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
        self.studetInfolabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.studetInfolabel.setObjectName("studetInfolabel")
        self.horizontalLayout_5.addWidget(self.studetInfolabel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
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
        self.gridLayout_8.addWidget(self.courseLabel, 2, 0, 1, 1)
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
        self.gridLayout_8.addWidget(self.subjectText, 3, 1, 1, 1)
        self.subjectlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.subjectlabel.setFont(font)
        self.subjectlabel.setObjectName("subjectlabel")
        self.gridLayout_8.addWidget(self.subjectlabel, 3, 0, 1, 1)
        self.periodLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.periodLabel.setFont(font)
        self.periodLabel.setStyleSheet("color:#1b1159;")
        self.periodLabel.setObjectName("periodLabel")
        self.gridLayout_8.addWidget(self.periodLabel, 0, 0, 1, 1)
        self.courseText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.courseText.setFont(font)
        self.courseText.setStyleSheet("color:#1b1159;")
        self.courseText.setObjectName("courseText")
        self.gridLayout_8.addWidget(self.courseText, 2, 1, 1, 1)
        self.yrandSectionText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.yrandSectionText.setFont(font)
        self.yrandSectionText.setStyleSheet("color:#1b1159;")
        self.yrandSectionText.setObjectName("yrandSectionText")
        self.gridLayout_8.addWidget(self.yrandSectionText, 4, 1, 1, 1)
        self.yrandSectionLabel = QtWidgets.QLabel(self.centralwidget)
        self.yrandSectionLabel.setStyleSheet("QLabel {\n"
                                             "    font: 700 9pt \"Gotham\";\n"
                                             "    color: #002F6C;\n"
                                             "}\n"
                                             "")
        self.yrandSectionLabel.setObjectName("yrandSectionLabel")
        self.gridLayout_8.addWidget(self.yrandSectionLabel, 4, 0, 1, 1)
        self.periodText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.periodText.setFont(font)
        self.periodText.setStyleSheet("color:#1b1159;")
        self.periodText.setObjectName("periodText")
        self.gridLayout_8.addWidget(self.periodText, 0, 1, 1, 1)
        self.horizontalLayout_12.addLayout(self.gridLayout_8)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setContentsMargins(200, -1, 150, -1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.acadyearLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.acadyearLabel.setFont(font)
        self.acadyearLabel.setObjectName("acadyearLabel")
        self.gridLayout_9.addWidget(self.acadyearLabel, 0, 0, 1, 1)
        self.noofstudentsLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.noofstudentsLabel.setFont(font)
        self.noofstudentsLabel.setStyleSheet("color:#1b1159")
        self.noofstudentsLabel.setObjectName("noofstudentsLabel")
        self.gridLayout_9.addWidget(self.noofstudentsLabel, 2, 0, 1, 1)
        self.instructorLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.instructorLabel.setFont(font)
        self.instructorLabel.setObjectName("instructorLabel")
        self.gridLayout_9.addWidget(self.instructorLabel, 3, 0, 1, 1)
        self.semesterLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.semesterLabel.setFont(font)
        self.semesterLabel.setObjectName("semesterLabel")
        self.gridLayout_9.addWidget(self.semesterLabel, 1, 0, 1, 1)
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
        self.noofstudentsText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.noofstudentsText.setFont(font)
        self.noofstudentsText.setStyleSheet("color:#1b1159;")
        self.noofstudentsText.setObjectName("noofstudentsText")
        self.gridLayout_9.addWidget(self.noofstudentsText, 2, 1, 1, 1)
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
        self.gridLayout_9.addWidget(self.instructorText, 3, 1, 1, 1)
        self.horizontalLayout_12.addLayout(self.gridLayout_9)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.HLayout = QtWidgets.QHBoxLayout()
        self.HLayout.setObjectName("HLayout")
        self.grades_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.grades_tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.grades_tab.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.grades_tab.setDocumentMode(False)
        self.grades_tab.setObjectName("grades_tab")
        self.lec_tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        font.setItalic(False)
        self.lec_tab.setFont(font)
        self.lec_tab.setObjectName("lec_tab")
        self.grades_tab.addTab(self.lec_tab, "")
        self.lab_tab = QtWidgets.QWidget()
        self.lab_tab.setObjectName("lab_tab")
        self.grades_tab.addTab(self.lab_tab, "")
        self.summary_tab = QtWidgets.QWidget()
        self.summary_tab.setObjectName("summary_tab")
        self.grades_tab.addTab(self.summary_tab, "")
        self.HLayout.addWidget(self.grades_tab)
        self.verticalLayout.addLayout(self.HLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.grades_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Academetrics | Final Term Class Record"))
        self.subjectCodeLabel.setText(_translate("MainWindow", "ELEC 111 | BSCpE 2A"))
        self.studetInfolabel.setText(_translate("MainWindow", "CLASS RECORD"))
        self.courseLabel.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Course Code:</span></p></body></html>"))
        self.subjectlabel.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Subject:</span></p></body></html>"))
        self.periodLabel.setText(_translate("MainWindow", "Period:"))
        self.yrandSectionLabel.setText(_translate("MainWindow",
                                                  "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Yr &amp; Section:</span></p></body></html>"))
        self.acadyearLabel.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Academic Year:</span></p></body></html>"))
        self.noofstudentsLabel.setText(_translate("MainWindow", "No. of Students"))
        self.instructorLabel.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Instructor:</span></p></body></html>"))
        self.semesterLabel.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Semester:</span></p></body></html>"))
        self.grades_tab.setTabText(self.grades_tab.indexOf(self.lec_tab), _translate("MainWindow", "Lecture"))
        self.grades_tab.setTabText(self.grades_tab.indexOf(self.lab_tab), _translate("MainWindow", "Laboratory"))
        self.grades_tab.setTabText(self.grades_tab.indexOf(self.summary_tab), _translate("MainWindow", "Summary"))

        table = QTableWidget()
        table.setRowCount(69)
        table.setColumnCount(36)
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
        table.setSpan(0, 2, 1, 22)

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

        portfolio_item = QTableWidgetItem('STUDENT PORTFOLIO')
        portfolio_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 20, portfolio_item)
        table.setSpan(1, 20, 1, 3)

        # CELLS UNDER PORTFOLIO
        p_item = QTableWidgetItem('SCORE')
        p_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 20, p_item)
        table.setSpan(2, 20, 1, 1)

        eqv4_item = QTableWidgetItem('EQV')
        eqv4_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 21, eqv4_item)
        table.setSpan(2, 21, 2, 1)

        weightedscoreport_item = QTableWidgetItem('WEIGHTED SCORE')
        weightedscoreport_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(2, 22, weightedscoreport_item)
        table.setSpan(2, 22, 2, 1)

        grade_item = QTableWidgetItem('GRADE')
        grade_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 23, grade_item)
        table.setSpan(1, 23, 3, 1)

        # CELLS FOR QUIZ
        quiz_item = QTableWidgetItem('QUIZ(30%)')
        quiz_item.setTextAlignment(4 | 0x80)
        table.setItem(0, 24, quiz_item)
        table.setSpan(0, 24, 1, 8)

        q1_item = QTableWidgetItem('QUIZ 1')
        q1_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 24, q1_item)
        table.setSpan(1, 24, 2, 1)

        eqv8_item = QTableWidgetItem('EQV')
        eqv8_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 25, eqv8_item)
        table.setSpan(1, 25, 3, 1)

        q2_item = QTableWidgetItem('QUIZ 2')
        q2_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 26, q2_item)
        table.setSpan(1, 26, 2, 1)

        eqv9_item = QTableWidgetItem('EQV')
        eqv9_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 27, eqv9_item)
        table.setSpan(1, 27, 3, 1)

        q3_item = QTableWidgetItem('QUIZ 3')
        q3_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 28, q3_item)
        table.setSpan(1, 28, 2, 1)

        eqv10_item = QTableWidgetItem('EQV')
        eqv10_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 29, eqv10_item)
        table.setSpan(1, 29, 3, 1)

        ave3_item = QTableWidgetItem('AVE')
        ave3_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 30, ave3_item)
        table.setSpan(1, 30, 3, 1)

        weightedscore3_item = QTableWidgetItem('WEIGHTED SCORE')
        weightedscore3_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 31, weightedscore3_item)
        table.setSpan(1, 31, 3, 1)

        # CELLS FOR EXAM
        exam_item = QTableWidgetItem('EXAM(30%)')
        exam_item.setTextAlignment(4 | 0x80)
        table.setItem(0, 32, exam_item)
        table.setSpan(0, 32, 1, 3)

        score_item = QTableWidgetItem('SCORE')
        score_item.setTextAlignment(4 | 0x80)
        table.setItem(1, 32, score_item)
        table.setSpan(1, 32, 2, 1)

        eqv11_item = QTableWidgetItem('EQV')
        eqv11_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 33, eqv11_item)
        table.setSpan(1, 33, 3, 1)

        weightedscore4_item = QTableWidgetItem('WEIGHTED SCORE/GRADE')
        weightedscore4_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        table.setItem(1, 34, weightedscore4_item)
        table.setSpan(1, 34, 3, 1)

        lec_item = QTableWidgetItem('LEC GRADE')
        lec_item.setTextAlignment(4 | 0x80)
        table.setItem(0, 35, lec_item)
        table.setSpan(0, 35, 4, 1)

        # For Lecture Tab
        self.lec_tab_layout = QtWidgets.QVBoxLayout(self.lec_tab)
        self.lec_tab_layout.addWidget(table)
        self.grades_tab.setTabText(self.grades_tab.indexOf(self.lec_tab), "Lecture")
        self.grades_tab.setTabToolTip(self.grades_tab.indexOf(self.lec_tab), "Midterm Lecture")

        # Set column widths for the first table
        table.setColumnWidth(0, 50)  # Adjust the width as needed
        table.setColumnWidth(1, 200)  # Adjust the width as needed

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

        # For Laboratory Tab
        self.lab_tab_layout = QtWidgets.QVBoxLayout(self.lab_tab)
        self.lab_tab_layout.addWidget(table2)
        self.grades_tab.setTabText(self.grades_tab.indexOf(self.lab_tab), "Laboratory")

        # Set column widths for the second table
        table2.setColumnWidth(0, 50)  # Adjust the width as needed
        table2.setColumnWidth(1, 200)  # Adjust the width as needed

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

        # Change ResizeToContents to Interactive or Fixed
        table3.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        # Set column widths for the third table
        table3.setColumnWidth(0, 100)  # Adjust the width as needed
        table3.setColumnWidth(1, 250)  # Adjust the width as needed
        table3.setColumnWidth(2, 150)
        table3.setColumnWidth(3, 150)
        table3.setColumnWidth(4, 150)
        table3.setColumnWidth(5, 150)
        table3.setColumnWidth(6, 150)
        table3.setColumnWidth(7, 200)

        # For Summary Tab
        self.summary_tab_layout = QtWidgets.QVBoxLayout(self.summary_tab)
        self.summary_tab_layout.addWidget(table3)
        self.grades_tab.setTabText(self.grades_tab.indexOf(self.summary_tab), "Summary")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.update_all_text_fields()
    sys.exit(app.exec_())
