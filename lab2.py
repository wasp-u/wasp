import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class StartWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.name = QLabel("ПІБ")
        self.number = QLabel("Номер")
        self.group = QLabel("Група")
        StartWindow.namew = QLineEdit()
        StartWindow.namew.setPlaceholderText("Osadchiy Yuriy")
        StartWindow.numberw = QLineEdit()
        StartWindow.numberw.setPlaceholderText("18")
        StartWindow.groupw = QLineEdit()
        StartWindow.groupw.setPlaceholderText("ІО-64")

        self.next = QPushButton("Next")
        self.next.setAutoDefault(True)

        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.name,0,0)
        self.grid.addWidget(self.number,1,0)
        self.grid.addWidget(self.group,2,0)
        self.grid.addWidget(StartWindow.namew,0,1,1,2)
        self.grid.addWidget(StartWindow.numberw,1,1,1,2)
        self.grid.addWidget(StartWindow.groupw,2,1)
        self.grid.addWidget(self.next,2,2)

        self.setLayout(self.grid)

        self.next.clicked.connect(self.showEvent)

        self.resize(300, 200)
        self.center()
        self.setWindowTitle('Start Window')


    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def showEvent(self):
        self.setVisible(False)
        self.mw = MainWindow()
        self.mw.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.nextwindow = QPushButton("Next")
        self.name = QLabel("ПІБ: " + StartWindow.namew.text())
        self.group = QLabel("Група: " + StartWindow.groupw.text())
        self.number = QLabel("Номер: "+ StartWindow.numberw.text())
        self.var = QLabel("Варіант: " + str((int(StartWindow.numberw.text())+(int(StartWindow.groupw.text().split("-")[1])%60))%30+1))

        self.grid = QGridLayout()
        self.grid.setSpacing(5)

        self.grid.addWidget(self.name,0,0)
        self.grid.addWidget(self.number,2,0)
        self.grid.addWidget(self.group,1,0)
        self.grid.addWidget(self.var,3,0)
        self.grid.addWidget(self.nextwindow,4,0)

        self.setLayout(self.grid)

        #self.nextwindow.clicked.connect(self.showEvent)

        self.resize(300, 200)
        self.center()
        self.setWindowTitle('MainWIndow')

    def showEvent(self):
        self.setVisible(False)
        self.sw = SecondWindow()
        self.sw.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

"""class SecondWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = StartWindow()
    w.show()
    sys.exit(app.exec_())
