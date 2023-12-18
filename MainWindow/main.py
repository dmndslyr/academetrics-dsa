import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_MainWindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.viewClassRecord.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.classRecord))
        self.ui.backButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.homepage))

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
