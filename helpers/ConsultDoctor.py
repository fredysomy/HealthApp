from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QMessageBox
import requests
import html5lib


class Ui_ConsultDoctor(object):
    def setupUi(self, ConsultDoctor):
        ConsultDoctor.setObjectName("ConsultDoctor")
        ConsultDoctor.resize(960, 606)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        ConsultDoctor.setFont(font)
        ConsultDoctor.setStyleSheet("font: 75 12pt \"Nunito\";\n"
"background-color: rgb(44, 51, 54);")
        self.centralwidget = QtWidgets.QWidget(ConsultDoctor)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 60, 341, 51))
        self.label.setStyleSheet("color:cyan;\n"
"font: 81 22pt \"Nunito ExtraBold\";")
        self.label.setObjectName("label")
        self.specialist = QtWidgets.QLineEdit(self.centralwidget)
        self.specialist.setGeometry(QtCore.QRect(320, 170, 251, 31))
        self.specialist.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Nunito Black\";")
        self.specialist.setPlaceholderText("")
        self.specialist.setObjectName("specialist")
        self.location = QtWidgets.QLineEdit(self.centralwidget)
        self.location.setGeometry(QtCore.QRect(320, 220, 251, 31))
        self.location.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Nunito Black\";")
        self.location.setPlaceholderText("")
        self.location.setObjectName("location")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 170, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:cyan;\n"
"font: 87 11pt \"Nunito\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 230, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:cyan;\n"
"font: 87 11pt \"Nunito\";")
        self.label_3.setObjectName("label_3")
        self.consult = QtWidgets.QPushButton(self.centralwidget)
        self.consult.setGeometry(QtCore.QRect(600, 190, 91, 31))
        self.consult.setStyleSheet("border-radius:10px;\n"
"font: 75 11pt \"Nunito\";\n"
"background-color: #3CB7A1;\n"
"color: white;")
        self.consult.setObjectName("consult")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(120, 290, 681, 301))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Nunito Black\";\n"
"border-radius: 10px;")
        self.textBrowser.setObjectName("textBrowser")
        self.consultsavedata = QtWidgets.QPushButton(self.centralwidget)
        self.consultsavedata.setGeometry(QtCore.QRect(820, 340, 131, 31))
        self.consultsavedata.setStyleSheet("border-radius:10px;\n"
"font: 75 11pt \"Nunito\";\n"
"background-color: #3CB7A1;\n"
"color: white;")
        self.consultsavedata.setObjectName("consultsavedata")
        self.consultsavetext = QtWidgets.QPushButton(self.centralwidget)
        self.consultsavetext.setGeometry(QtCore.QRect(820, 390, 131, 31))
        self.consultsavetext.setStyleSheet("border-radius:10px;\n"
"font: 75 11pt \"Nunito\";\n"
"background-color: #3CB7A1;\n"
"color: white;")
        self.consultsavetext.setObjectName("consultsavetext")
        ConsultDoctor.setCentralWidget(self.centralwidget)

        self.retranslateUi(ConsultDoctor)
        QtCore.QMetaObject.connectSlotsByName(ConsultDoctor)
        self.consult.clicked.connect(self.PractoProject)
        self.consultsavetext.clicked.connect(self.SavePractoFile)
    def PractoProject(self):
        s1=self.specialist.text()
        s2=self.location.text().split(",")
        s3=s2[0]
        s4=s2[1]
        url="https://www.practo.com/search?results_type=doctor&q=%5B%7B%22word%22%3A%22{}%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%2C%7B%22word%22%3A%22{}%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22locality%22%7D%5D&city={}".format(s1,s3,s4)
        re=requests.get(url)
        so=BeautifulSoup(re.content,'html5lib')
        a=so.find_all('div',class_="u-border-general--bottom")
        addd=" "
        for i in range(0,len(a)):
            try:
                c=a[i].find('div',class_="listing-doctor-card")
                d=c.find('div',class_="info-section")
                url="https://www.practo.com"+d.find('a')['href']
                name=d.find('a').getText()
                try:
                    recurreq=requests.get(url)
                    sop=BeautifulSoup(recurreq.content,'html5lib')
                    add=sop.find('p',class_="c-profile--clinic__address").getText()
                        
                except:
                    pass    
                f=d.find_all('div',class_="u-grey_3-text")
                proff=f[0].find('h3').getText()

                h=d.find_all('div',class_="uv2-spacer--sm-top")   
                addd=addd+"\n"+name+"\n"+url+h[0].getText()+"\n"+add+"\n"+proff+"\n"+"#######################################"+"\n"
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Zero Input Error")
                msg.setInformativeText("An error occured")
                msg.setWindowTitle('Error')
                msg.exec_()
        self.textBrowser.append(str(addd))

    def SavePractoFile(self):
        s="../txtfiles/"+self.specialist.text()+"in"+self.location.text()+".txt"
        fd=open(s,'w',encoding='utf-8')
        fd.write(self.textBrowser.toPlainText())
        fd.close()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("File Succesfully saved")
        msg.setInformativeText("FIle saved as "+s)
        msg.setWindowTitle('Saved')
        msg.exec_()
    def retranslateUi(self, ConsultDoctor):
        _translate = QtCore.QCoreApplication.translate
        ConsultDoctor.setWindowTitle(_translate("ConsultDoctor", "ConsultDoctor"))
        self.label.setText(_translate("ConsultDoctor", "Consult A Doctor"))
        self.label_2.setText(_translate("ConsultDoctor", "Specialist"))
        self.label_3.setText(_translate("ConsultDoctor", "Location"))
        self.consult.setText(_translate("ConsultDoctor", "Search"))
        self.consultsavedata.setText(_translate("ConsultDoctor", "Save to Database"))
        self.consultsavetext.setText(_translate("ConsultDoctor", "Save as text file"))
        self.location.setPlaceholderText(_translate("ConsultDoctor","Place,City ( Both required ) "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConsultDoctor = QtWidgets.QMainWindow()
    ui = Ui_ConsultDoctor()
    ui.setupUi(ConsultDoctor)
    ConsultDoctor.show()
    sys.exit(app.exec_())
