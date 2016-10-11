#coding: utf8
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUiType

app = QApplication(sys.argv)
app.setApplicationName('test')
form_class, base_class = loadUiType('window.ui')


class MainWindow(QDialog, form_class):
    key = 'abcdefghijklmnopqrstuvwxyz'
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)

        self.setupUi(self)

        self.pushButton.clicked.connect(self.buttonClick)
        self.EncodeButton.clicked.connect(self.EncodeClick)
        self.button_im_dec.clicked.connect(self.ImportDecButton)
        self.buttonDecode.clicked.connect(self.DecodeClick)
        self.btnClear.clicked.connect(self.Clear1)
        self.btnClear2.clicked.connect(self.Clear2)
        self.btnButeForce.clicked.connect(self.BruteForce)


    def buttonClick(self):
        self.textBrowser.clear()
        f = open('encode.txt')
        string = f.read()
        f.close()

        self.textBrowser.append(string)

    def EncodeClick(self):
        self.textBrowser_2.clear()
        n = int(self.lineEdit.text())
        f = open('encode.txt')
        plaintext = f.read()
        f.close()

        self.textBrowser_2.append(self.encrypt(n, plaintext))
        f = open('decode.txt', 'w')
        f.write(self.encrypt(n, plaintext))
        f.close()


    def DecodeClick(self):
        self.textBrowser.clear()
        n = int(self.lineEdit.text())
        f = open('decode.txt')
        plaintext = f.read()
        f.close()

        self.textBrowser.append(self.decrypt(n, plaintext))
        f = open('encode.txt', 'w')
        f.write(self.decrypt(n, plaintext))
        f.close()

    def encrypt(self, n, plaintext):
        result = ''

        for l in plaintext.lower():
            try:
                i = (self.key.index(l) + n) % 26
                result += self.key[i]
            except ValueError:
                result += l

        return result.lower()

    def decrypt(self, n, ciphertext):
        """Decrypt the string and return the plaintext"""
        result = ''

        for l in ciphertext:
            try:
                i = (self.key.index(l) - n) % 26
                result += self.key[i]
            except ValueError:
                result += l



        return result

    def ImportDecButton(self):
        self.textBrowser_2.clear()
        f = open('decode.txt')
        string = f.read()
        f.close()

        self.textBrowser_2.append(string)


    def BruteForce(self):
        self.textBrowser_3.clear()

        f = open('decode.txt')
        plaintext = f.read()
        f.close()

        self.textBrowser_3.append("Your translated text is:")

        for key in range(33):
            self.textBrowser_3.append(str(key) + " : " + self.decrypt(key, plaintext))





    def Clear1(self):
        self.textBrowser.clear()


    def Clear2(self):
        self.textBrowser_2.clear()


#-----------------------------------------------------#
form = MainWindow()
form.setWindowTitle('test')
form.show()
sys.exit(app.exec_())