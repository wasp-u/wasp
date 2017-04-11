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
        self.nextwindow = QPushButton("START")
        self.nextwindow.setAutoDefault(True)
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

        self.nextwindow.clicked.connect(self.showEvent)

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

class SecondWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        bg = "#353638"
        appearance = self.palette()
        appearance.setColor(QPalette.Active, QPalette.Window,
                     QColor(bg))
        appearance.setColor(QPalette.Inactive, QPalette.Window,
                     QColor(bg))
        self.setPalette(appearance)

        self.tabWidget1 = QWidget(self)
        self.tabWidget1.setStyleSheet("QWidget { background-color: #4c88ff }")
        SecondWindow.tabWidget2 = QWidget(self)
        SecondWindow.tabWidget3 = QWidget(self)

        self.tabs = QTabWidget()
        self.tabs.addTab(self.tabWidget1,'window &2')
        self.tabs.addTab(SecondWindow.tabWidget2,'window &3')
        self.tabs.addTab(SecondWindow.tabWidget3,'window &4')

        self.save = QPushButton("Save")
        self.load = QPushButton("Load")
        self.clear = QPushButton("Clear")
        self.man = QLabel("Man:")
        self.woman = QLabel("Woman:")
        self.set = QLabel("Your set:")
        self.radioA = QRadioButton('set A')
        self.radioB = QRadioButton('set B')

        self.listMan = QListWidget()
        self.listWoman = QListView()
        self.listSet = QListView()

        self.ManNames = ['lol','kek','cheburek']
        for Item in self.ManNames:
            self.listMan.addItem(Item)

        model = QStandardItemModel(self.listWoman)

        self.WomanNames = ['Анна','Анастасия','Алёна','Елена','Андрюха']

        for name in self.WomanNames:
            item = QStandardItem(name)
            model.appendRow(item)

        self.listWoman.setModel(model)

        self.grid = QGridLayout(self.tabWidget1)
        self.grid.setSpacing(5)
        self.grid.addWidget(self.radioA,0,0)
        self.grid.addWidget(self.radioB,0,1)
        self.grid.addWidget(self.man,1,0)
        self.grid.addWidget(self.woman,1,1)
        self.grid.addWidget(self.set,1,2,1,2)
        self.grid.addWidget(self.listSet,2,2,1,2)
        self.grid.addWidget(self.listMan,2,0)
        self.grid.addWidget(self.listWoman,2,1)
        self.grid.addWidget(self.clear,0,2)
        self.grid.addWidget(self.save,3,2)
        self.grid.addWidget(self.load,3,3)
        self.tabWidget1.setLayout(self.grid)

        self.maingrid = QGridLayout()
        self.maingrid.setSpacing(5)
        self.maingrid.addWidget(self.tabs,0,0)

        self.setLayout(self.maingrid)

        self.resize(600, 400)
        self.center()
        self.setWindowTitle('MainWIndow')


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

class ThirdWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        ThirdWindow.setA = QListWidget()
        ThirdWindow.setB = QListWidget()
        self.matrixS = QLabel('lol')
        self.matrixR = QLabel('kek')

        self.grid = QGridLayout(SecondWindow.tabWidget2)
        self.grid.setSpacing(5)
        self.grid.addWidget(ThirdWindow.setA,0,0)
        self.grid.addWidget(ThirdWindow.setB,0,1)
        self.grid.addWidget(self.matrixR,0,2)
        self.grid.addWidget(self.matrixS,1,0,1,3)

        SecondWindow.tabWidget2.setLayout(self.grid)

        self.show()

class FourthWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):


        self.grid = QGridLayout(ThirdWindow.tabWidget3)
        self.grid.setSpacing(5)


        SecondWindow.tabWidget3.setLayout(self.grid)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SecondWindow()
    w.show()
    sys.exit(app.exec_())
