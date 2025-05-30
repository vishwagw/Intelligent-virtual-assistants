# Graphical user interface:
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ELSA 3.1")
        MainWindow.resize(1500, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1450, 950))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ELSA/utils/images/trinity.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1180, 800, 101, 51))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);\n" "font: 75 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1310, 800, 101, 51))
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 0, 0);\n" "font: 75 18pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 401, 91))
        self.label_2.setText("")
        #self.label_2.setPixmap(QtGui.QPixmap("ELSA/utils/images/initiating.gif"))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(640, 30, 291, 61))
        self.textBrowser.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n" "background-color:transparent;\ncolor:white;" "border-radius:none;\n" "")
        self.textBrowser.setObjectName("textBrowser")
        
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(930, 30, 291, 61))
        self.textBrowser_2.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n" "background-color:transparent;\ncolor:white;" "border-radius:none;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(1000, 500, 431, 281))
        self.textBrowser_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n" "background-color:transparent;\ncolor:white;")
        self.textBrowser_3.setObjectName("textBrowser_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) 
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
