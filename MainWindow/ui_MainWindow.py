from PyQt5 import QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        icon = QIcon()
        icon.addFile(u"../../../../../../../PycharmProjects/pythonProject/FinalProject/Home_Page/ACADEMETRICS LOGO.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.profile = QPushButton(self.centralwidget)
        self.profile.setObjectName(u"profile")
        self.profile.setGeometry(QRect(1140, 50, 71, 71))
        self.profile.setAutoFillBackground(False)
        self.profile.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; \n"
"	background-color: #00FFFFFF;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:pressed,\n"
"QPushButton:checked,\n"
"QPushButton:hover {\n"
"    background-color: #949494; \n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"PROFILE BUTTON.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profile.setIcon(icon1)
        self.profile.setIconSize(QSize(60, 60))
        self.profile_menu = QMenu(self.centralwidget)
        self.logout_action = QAction("Log Out", self.centralwidget)
        self.logout_action.triggered.connect(self.logout)
        self.profile_menu.addAction(self.logout_action)
        self.profile.setMenu(self.profile_menu)
        self.header = QLabel(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(0, 0, 1281, 151))
        self.header.setPixmap(QPixmap(u"HEADER WITH TEXT CROPPED PNG.png"))
        self.header.setScaledContents(True)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 150, 1281, 571))
        self.homepage = QWidget()
        self.homepage.setObjectName(u"homepage")
        self.viewIndivRecord = QPushButton(self.homepage)
        self.viewIndivRecord.setObjectName(u"viewIndivRecord")
        self.viewIndivRecord.setEnabled(True)
        self.viewIndivRecord.setGeometry(QRect(460, 390, 421, 71))
        font = QFont()
        font.setFamily(u"Gotham Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(QFont.Normal)
        self.viewIndivRecord.setFont(font)
        self.viewIndivRecord.setMouseTracking(True)
        self.viewIndivRecord.setAcceptDrops(True)
        self.viewIndivRecord.setLayoutDirection(Qt.LeftToRight)
        self.viewIndivRecord.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; \n"
"	background-color: #FFF728; color: #002F6C; \n"
"    padding: 5px;\n"
"}\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"    background-color: #949494; \n"
"    text-decoration: underline;\n"
"}\n"
"QPushButton:hover {\n"
"	text-decoration: underline;\n"
"}")
        self.viewIndivRecord.setAutoDefault(False)
        self.viewIndivRecord.setFlat(False)
        self.subjectCodeLabel = QLabel(self.homepage)
        self.subjectCodeLabel.setObjectName(u"subjectCodeLabel")
        self.subjectCodeLabel.setGeometry(QRect(50, 40, 481, 91))
        font1 = QFont()
        font1.setFamily(u"Gotham Black")
        font1.setPointSize(28)
        self.subjectCodeLabel.setFont(font1)
        self.subjectCodeLabel.setStyleSheet(u"QLabel {\n"
"	color: #002F6C;\n"
"    letter-spacing: -3px;\n"
"}\n"
"")
        self.subjectCodeLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.viewClassRecord = QPushButton(self.homepage)
        self.viewClassRecord.setObjectName(u"viewClassRecord")
        self.viewClassRecord.setEnabled(True)
        self.viewClassRecord.setGeometry(QRect(460, 230, 421, 71))
        self.viewClassRecord.setFont(font)
        self.viewClassRecord.setMouseTracking(True)
        self.viewClassRecord.setAcceptDrops(True)
        self.viewClassRecord.setLayoutDirection(Qt.LeftToRight)
        self.viewClassRecord.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; \n"
"	background-color: #FFF728; color: #002F6C; \n"
"    padding: 5px;\n"
"}\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"    background-color: #949494; \n"
"    text-decoration: underline;\n"
"}\n"
"QPushButton:hover {\n"
"	text-decoration: underline;\n"
"}")
        self.viewClassRecord.setAutoDefault(False)
        self.viewClassRecord.setFlat(False)
        self.subjectLabel = QLabel(self.homepage)
        self.subjectLabel.setObjectName(u"subjectLabel")
        self.subjectLabel.setGeometry(QRect(50, 120, 381, 16))
        font2 = QFont()
        font2.setFamily(u"Gotham")
        font2.setPointSize(12)
        self.subjectLabel.setFont(font2)
        self.subjectLabel.setStyleSheet(u"color: blue;\n"
"letter-spacing: -1px;")
        self.semesterLabel = QLabel(self.homepage)
        self.semesterLabel.setObjectName(u"semesterLabel")
        self.semesterLabel.setGeometry(QRect(50, 140, 391, 16))
        self.semesterLabel.setFont(font2)
        self.semesterLabel.setStyleSheet(u"color: blue; letter-spacing: -1px;")
        self.stackedWidget.addWidget(self.homepage)
        self.classRecord = QWidget()
        self.classRecord.setObjectName(u"classRecord")
        self.classRecordText = QLabel(self.classRecord)
        self.classRecordText.setObjectName(u"classRecordText")
        self.classRecordText.setGeometry(QRect(470, 90, 381, 21))
        font3 = QFont()
        font3.setFamily(u"Gotham")
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setWeight(QFont.Bold)
        self.classRecordText.setFont(font3)
        self.classRecordText.setStyleSheet(u"color: #002F6C;\n"
"letter-spacing: -1px;")
        self.classRecordText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.finaltermButton = QPushButton(self.classRecord)
        self.finaltermButton.setObjectName(u"finaltermButton")
        self.finaltermButton.setEnabled(True)
        self.finaltermButton.setGeometry(QRect(770, 260, 301, 71))
        self.finaltermButton.setFont(font)
        self.finaltermButton.setMouseTracking(True)
        self.finaltermButton.setAcceptDrops(True)
        self.finaltermButton.setLayoutDirection(Qt.LeftToRight)
        self.finaltermButton.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; \n"
"	background-color: #FFF728; color: #002F6C; \n"
"    padding: 5px;\n"
"}\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"    background-color: #949494; \n"
"    text-decoration: underline;\n"
"}\n"
"QPushButton:hover {\n"
"	text-decoration: underline;\n"
"}")
        self.finaltermButton.setAutoDefault(False)
        self.finaltermButton.setFlat(False)
        self.semesterLabel_2 = QLabel(self.classRecord)
        self.semesterLabel_2.setObjectName(u"semesterLabel_2")
        self.semesterLabel_2.setGeometry(QRect(140, 150, 391, 16))
        self.semesterLabel_2.setFont(font2)
        self.semesterLabel_2.setStyleSheet(u"color: blue; letter-spacing: -1px;")
        self.semestral = QPushButton(self.classRecord)
        self.semestral.setObjectName(u"semestral")
        self.semestral.setEnabled(True)
        self.semestral.setGeometry(QRect(530, 390, 301, 71))
        self.semestral.setFont(font)
        self.semestral.setMouseTracking(True)
        self.semestral.setAcceptDrops(True)
        self.semestral.setLayoutDirection(Qt.LeftToRight)
        self.semestral.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; \n"
"	background-color: #FFF728; color: #002F6C; \n"
"    padding: 5px;\n"
"}\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"    background-color: #949494; \n"
"    text-decoration: underline;\n"
"}\n"
"QPushButton:hover {\n"
"	text-decoration: underline;\n"
"}")
        self.semestral.setAutoDefault(False)
        self.semestral.setFlat(False)
        self.subjectCodeLabel_2 = QLabel(self.classRecord)
        self.subjectCodeLabel_2.setObjectName(u"subjectCodeLabel_2")
        self.subjectCodeLabel_2.setGeometry(QRect(140, 50, 481, 91))
        self.subjectCodeLabel_2.setFont(font1)
        self.subjectCodeLabel_2.setStyleSheet(u"QLabel {\n"
"	color: #002F6C;\n"
"    letter-spacing: -3px;\n"
"}\n"
"")
        self.subjectCodeLabel_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.subjectLabel_2 = QLabel(self.classRecord)
        self.subjectLabel_2.setObjectName(u"subjectLabel_2")
        self.subjectLabel_2.setGeometry(QRect(140, 130, 381, 16))
        self.subjectLabel_2.setFont(font2)
        self.subjectLabel_2.setStyleSheet(u"color: blue;\n"
"letter-spacing: -1px;")
        self.backButton = QPushButton(self.classRecord)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(60, 80, 61, 71))
        self.backButton.setAutoFillBackground(False)
        self.backButton.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; \n"
"	background-color: #00FFFFFF;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:pressed,\n"
"QPushButton:checked,\n"
"QPushButton:hover {\n"
"    background-color: #949494; \n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"BACK BUTTON.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backButton.setIcon(icon2)
        self.backButton.setIconSize(QSize(60, 60))
        self.midtermsButton = QPushButton(self.classRecord)
        self.midtermsButton.setObjectName(u"midtermsButton")
        self.midtermsButton.setEnabled(True)
        self.midtermsButton.setGeometry(QRect(310, 260, 301, 71))
        self.midtermsButton.setFont(font)
        self.midtermsButton.setMouseTracking(True)
        self.midtermsButton.setAcceptDrops(True)
        self.midtermsButton.setLayoutDirection(Qt.LeftToRight)
        self.midtermsButton.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; \n"
"	background-color: #FFF728; color: #002F6C; \n"
"    padding: 5px;\n"
"}\n"
"QPushButton:pressed,\n"
"QPushButton:checked {\n"
"    background-color: #949494; \n"
"    text-decoration: underline;\n"
"}\n"
"QPushButton:hover {\n"
"	text-decoration: underline;\n"
"}")
        self.midtermsButton.setAutoDefault(False)
        self.midtermsButton.setFlat(False)
        self.stackedWidget.addWidget(self.classRecord)
        MainWindow.setCentralWidget(self.centralwidget)
        self.header.raise_()
        self.profile.raise_()
        self.stackedWidget.raise_()

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.viewIndivRecord.setDefault(False)
        self.viewClassRecord.setDefault(False)
        self.finaltermButton.setDefault(False)
        self.semestral.setDefault(False)
        self.midtermsButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Academetrics", None))
        self.profile.setText("")
#if QT_CONFIG(shortcut)
        self.profile.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.header.setText("")
        self.viewIndivRecord.setText(QCoreApplication.translate("MainWindow", u"INDIVIDUAL RECORD", None))
        self.subjectCodeLabel.setText(QCoreApplication.translate("MainWindow", u"EDWARD", None))
        self.viewClassRecord.setText(QCoreApplication.translate("MainWindow", u"CLASS RECORD", None))
        self.subjectLabel.setText(QCoreApplication.translate("MainWindow", u"DATA STRUCTURES AND ALGORTHMS", None))
        self.semesterLabel.setText(QCoreApplication.translate("MainWindow", u"Academic Year 2023-2024, 1st Semester", None))
        self.classRecordText.setText(QCoreApplication.translate("MainWindow", u"CLASS RECORD", None))
        self.finaltermButton.setText(QCoreApplication.translate("MainWindow", u"FINAL TERM", None))
        self.semesterLabel_2.setText(QCoreApplication.translate("MainWindow", u"Academic Year 2023-2024, 1st Semester", None))
        self.semestral.setText(QCoreApplication.translate("MainWindow", u"SEMESTRAL", None))
        self.subjectCodeLabel_2.setText(QCoreApplication.translate("MainWindow", u"CpE 114 | BSCpE 2A", None))
        self.subjectLabel_2.setText(QCoreApplication.translate("MainWindow", u"DATA STRUCTURES AND ALGORTHMS", None))
        self.backButton.setText("")
#if QT_CONFIG(shortcut)
        self.backButton.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.midtermsButton.setText(QCoreApplication.translate("MainWindow", u"MIDTERMS", None))
    # retranslateUi
    def logout(self):
        # Implement the logout functionality here
        sys.exit(0)
