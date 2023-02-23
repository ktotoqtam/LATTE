from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic, QtWidgets, QtCore
import sys, sqlite3

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("addEditCoffee.ui", self)

        self.add.clicked.connect(self.addShow)
        self.edit.clicked.connect(self.editShow)

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

        uic.loadUi("aECa.ui", self)

        self.addb.clicked.connect(self.add_clicked)

    def add_clicked(self):
        with sqlite3.connect("coffee.db") as db:
            cur = db.cursor()

            query = f'''INSERT INTO coffee(сорт, описание, цена, тип, степень, объем)
                       VALUES('{self.sort.text()}', '{self.opis.text()}', '{self.price.text()}',
                       '{self.type.text()}', '{self.step.text()}', '{self.volume.text()}')'''

            cur.execute(query)


class EditWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("aECe.ui", self)

        self.edbit.clicked.connect(self.edit_clicked)

    def edit_clicked(self):
        with sqlite3.connect("coffee.db") as db:
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
