from PyQt5.QtGui import QIcon

import tracker
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, \
    QTableWidgetItem, QHeaderView, QMessageBox, QInputDialog


# GUI
    # table 
        # n rows x 4 columns
        # header
        # content
        # update table
        # reset table

    # buttons
        # refresh
        # add new item
        # update count
        # edit price
        # delete item
        # commit changes to file

class gui:

    #########################################



#################################################################################################################

    app = QApplication([])
    window = QWidget()

    layout = QHBoxLayout()

    #########################################

    tracker.tracker.newItem("apple", 10, 1.24)
    tracker.tracker.newItem("pear", 15, 0.99)
    tracker.tracker.newItem("grape", 100, 0.12)

    def tableWidget(*args):
        tableWidget = QWidget()
        tableLayout = QVBoxLayout()
        table = QTableWidget(24,3)
        table.setHorizontalHeaderLabels("Name;Count;Price".split(";"))

        for i in range (0, tracker.itemTotal):
            table.setItem(i,0, QTableWidgetItem(tracker.itemDict["itemName"][i]))
            table.setItem(i,1, QTableWidgetItem(str(tracker.itemDict["itemCount"][i])))
            table.setItem(i,2, QTableWidgetItem(str(tracker.itemDict["itemPrice"][i])))

        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tableLayout.addWidget(table)
        tableWidget.setLayout(tableLayout)
        return tableWidget
    layout.addWidget(tableWidget()) # table widget

    ##################################################

    buttonStrip = QWidget()
    buttonLayout = QVBoxLayout()

    refreshTable = QPushButton()
    refreshTable.setIcon(QIcon("resources/refresh.png"))
    addItem = QPushButton()
    addItem.setIcon(QIcon("resources/add.png"))
    updateCount = QPushButton()
    updateCount.setIcon(QIcon("resources/update.png"))
    updatePrice = QPushButton()
    updatePrice.setIcon(QIcon("resources/edit.png"))
    deleteItem = QPushButton()
    deleteItem.setIcon(QIcon("resources/delete.png"))
    commitTable = QPushButton()
    commitTable.setIcon(QIcon("resources/commit.png"))

    buttonLayout.addWidget(refreshTable)
    buttonLayout.addWidget(addItem)
    buttonLayout.addWidget(updateCount)
    buttonLayout.addWidget(updatePrice)
    buttonLayout.addWidget(deleteItem)
    buttonLayout.addWidget(commitTable)
    buttonStrip.setLayout(buttonLayout)
    layout.addWidget(buttonStrip) # button widget

    ######################################

    def add(*args):
        tracker.tracker.newItem("Name", count=10, price=1.12)
        print("Item Added")
        gui.window.repaint()
        pass

    def count(*args):
        tracker.tracker.updateCount("Name", count=15)
        print("Count updated.")
        gui.window.repaint()
        pass

    def price(*args):
        tracker.tracker.updatePrice("Name", price=1.25)
        print("Price updated.")
        gui.window.repaint()
        pass

    def delete(*args):
        tracker.tracker.deleteItem("Name")
        print("Deleted.")
        gui.window.repaint()
        pass

    def commit(*args):
        print("Committed")
        pass

    refreshTable.clicked.connect(tableWidget)
    addItem.clicked.connect(add)
    updateCount.clicked.connect(count)
    updatePrice.clicked.connect(price)
    deleteItem.clicked.connect(delete)
    commitTable.clicked.connect(commit)

    ############################################

    window.setLayout(layout)
    window.show()
    app.exec()
