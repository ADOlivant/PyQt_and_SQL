from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys
import re

class MainWindow(QMainWindow):
    """Adding Data to SQL Database with PyQt"""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Product")

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("coffeeshop.db")
        self.db.open()

        self.name_label = QLabel("Name")
        self.pound_symbol = QLabel("£")
        self.price_label = QLabel("Price")
        self.type_label = QLabel("TypeID")
        self.title_label = QLabel("""<html>
                                          <body>
                                               <p><span style=" font-size:18pt; font-weight:1000;">Add Product</span></p>
                                          </body>
                                     </html>""")
        #self.title_label.Qt.RichText()
        
        self.name_line_edit = QLineEdit()
        self.price_line_edit = QLineEdit()
        self.type_spin_box = QSpinBox()

        self.submit_changes_push_button = QPushButton("Submit Changes")
        self.reset_push_button = QPushButton("Reset")

        self.price_layout = QGridLayout()
        self.price_layout.addWidget(self.pound_symbol,0,0)
        self.price_layout.addWidget(self.price_line_edit,0,1)
        self.price_layout_widget = QWidget()
        self.price_layout_widget.setLayout(self.price_layout)

        self.data_layout = QGridLayout()
        self.data_layout.addWidget(self.name_label,0,0)
        self.data_layout.addWidget(self.price_label,1,0)
        self.data_layout.addWidget(self.type_label,2,0)
        self.data_layout.addWidget(self.name_line_edit,0,1)
        self.data_layout.addWidget(self.price_layout_widget,1,1)
        self.data_layout.addWidget(self.type_spin_box,2,1)
        self.data_layout_widget = QWidget()
        self.data_layout_widget.setLayout(self.data_layout)

        self.button_layout = QGridLayout()
        self.button_layout.addWidget(self.submit_changes_push_button,0,0)
        self.button_layout.addWidget(self.reset_push_button,0,1)
        self.button_layout_widget = QWidget()
        self.button_layout_widget.setLayout(self.button_layout)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.data_layout_widget)
        self.layout.addWidget(self.button_layout_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()


        

        
