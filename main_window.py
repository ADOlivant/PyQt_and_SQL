from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from browse_data import *

import sys

class MainWindow(QMainWindow):
    """Main Window of the Program"""
    def __init__(self):
        super().__init__()

        #Set Window Title
        self.setWindowTitle("Coffee Shop | SQL with PyQt4")

        #Create Connection to Database
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("coffeeshop.db")
        self.db.open()

        #create actions
        self.browse_customer = QAction("Customer",self)
        self.browse_product_type = QAction("Product Type",self)
        self.browse_product = QAction("Product",self)
        self.browse_customer_order = QAction("Customer Order",self)
        self.browse_order_item = QAction("Order Item",self)
        self.add_customer = QAction("Customer",self)
        self.add_product_type = QAction("Product Type",self)
        self.add_product = QAction("Product",self)
        self.add_customer_order = QAction("Customer Order",self)
        self.add_order_item = QAction("Order Item",self)
        
        #Create Main Menu Bar
        self.main_menu_bar = QMenuBar()

        #Add Drop Down Menu
        self.add_menu = QMenu("Add")
        self.add_menu.addAction(self.add_customer)
        self.add_menu.addAction(self.add_product_type)
        self.add_menu.addAction(self.add_product)
        self.add_menu.addAction(self.add_customer_order)
        self.add_menu.addAction(self.add_order_item)

        #Browse Drop Down Menu
        self.browse_menu = QMenu("Browse")
        self.browse_menu.addAction(self.browse_customer)
        self.browse_menu.addAction(self.browse_product_type)
        self.browse_menu.addAction(self.browse_product)
        self.browse_menu.addAction(self.browse_customer_order)
        self.browse_menu.addAction(self.browse_order_item)

        #Add Drop Down Menus to Main Menu Bar
        self.main_menu_bar.addMenu(self.add_menu)
        self.main_menu_bar.addMenu(self.browse_menu)

        #Set Main Menu in Main Program
        self.setMenuBar(self.main_menu_bar)

        #Connections
        self.browse_customer.triggered.connect(self.browse_customers)
        

    def browse_customers(self):
        self.browse_widget = BrowseData(self.db)
        self.setCentralWidget(self.browse_widget)
        print("Hello")
        
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
