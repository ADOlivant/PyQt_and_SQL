from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

class MainWindow(QMainWindow):
    """simple example using QtSql"""
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Coffee Shop SQL with PyQt")

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("coffeeshop.db")
        self.db.open()

        self.table_view = QTableView()
        self.submit_changes_button = QPushButton("Submit Changes")
        self.submit_changes_button.setEnabled(False)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table_view)
        self.layout.addWidget(self.submit_changes_button)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

        self.create_query_model()

        #connection
        self.submit_changes_button.clicked.connect(self.update_customers)

    def create_table_model(self):
        self.model = QSqlTableModel()
        self.model.setTable("Products")
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.table_view.setModel(self.model)
        self.table_view.model().select()

    def update_customers(self):
        self.model.submitAll()

    def create_query_model(self):
        query = QSqlQuery()
        query.prepare("""SELECT *
                         FROM Product
                         WHERE Price > ?""")
        query.addBindValue(4)
        query.exec_()

        self.model = QSqlQueryModel()
        self.model.setQuery(query)

        self.table_view.setModel(self.model)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
