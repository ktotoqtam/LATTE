from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic, QtWidgets, QtCore
import sys, sqlite3
import _aECa

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.add.clicked.connect(self.addShow)
        self.edit.clicked.connect(self.editShow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(200, 100, 201, 91))
        self.add.setObjectName("add")
        self.edit = QtWidgets.QPushButton(self.centralwidget)
        self.edit.setGeometry(QtCore.QRect(200, 220, 201, 91))
        self.edit.setObjectName("edit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add.setText(_translate("MainWindow", "Добавить"))
        self.edit.setText(_translate("MainWindow", "Изменить"))

    def addShow(self):
        self.setHidden(True)

        self._add = AddWindow()
        self._add.show()

    def editShow(self):
        self.setHidden(True)

        self._edit = EditWindow()
        self._edit.show()


class AddWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.addb.clicked.connect(self.add_clicked)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sort = QtWidgets.QLineEdit(self.centralwidget)
        self.sort.setGeometry(QtCore.QRect(90, 10, 113, 20))
        self.sort.setObjectName("sort")
        self.step = QtWidgets.QLineEdit(self.centralwidget)
        self.step.setGeometry(QtCore.QRect(90, 40, 113, 20))
        self.step.setObjectName("step")
        self.type = QtWidgets.QLineEdit(self.centralwidget)
        self.type.setGeometry(QtCore.QRect(90, 70, 113, 20))
        self.type.setObjectName("type")
        self.price = QtWidgets.QLineEdit(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(90, 130, 113, 20))
        self.price.setObjectName("price")
        self.volume = QtWidgets.QLineEdit(self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(90, 160, 113, 20))
        self.volume.setObjectName("volume")
        self.opis = QtWidgets.QLineEdit(self.centralwidget)
        self.opis.setGeometry(QtCore.QRect(90, 100, 113, 20))
        self.opis.setObjectName("opis")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_6.setObjectName("label_6")
        self.addb = QtWidgets.QPushButton(self.centralwidget)
        self.addb.setGeometry(QtCore.QRect(300, 60, 211, 61))
        self.addb.setObjectName("addb")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Сорт"))
        self.label_2.setText(_translate("MainWindow", "степень"))
        self.label_3.setText(_translate("MainWindow", "описание"))
        self.label_4.setText(_translate("MainWindow", "цена"))
        self.label_5.setText(_translate("MainWindow", "объем"))
        self.label_6.setText(_translate("MainWindow", "тип"))
        self.addb.setText(_translate("MainWindow", "Добавить"))

    def add_clicked(self):
        with sqlite3.connect("../data/coffee.db") as db:
            cur = db.cursor()

            query = f'''INSERT INTO coffee(сорт, описание, цена, тип, степень, объем)
                       VALUES('{self.sort.text()}', '{self.opis.text()}', '{self.price.text()}',
                       '{self.type.text()}', '{self.step.text()}', '{self.volume.text()}')'''

            cur.execute(query)


class EditWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.edbit.clicked.connect(self.edit_clicked)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sort = QtWidgets.QLineEdit(self.centralwidget)
        self.sort.setGeometry(QtCore.QRect(90, 10, 113, 20))
        self.sort.setObjectName("sort")
        self.step = QtWidgets.QLineEdit(self.centralwidget)
        self.step.setGeometry(QtCore.QRect(90, 40, 113, 20))
        self.step.setObjectName("step")
        self.type = QtWidgets.QLineEdit(self.centralwidget)
        self.type.setGeometry(QtCore.QRect(90, 70, 113, 20))
        self.type.setObjectName("type")
        self.price = QtWidgets.QLineEdit(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(90, 130, 113, 20))
        self.price.setObjectName("price")
        self.volume = QtWidgets.QLineEdit(self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(90, 160, 113, 20))
        self.volume.setObjectName("volume")
        self.opis = QtWidgets.QLineEdit(self.centralwidget)
        self.opis.setGeometry(QtCore.QRect(90, 100, 113, 20))
        self.opis.setObjectName("opis")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_6.setObjectName("label_6")
        self.edbit = QtWidgets.QPushButton(self.centralwidget)
        self.edbit.setGeometry(QtCore.QRect(300, 60, 211, 61))
        self.edbit.setObjectName("edbit")
        self.id = QtWidgets.QLineEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(90, 190, 113, 20))
        self.id.setObjectName("id")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 190, 171, 21))
        self.label_8.setStyleSheet("color: rgb(255, 0, 4);")
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Сорт"))
        self.label_2.setText(_translate("MainWindow", "степень"))
        self.label_3.setText(_translate("MainWindow", "описание"))
        self.label_4.setText(_translate("MainWindow", "цена"))
        self.label_5.setText(_translate("MainWindow", "объем"))
        self.label_6.setText(_translate("MainWindow", "тип"))
        self.edbit.setText(_translate("MainWindow", "Изменить"))
        self.label_7.setText(_translate("MainWindow", "ID"))
        self.label_8.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">ОБЯЗАТЕЛЬНОЕ ПОЛЕ</span></p></body></html>"))

    def edit_clicked(self):
        with sqlite3.connect("../data/coffee.db") as db:
            cur = db.cursor()

            query = f'''UPDATE coffee
                        SET column = value
                        WHERE id = {self.id.text()}'''

            if self.id.text().strip() != '':
                if self.sort.text() != '':
                    cur.execute(f'''UPDATE coffee
                        SET сорт = {self.sort.text()}
                        WHERE id = {self.id.text()}''')

                if self.price.text() != '':
                    cur.execute(f'''UPDATE coffee
                        SET цена = {self.price.text()}
                        WHERE id = {self.id.text()}''')

                if self.volume.text() != '':
                    cur.execute(f'''UPDATE coffee
                        SET объем = {self.volume.text()}
                        WHERE id = {self.id.text()}''')

                if self.type.text() != '':
                    cur.execute(f'''UPDATE coffee
                        SET тип = {self.type.text()}
                        WHERE id = {self.id.text()}''')

                if self.step.text() != '':
                    cur.execute(f'''UPDATE coffee
                        SET степень = {self.step.text()}
                        WHERE id = {self.id.text()}''')

                if self.opis.text() != '':
                    cur.execute(f'''UPDATE coffee
                        SET описание = {self.opis.text()}
                        WHERE id = {self.id.text()}''')


app = QApplication(sys.argv)
window = Main()
window.show()
app.exec()
