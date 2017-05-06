import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    
    def initUI(self):

        self.statusBar().showMessage('Not Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(self.handleButton)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.show()


    def handleButton(self):
        self.statusBar().showMessage('Ready')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
