from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import sqlite3
conn=sqlite3.connect('database.db')




class Ui_Saved(object):
    def setupUi(self, Saved):
        Saved.setObjectName("Saved")
        Saved.resize(973, 550)
        Saved.setStyleSheet("background-color: #2C3336;\n"
"font: 63 12pt \"Nunito\";")
        self.DatabaseBrowser = QtWidgets.QTextBrowser(Saved)
        self.DatabaseBrowser.setGeometry(QtCore.QRect(70, 130, 871, 361))
        self.DatabaseBrowser.setStyleSheet("background-color: white;\n"
"border-radius: 10px;")
        self.DatabaseBrowser.setObjectName("DatabaseBrowser")
        self.heading = QtWidgets.QLabel(Saved)
        self.heading.setGeometry(QtCore.QRect(420, 30, 181, 41))
        self.heading.setStyleSheet("color: cyan;\n"
"font: 81 24pt \"Nunito ExtraBold\";\n"
"")
        self.heading.setObjectName("heading")
        self.DatabaseRefresh = QtWidgets.QPushButton(Saved)
        self.DatabaseRefresh.setGeometry(QtCore.QRect(450, 500, 81, 31))
        self.DatabaseRefresh.setStyleSheet("border-radius:10px;\n"
"background-color: #3CB7A1;\n"
"color: white;")
        self.DatabaseRefresh.setObjectName("DatabaseRefresh")

        self.retranslateUi(Saved)
        QtCore.QMetaObject.connectSlotsByName(Saved)
        self.DatabaseRefresh.clicked.connect(self.getdb)
    def getdb(self):
        
        x=" "
    
        for row in conn.execute("select info from checking"):
            x=x+str(row[0])
            
        self.DatabaseBrowser.append(str(x))   
       
        
            
        
    def retranslateUi(self, Saved):
        _translate = QtCore.QCoreApplication.translate
        Saved.setWindowTitle(_translate("Saved", "Saved"))
        self.heading.setText(_translate("Saved", "Saved Data"))
        self.DatabaseRefresh.setText(_translate("Saved", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Saved = QtWidgets.QDialog()
    ui = Ui_Saved()
    ui.setupUi(Saved)
    Saved.show()
    sys.exit(app.exec_())
