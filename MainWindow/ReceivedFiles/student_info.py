# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
import add_delete_students  # Take note of this! Place the add_delete_students on the same directory


# Warnings GUI
def show_warning():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText("Student ID is invalid! May be absent or duplicated.")
    msg.setWindowTitle("Invalid ID")

    # Set the icon for the QMessageBox
    icon: QIcon = QIcon()
    icon.addPixmap(QPixmap("ACADEMETRICS LOGO.png"), QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    msg.exec_()


def add_show_confirmation():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Student Enrolled successfully!")
    msg.setWindowTitle("Confirmation")
    icon: QIcon = QIcon()
    icon.addPixmap(QPixmap("ACADEMETRICS LOGO.png"), QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    msg.exec_()


def remove_show_confirmation():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("The Student is removed successfully!")
    msg.setWindowTitle("Confirmation")
    icon: QIcon = QIcon()
    icon.addPixmap(QPixmap("ACADEMETRICS LOGO.png"), QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    msg.exec_()


def blank_warning():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText("Please fill out the text areas with something.")
    msg.setWindowTitle("No Input!")
    icon: QIcon = QIcon()
    icon.addPixmap(QPixmap("ACADEMETRICS LOGO.png"), QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    msg.exec_()


def invalid_id_warning():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText("Please enter a valid id. (e.g. 22-UR-0310)")
    msg.setWindowTitle("Invalid ID Format!")
    icon: QIcon = QIcon()
    icon.addPixmap(QPixmap("ACADEMETRICS LOGO.png"), QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    msg.exec_()


class Ui_MainWindow(object):

    def show_students(self):
        connection = None
        cursor = None
        student_count = 0  # Variable to count the number of students

        try:
            connection = sqlite3.connect('ryan_test_db_1.db')  # Use your own db
            cursor = connection.cursor()

            query = "SELECT student_id, full_name FROM class"  # Use your own table (e.g. class)
            cursor.execute(query)
            rows = cursor.fetchall()

            # Clear existing items from the table
            self.tableWidget.setRowCount(0)

            # Update the table with the retrieved data
            for row_number, row_data in enumerate(rows):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    self.tableWidget.setItem(row_number, column_number, item)

                student_count += 1  # Increment the student count

            # This will limit to one data only!
            cursor.execute("SELECT yrandSection FROM header LIMIT 1")
            section = cursor.fetchone()

            if section:
                # Extract the value from the tuple
                section_value = section[0]

                # Insert the student count into the header table in the database
                update_query = "UPDATE header SET noofstudents = ? WHERE yrandSection = ?"
                cursor.execute(update_query, (student_count, section_value))
                connection.commit()
            else:
                print("No section found.")

        except sqlite3.Error as e:
            print("Database error:", e)
            # Handle the error (e.g., show an error message)

        finally:
            cursor.close()
            connection.close()

        # Update the QLabel with the student count
        self.noofstudentsText.setText(QtCore.QCoreApplication.translate("MainWindow", str(student_count)))

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
        self.update_text_from_database("period", self.periodText)
        self.update_text_from_database("course", self.courseText)
        self.update_text_from_database("subject", self.subjectText)
        self.update_text_from_database("yrandSection", self.yrandSectionText)
        self.update_text_from_database("acadyear", self.acadyearText)
        self.update_text_from_database("semester", self.semesterText)
        self.update_text_from_database("instructor", self.instructorText)


    def add_student_button_clicked(self):
        # Get the student name and ID from the input fields
        inputted_name = self.addStudentName.text()
        student_name = self.add_delete_students_module.auto_capitalize(inputted_name)
        student_id = self.addStudentID.text()

        blank_id = self.add_delete_students_module.check_if_blank(student_id)
        blank_name = self.add_delete_students_module.check_if_blank(student_name)
        validate_id = self.add_delete_students_module.validate_id_input(student_id)

        if blank_id or blank_name:
            blank_warning()
        else:
            # Check if the entered value already exists in the database
            if not validate_id:
                invalid_id_warning()
                self.addStudentID.clear()
            else:
                formatted_id = self.add_delete_students_module.format_id_input(student_id)
                boolean = self.add_delete_students_module.check_id_value(formatted_id)
                if boolean:
                    show_warning()
                    self.addStudentID.clear()

                else:
                    student_to_add = [formatted_id, student_name]

                    # Call the add_student function from the add_delete_students module
                    self.add_delete_students_module.add_student(student_to_add)

                    # Update the table with the new student data
                    self.show_students()
                    add_show_confirmation()
                    # Clear the content of the QLineEdit widgets
                    self.addStudentName.clear()
                    self.addStudentID.clear()


    def semestralBtn_3_clicked(self):
        # Get the student name and ID from the input fields
        student_id = self.removeStudentID.text()

        # Check if the ID is blank
        blank_id = self.add_delete_students_module.check_if_blank(student_id)

        if blank_id:
            blank_warning()
        else:
            # Validate and format the ID
            validate_id = self.add_delete_students_module.validate_id_input(student_id)
            if not validate_id:
                invalid_id_warning()
            else:
                formatted_id = self.add_delete_students_module.format_id_input(student_id)
                # Check if the ID exists
                if self.add_delete_students_module.check_id_value(formatted_id):
                    # Call the delete_student function from the add_delete_students module
                    self.add_delete_students_module.delete_student(formatted_id)

                    # Update the table with the new student data
                    self.show_students()
                    remove_show_confirmation()

                else:
                    show_warning()

        self.removeStudentID.clear()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ACADEMETRICS LOGO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("QMainWindow {\n"
                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #CBE2FC, stop:1 #D8D8D8);\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
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
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setContentsMargins(150, -1, 200, -1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.subjectlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.subjectlabel.setFont(font)
        self.subjectlabel.setObjectName("subjectlabel")
        self.gridLayout_8.addWidget(self.subjectlabel, 2, 0, 1, 1)
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
        self.courseLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.courseLabel.setFont(font)
        self.courseLabel.setObjectName("courseLabel")
        self.gridLayout_8.addWidget(self.courseLabel, 1, 0, 1, 1)
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
        self.yrandSectionLabel = QtWidgets.QLabel(self.centralwidget)
        self.yrandSectionLabel.setStyleSheet("QLabel {\n"
                                             "    font: 700 9pt \"Gotham\";\n"
                                             "    color: #002F6C;\n"
                                             "}\n"
                                             "")
        self.yrandSectionLabel.setObjectName("yrandSectionLabel")
        self.gridLayout_8.addWidget(self.yrandSectionLabel, 3, 0, 1, 1)
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
        self.HLayout = QtWidgets.QHBoxLayout()
        self.HLayout.setObjectName("HLayout")
        self.tablelayout = QtWidgets.QVBoxLayout()
        self.tablelayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.tablelayout.setContentsMargins(20, 20, 20, 20)
        self.tablelayout.setObjectName("tablelayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(57)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(158, 158, 158))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tablelayout.addWidget(self.tableWidget)
        self.HLayout.addLayout(self.tablelayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.HLayout.addItem(spacerItem5)
        self.VLayout = QtWidgets.QVBoxLayout()
        self.VLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.VLayout.setContentsMargins(20, -1, 20, -1)
        self.VLayout.setObjectName("VLayout")
        spacerItem6 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.VLayout.addItem(spacerItem6)
        self.addstudentLayout = QtWidgets.QVBoxLayout()
        self.addstudentLayout.setObjectName("addstudentLayout")
        self.addStudnetLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(20)
        self.addStudnetLabel.setFont(font)
        self.addStudnetLabel.setStyleSheet("QLabel {\n"
                                           "    color: #002F6C;\n"
                                           "    letter-spacing: -3px;\n"
                                           "    background-color: transparent;\n"
                                           "}\n"
                                           "")
        self.addStudnetLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.addStudnetLabel.setObjectName("addStudnetLabel")
        self.addstudentLayout.addWidget(self.addStudnetLabel)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setContentsMargins(100, -1, 0, -1)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.addStudentIDLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.addStudentIDLabel.setFont(font)
        self.addStudentIDLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.addStudentIDLabel.setObjectName("addStudentIDLabel")
        self.gridLayout_11.addWidget(self.addStudentIDLabel, 1, 0, 1, 1)
        self.addStudentName = QtWidgets.QLineEdit(self.centralwidget)
        self.addStudentName.setMaximumSize(QtCore.QSize(200, 16777215))
        self.addStudentName.setStyleSheet("QLineEdit {\n"
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
        self.addStudentName.setObjectName("addStudentName")
        self.gridLayout_11.addWidget(self.addStudentName, 0, 1, 1, 1)
        self.addStudentID = QtWidgets.QLineEdit(self.centralwidget)
        self.addStudentID.setMaximumSize(QtCore.QSize(200, 16777215))
        self.addStudentID.setStyleSheet("QLineEdit {\n"
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
        self.addStudentID.setObjectName("addStudentID")
        self.gridLayout_11.addWidget(self.addStudentID, 1, 1, 1, 1)
        self.addStudentNameLLabel = QtWidgets.QLabel(self.centralwidget)
        self.addStudentNameLLabel.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.addStudentNameLLabel.setFont(font)
        self.addStudentNameLLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.addStudentNameLLabel.setObjectName("addStudentNameLLabel")
        self.gridLayout_11.addWidget(self.addStudentNameLLabel, 0, 0, 1, 1)
        self.addstudentLayout.addLayout(self.gridLayout_11)
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setEnabled(True)
        self.AddButton.setMinimumSize(QtCore.QSize(171, 31))
        self.AddButton.setMaximumSize(QtCore.QSize(171, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.AddButton.setFont(font)
        self.AddButton.setMouseTracking(True)
        self.AddButton.setAcceptDrops(True)
        self.AddButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AddButton.setStyleSheet("QPushButton {\n"
                                     "    border-radius: 10px; \n"
                                     "    background-color: #FFF728; color: #002F6C; \n"
                                     "    padding: 5px;\n"
                                     "}\n"
                                     "QPushButton:pressed,\n"
                                     "QPushButton:checked {\n"
                                     "    background-color: #949494; \n"
                                     "    text-decoration: underline;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    text-decoration: underline;\n"
                                     "}")

        # Assign the instance to the class variable
        self.add_delete_students_module = add_delete_students

        # Connect the button's clicked signal to the add_student_button_clicked function
        self.AddButton.clicked.connect(self.add_student_button_clicked)

        self.AddButton.setAutoDefault(False)
        self.AddButton.setDefault(False)
        self.AddButton.setFlat(False)
        self.AddButton.setObjectName("AddButton")
        self.addstudentLayout.addWidget(self.AddButton, 0, QtCore.Qt.AlignHCenter)
        self.VLayout.addLayout(self.addstudentLayout)
        self.removeLayout = QtWidgets.QVBoxLayout()
        self.removeLayout.setObjectName("removeLayout")
        self.removeStudentLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(20)
        self.removeStudentLabel.setFont(font)
        self.removeStudentLabel.setStyleSheet("QLabel {\n"
                                              "    color: #002F6C;\n"
                                              "    letter-spacing: -3px;\n"
                                              "    background-color: transparent;\n"
                                              "}\n"
                                              "")
        self.removeStudentLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.removeStudentLabel.setObjectName("removeStudentLabel")
        self.removeLayout.addWidget(self.removeStudentLabel)
        spacerItem7 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.removeLayout.addItem(spacerItem7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.removeStudentIDLAbel = QtWidgets.QLabel(self.centralwidget)
        self.removeStudentIDLAbel.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(True)
        font.setWeight(75)
        self.removeStudentIDLAbel.setFont(font)
        self.removeStudentIDLAbel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.removeStudentIDLAbel.setObjectName("removeStudentIDLAbel")
        self.horizontalLayout_2.addWidget(self.removeStudentIDLAbel)
        self.removeStudentID = QtWidgets.QLineEdit(self.centralwidget)
        self.removeStudentID.setMaximumSize(QtCore.QSize(200, 16777215))
        self.removeStudentID.setStyleSheet("QLineEdit {\n"
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
        self.removeStudentID.setObjectName("removeStudentID")
        self.horizontalLayout_2.addWidget(self.removeStudentID)
        self.removeLayout.addLayout(self.horizontalLayout_2)
        self.semestralBtn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.semestralBtn_3.setEnabled(True)
        self.semestralBtn_3.setMinimumSize(QtCore.QSize(171, 31))
        self.semestralBtn_3.setMaximumSize(QtCore.QSize(171, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.semestralBtn_3.setFont(font)
        self.semestralBtn_3.setMouseTracking(True)
        self.semestralBtn_3.setAcceptDrops(True)
        self.semestralBtn_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.semestralBtn_3.setStyleSheet("QPushButton {\n"
                                          "    border-radius: 10px; \n"
                                          "    background-color: #FFF728; color: #002F6C; \n"
                                          "    padding: 5px;\n"
                                          "}\n"
                                          "QPushButton:pressed,\n"
                                          "QPushButton:checked {\n"
                                          "    background-color: #949494; \n"
                                          "    text-decoration: underline;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    text-decoration: underline;\n"
                                          "}")

        self.semestralBtn_3.clicked.connect(self.semestralBtn_3_clicked)

        self.semestralBtn_3.setAutoDefault(False)
        self.semestralBtn_3.setDefault(False)
        self.semestralBtn_3.setFlat(False)
        self.semestralBtn_3.setObjectName("semestralBtn_3")
        self.removeLayout.addWidget(self.semestralBtn_3, 0, QtCore.Qt.AlignHCenter)
        self.VLayout.addLayout(self.removeLayout)
        spacerItem8 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.VLayout.addItem(spacerItem8)
        self.HLayout.addLayout(self.VLayout)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.HLayout.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.HLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Academetrics | Student Info"))
        self.subjectCodeLabel.setText(_translate("MainWindow", "ELEC 111 | BSCpE 2A"))
        self.studetInfolabel.setText(_translate("MainWindow", "STUDENT INFO"))
        self.subjectlabel.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Subject:</span></p></body></html>"))
        self.courseLabel.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Course Code:</span></p></body></html>"))
        self.yrandSectionLabel.setText(_translate("MainWindow",
                                                  "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Yr &amp; Section:</span></p></body></html>"))
        self.periodLabel.setText(_translate("MainWindow", "Period:"))
        self.acadyearLabel.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Academic Year:</span></p></body></html>"))
        self.noofstudentsLabel.setText(_translate("MainWindow", "No. of Students: "))
        self.instructorLabel.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Instructor:</span></p></body></html>"))
        self.semesterLabel.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Semester:</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Student ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        self.addStudnetLabel.setText(_translate("MainWindow", "Add Student"))
        self.addStudentIDLabel.setText(_translate("MainWindow",
                                                  "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Student ID:</span></p></body></html>"))
        self.addStudentNameLLabel.setText(_translate("MainWindow",
                                                     "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Name:</span></p></body></html>"))
        self.AddButton.setText(_translate("MainWindow", "ADD"))
        self.removeStudentLabel.setText(_translate("MainWindow", "Remove Student"))
        self.removeStudentIDLAbel.setText(_translate("MainWindow",
                                                     "<html><head/><body><p><span style=\" font-size:10pt; color:#1b1159;\">Student ID:</span></p></body></html>"))
        self.semestralBtn_3.setText(_translate("MainWindow", "REMOVE"))

        self.show_students()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.show_students()
    MainWindow.show()
    ui.update_all_text_fields()
    sys.exit(app.exec_())
