from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

class BrowseData(QWidget):
    """to browse data using table view"""
    def __init__(self,db):
        super().__init__()

        self.db = db

        self.table_view = QTableView()
        self.submit_changes_button = QPushButton("Submit Changes")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table_view)
        self.layout.addWidget(self.submit_changes_button)

        self.setLayout(self.layout)

        self.create_table_model()

        #Connections 
        self.submit_changes_button.clicked.connect(self.update_customers)

    def create_table_model(self):
        self.model = QSqlTableModel()
        self.model.setTable("Customer")
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.table_view.setModel(self.model)
        self.table_view.model().select()

    def update_customers(self):
        self.model.submitAll() 
