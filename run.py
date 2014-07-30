from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main import Ui_MainWindow
import sys
import encodings
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.create_convert_options()
        self.ui.pushButton.clicked.connect(self.file_dialog)
        self.ui.pushButton_2.clicked.connect(self.convert)

    def create_convert_options(self):
        self.ui.comboBox.insertItem(0, 'Select')
        self.ui.comboBox_2.insertItem(0, 'Select')
        for e in enumerate(sorted(encodings.aliases.aliases)):
            index = e[0]
            s = e[1]
            self.ui.comboBox.insertItem(index+1, s)
            self.ui.comboBox_2.insertItem(index+1, s)

    def file_dialog(self):
        d = QFileDialog(self)
        d.setFileMode(QFileDialog.ExistingFiles)
        if d.exec():
            s = d.selectedFiles()
            for ss in s:
                self.ui.lineEdit.setText(self.ui.lineEdit.text()+ss+',')

    def convert(self):
        e_from = self.ui.comboBox.currentText()
        e_to = self.ui.comboBox_2.currentText()
        if e_from != e_to:
            for path in self.ui.lineEdit.text().split(','):
                if path != '':
                    f_path, f_name = os.path.split(path)
                    new_f_name = 'redecoded'+f_name
                    new_f_path = os.path.join(f_path, new_f_name)
                    open(new_f_path, 'wb').write(open(path, 'rb').read().decode(e_from).encode(e_to))
        else:
            print('No jednak sobie rowne')
            c_icon = QMessageBox.Icon(QMessageBox.Critical)
            ok_button = QMessageBox.StandardButton(QMessageBox.Ok)
            m = QMessageBox(self)
            m.addButton(ok_button)
            m.setIcon(c_icon)
            m.setText("'From' and 'to' are equal!")
            m.show()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
