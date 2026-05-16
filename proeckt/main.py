import pymysql
import sys
from PyQt6 import QtWidgets
from  PyQt6.QtGui import QPixmap
from vxod import Ui_Form
from  manager import Ui_Form_manager

class Main(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_manager)
    def show_manager(self):
        self.okno = Manager()
        self.okno.show()
        self.hide()
class Manager(QtWidgets.QWidget,Ui_Form_manager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = Main()
    Form.show()
    sys.exit(app.exec())