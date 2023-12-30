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
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(69)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.HLayout.addWidget(self.tableWidget)
        self.verticalLayout.addLayout(self.HLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Academetrics | Semestral Class Record"))
        self.subjectCodeLabel.setText(_translate("MainWindow", "ELEC 111 | BSCpE 2A"))
        self.studetInfolabel.setText(_translate("MainWindow", "CLASS RECORD"))
        self.courseLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Course Code:</span></p></body></html>"))
        self.subjectlabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Subject:</span></p></body></html>"))
        self.periodLabel.setText(_translate("MainWindow", "Period:"))
        self.yrandSectionLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Yr &amp; Section:</span></p></body></html>"))
        self.acadyearLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Academic Year:</span></p></body></html>"))
        self.noofstudentsLabel.setText(_translate("MainWindow", "No. of Students"))
        self.instructorLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Instructor:</span></p></body></html>"))
        self.semesterLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Semester:</span></p></body></html>"))

        # NO. COLUMN
        no_item = QTableWidgetItem('NO.')
        no_item.setTextAlignment(4 | 0x80)
        self.tableWidget.setItem(0, 0, no_item)
        self.tableWidget.setSpan(0, 0, 2, 1)

        # AME OF STUDENT COLUMN
        name_item = QTableWidgetItem('Name of Student')
        name_item.setTextAlignment(4 | 0x80)
        self.tableWidget.setItem(0, 1, name_item)
        self.tableWidget.setSpan(0, 1, 2, 1)

        # MIDTERM COLUMN
        mid_item = QTableWidgetItem('MIDTERM')
        mid_item.setTextAlignment(4 | 0x80)
        self.tableWidget.setItem(0, 2, mid_item)
        self.tableWidget.setSpan(0, 2, 1, 2)

        # CELLS UNDER OTHERS
        mgrade_item = QTableWidgetItem('GRADE')
        mgrade_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        self.tableWidget.setItem(1, 2, mgrade_item)
        self.tableWidget.setSpan(1, 2, 1, 1)

        eqv_item = QTableWidgetItem('NUMERICAL EUIVALENT')
        eqv_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        self.tableWidget.setItem(1, 3, eqv_item)
        self.tableWidget.setSpan(1, 3, 1, 1)

        # FINAL COLUMN
        final_item = QTableWidgetItem('FINAL TERM')
        final_item.setTextAlignment(4 | 0x80)
        self.tableWidget.setItem(0, 4, final_item)
        self.tableWidget.setSpan(0, 4, 1, 2)

        # CELLS UNDER OTHERS
        fgrade_item = QTableWidgetItem('GRADE')
        fgrade_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        self.tableWidget.setItem(1, 4, fgrade_item)
        self.tableWidget.setSpan(1, 4, 1, 1)

        eqv_item = QTableWidgetItem('NUMERICAL EUIVALENT')
        eqv_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        self.tableWidget.setItem(1, 5, eqv_item)
        self.tableWidget.setSpan(1, 5, 1, 1)

        # SEMESTRAL COLUMN
        sem_item = QTableWidgetItem('SEMESTRAL')
        sem_item.setTextAlignment(4 | 0x80)
        self.tableWidget.setItem(0, 6, sem_item)
        self.tableWidget.setSpan(0, 6, 1, 2)

        # CELLS UNDER OTHERS
        sgrade_item = QTableWidgetItem('GRADE')
        sgrade_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        self.tableWidget.setItem(1, 6, sgrade_item)
        self.tableWidget.setSpan(1, 6, 1, 1)

        eqv_item = QTableWidgetItem('NUMERICAL EUIVALENT')
        eqv_item.setTextAlignment(4 | 0x80)  # AlignCenter | AlignVCenter
        self.tableWidget.setItem(1, 7, eqv_item)
        self.tableWidget.setSpan(1, 7, 1, 1)

        # REMARKS COLUMN
        rem_item = QTableWidgetItem('REMARKS')
        rem_item.setTextAlignment(4 | 0x80)
        self.tableWidget.setItem(0, 8, rem_item)
        self.tableWidget.setSpan(0, 8, 2, 1)

        # Change ResizeToContents to Interactive or Fixed
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        # Set column widths for the third table
        self.tableWidget.setColumnWidth(0, 50)  # Adjust the width as needed
        self.tableWidget.setColumnWidth(1, 300)  # Adjust the width as needed
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 150)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setColumnWidth(6, 150)
        self.tableWidget.setColumnWidth(7, 200)
        self.tableWidget.setColumnWidth(8, 200)

        # Add the table to the layout
        self.HLayout.addWidget(self.tableWidget)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.update_all_text_fields()
    sys.exit(app.exec_())
