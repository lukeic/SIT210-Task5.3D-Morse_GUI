import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

import UI
from MorseEncoder import MorseEncoder


class MorseCoder(QtWidgets.QMainWindow, UI.Ui_MainWindow):

    encoder = MorseEncoder()

    def __init__(self, parent=None):
        super(MorseCoder, self).__init__(parent)
        self.setupUi(self)
        self.messageInput.returnPressed.connect(self.send_message)
        self.btnSend.clicked.connect(self.send_message)
        self.btnExit.clicked.connect(self.handle_exit)

    def send_message(self):
        self.encoder.encode(self.messageInput.text())
        self.messageInput.clear()

    def cleanup(self):
        self.encoder.dispose()

    def closeEvent(self, event):
        self.cleanup()
        event.accept()

    def handle_exit(self):
        self.cleanup()
        self.close()


def main():
    app = QApplication(sys.argv)
    form = MorseCoder()
    form.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
