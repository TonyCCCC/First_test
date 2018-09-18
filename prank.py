import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import random


class MainDialog(QDialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Background, QBrush(QPixmap('1.gif')))
        self.setPalette(palette1)
        self.setAutoFillBackground(1)
        self.button1 = QPushButton(self)
        self.button1.setText('Catch me~')
        self.button1.move(200, 250)
        self.button2 = QPushButton(self)
        self.button2.setText('Give up bro.')
        self.button2.move(240, 250)

        #bg = QLabel(self)
        #bg.setPixmap(QPixmap('1.gif'))
        #bg.move(220, 10)

        self.connect(self.button1, SIGNAL('clicked()'), self.changepos)
        self.connect(self.button2, SIGNAL('clicked()'), self.end)
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Prank')
        self.kill = 0

    def changepos(self):
        self.button1.move(random.randrange(0, 500-self.button1.width()), random.randrange(0, 500-self.button1.height()))

    def end(self):
        msg = QMessageBox.information(self, 'You lose!', 'You lose!')
        self.kill = 1
        self.close()

    def closeEvent(self, event):
        print('event')
        if self.kill == 1:
            event.accept()
        else:
            reply = QMessageBox.question(self, 'Message', "关不掉～")
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainDialog()
    win.show()
    sys.exit(app.exec_())