from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
from StockCrawler import Stock_Crawler

class Ui_MainWindow(object):
    def __init__(self):
        self.stockCrawler = Stock_Crawler()

    def SetupUi(self, MainWindow):
        MainWindow.setObjectName("StockDB")
        MainWindow.resize(1200, 500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1050, 20, 120, 30))
        self.pushButton.setObjectName("pushbutton")
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setCentralWidget(self.centralwidget)
     
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Parse Today Stock"))

    def parseStock(self):
        self.stockCrawler.crawl_one_month(1101, date.today())

    def SetupEventListeners(self):
        self.pushButton.clicked.connect(self.parseStock)
        

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.SetupUi(self)
        self.ui.SetupEventListeners()