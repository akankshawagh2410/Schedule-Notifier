import datetime
from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime,QTime,QDate,Qt
import sqlite3
from SET_REMAINDER_1 import Remainder


class Ui_MainWindow(object):
    def SetReamainder(self):
        self.setrem=QtWidgets.QMainWindow()
        self.ui=Remainder()
        self.ui.setup(self.setrem)
        self.ui.getvar(self.comboBox.currentIndex())
        self.setrem.show()
        
    def loadData(self,i):
        conn=sqlite3.connect("Data.db")
        if(i==0):
            que="SELECT * FROM School"
            result = conn.execute(que)
            self.tableWidget.setRowCount(0)
            colno=0
            for rowno,rowdata in enumerate(result):
                self.tableWidget.insertRow(rowno)
                self.tableWidget.setItem(rowno,colno,QtWidgets.QTableWidgetItem(str(rowdata[0])))
                self.tableWidget.setItem(rowno,colno+1,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[1])+"/"+str(rowdata[2])+"/"+str(rowdata[3])+"      ")))
                self.tableWidget.setItem(rowno,colno+2,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[4])+":"+str(rowdata[5])+"      ")))
                self.tableWidget.setItem(rowno,colno+3,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[6])+"      ")))
        elif(i==1):
            que="SELECT * FROM Office"
            result = conn.execute(que)
            self.tableWidget.setRowCount(0)
            colno=0
            for rowno,rowdata in enumerate(result):
                self.tableWidget.insertRow(rowno)
                self.tableWidget.setItem(rowno,colno,QtWidgets.QTableWidgetItem(str(rowdata[0])))
                self.tableWidget.setItem(rowno,colno+1,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[1])+"/"+str(rowdata[2])+"/"+str(rowdata[3])+"      ")))
                self.tableWidget.setItem(rowno,colno+2,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[4])+":"+str(rowdata[5])+"      ")))
                self.tableWidget.setItem(rowno,colno+3,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[6])+"      ")))
        elif(i==2):
            que="SELECT * FROM Gathering"
            result = conn.execute(que)
            self.tableWidget.setRowCount(0)
            colno=0
            for rowno,rowdata in enumerate(result):
                self.tableWidget.insertRow(rowno)
                self.tableWidget.setItem(rowno,colno,QtWidgets.QTableWidgetItem(str(rowdata[0])))
                self.tableWidget.setItem(rowno,colno+1,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[1])+"/"+str(rowdata[2])+"/"+str(rowdata[3])+"      ")))
                self.tableWidget.setItem(rowno,colno+2,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[4])+":"+str(rowdata[5])+"      ")))
                self.tableWidget.setItem(rowno,colno+3,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[6])+"      ")))
        elif(i==3):
            que="SELECT * FROM Chores"
            result = conn.execute(que)
            self.tableWidget.setRowCount(0)
            colno=0
            for rowno,rowdata in enumerate(result):
                self.tableWidget.insertRow(rowno)
                self.tableWidget.setItem(rowno,colno,QtWidgets.QTableWidgetItem(str(rowdata[0])))
                self.tableWidget.setItem(rowno,colno+1,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[1])+"/"+str(rowdata[2])+"/"+str(rowdata[3])+"      ")))
                self.tableWidget.setItem(rowno,colno+2,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[4])+":"+str(rowdata[5])+"      ")))
                self.tableWidget.setItem(rowno,colno+3,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[6])+"      ")))
        elif(i==4):
            que="SELECT * FROM Medical"
            result = conn.execute(que)
            self.tableWidget.setRowCount(0)
            colno=0
            for rowno,rowdata in enumerate(result):
                self.tableWidget.insertRow(rowno)
                self.tableWidget.setItem(rowno,colno,QtWidgets.QTableWidgetItem(str(rowdata[0])))
                self.tableWidget.setItem(rowno,colno+1,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[1])+"/"+str(rowdata[2])+"/"+str(rowdata[3])+"      ")))
                self.tableWidget.setItem(rowno,colno+2,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[4])+":"+str(rowdata[5])+"      ")))
                self.tableWidget.setItem(rowno,colno+3,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[6])+"      ")))
        elif(i==5):
            que="SELECT * FROM Submission"
            result = conn.execute(que)
            self.tableWidget.setRowCount(0)
            colno=0
            for rowno,rowdata in enumerate(result):
                self.tableWidget.insertRow(rowno)
                self.tableWidget.setItem(rowno,colno,QtWidgets.QTableWidgetItem(str(rowdata[0])))
                self.tableWidget.setItem(rowno,colno+1,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[1])+"/"+str(rowdata[2])+"/"+str(rowdata[3])+"      ")))
                self.tableWidget.setItem(rowno,colno+2,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[4])+":"+str(rowdata[5])+"      ")))
                self.tableWidget.setItem(rowno,colno+3,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[6])+"      ")))
        elif(i==6):
            que="SELECT * FROM Others"
            result = conn.execute(que)
            self.tableWidget.setRowCount(0)
            colno=0
            for rowno,rowdata in enumerate(result):
                self.tableWidget.insertRow(rowno)
                self.tableWidget.setItem(rowno,colno,QtWidgets.QTableWidgetItem(str(rowdata[0])))
                self.tableWidget.setItem(rowno,colno+1,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[1])+"/"+str(rowdata[2])+"/"+str(rowdata[3])+"      ")))
                self.tableWidget.setItem(rowno,colno+2,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[4])+":"+str(rowdata[5])+"      ")))
                self.tableWidget.setItem(rowno,colno+3,QtWidgets.QTableWidgetItem(str("      "+str(rowdata[6])+"      ")))
        
        conn.close()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 60, 740, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        self.tableWidget.setHorizontalHeaderLabels(['TASK', 'DATE', 'TIME', 'DAY'])
        #self.loadData(self.comboBox.currentIndex())
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setGeometry(QtCore.QRect(650,525,100,38))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda:self.HideWindow(MainWindow))
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-20, 500, 831, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 460, 486, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Refresh)
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.SetReamainder)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(30, 10, 251, 28))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.splitter)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("School/College")
        self.comboBox.addItem("Office")
        self.comboBox.addItem("Gathering")
        self.comboBox.addItem("Chores")
        self.comboBox.addItem("Medical")
        self.comboBox.addItem("Submission")
        self.comboBox.addItem("Others")
        self.loadData(self.comboBox.currentIndex())
        self.comboBox.currentIndexChanged.connect(self.Callload)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Schedule Notifier"))
        self.tableWidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_3.setText(_translate("MainWindow", "Cancel"))
        self.pushButton.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_2.setText(_translate("MainWindow", "Add Reminder to Domain"))
        self.label.setText(_translate("MainWindow", "DOMAIN"))

    def Callload(self):
        self.loadData(self.comboBox.currentIndex())

    def Refresh(self):
        conn=sqlite3.connect("Data.db")
        c=conn.cursor()
        i=self.comboBox.currentIndex()
        Yeartoberemoved=[datetime.datetime.now().year]
        Monthtoberemoved=[datetime.datetime.now().month,datetime.datetime.now().year]
        hourtodayremove=[datetime.datetime.now().day,datetime.datetime.now().month,datetime.datetime.now().year,datetime.datetime.now().hour]
        Timetodayremove=[datetime.datetime.now().day,datetime.datetime.now().month,datetime.datetime.now().year,datetime.datetime.now().hour,datetime.datetime.now().minute]
        datatoberemoved=[datetime.datetime.now().day,datetime.datetime.now().month,datetime.datetime.now().year]
        if(i==0):
            c.execute("DELETE FROM School WHERE Year < ? ",Yeartoberemoved)
            c.execute("DELETE FROM School WHERE Month < ? And Year = ? ",Monthtoberemoved)
            c.execute("DELETE FROM School WHERE Date < ? AND Month <= ? And Year <= ? ",datatoberemoved)
            c.execute("DELETE FROM School WHERE Date = ? AND Month = ? And Year = ? AND Hour< ? ",hourtodayremove)
            c.execute("DELETE FROM School WHERE Date = ? AND Month = ? And Year = ? AND Hour <= ? And Min<?",Timetodayremove)
        elif(i==1):
            c.execute("DELETE FROM Office WHERE Year < ? ",Yeartoberemoved)
            c.execute("DELETE FROM Office WHERE Month < ? And Year = ? ",Monthtoberemoved)
            c.execute("DELETE FROM Office WHERE Date < ? AND Month <= ? And Year < ? ",datatoberemoved)
            c.execute("DELETE FROM Office WHERE Date = ? AND Month = ? And Year = ? AND Hour< ? ",hourtodayremove)
            c.execute("DELETE FROM Office WHERE Date = ? AND Month = ? And Year = ? AND Hour<= ? And Min<?",Timetodayremove)
        elif(i==2):
            c.execute("DELETE FROM Gathering WHERE Year < ? ",Yeartoberemoved)
            c.execute("DELETE FROM Gathering WHERE Month < ? And Year = ? ",Monthtoberemoved)
            c.execute("DELETE FROM Gathering WHERE Date < ? AND Month <= ? And Year < ? ",datatoberemoved)
            c.execute("DELETE FROM Gathering WHERE Date = ? AND Month = ? And Year = ? AND Hour< ?",hourtodayremove)
            c.execute("DELETE FROM Gathering WHERE Date = ? AND Month = ? And Year = ? AND Hour<= ? And Min<?",Timetodayremove)
        elif(i==3):
            c.execute("DELETE FROM Chores WHERE Year < ? ",Yeartoberemoved)
            c.execute("DELETE FROM Chores WHERE Month < ? And Year = ? ",Monthtoberemoved)
            c.execute("DELETE FROM Chores WHERE Date < ? AND Month <= ? And Year <= ? ",datatoberemoved)
            c.execute("DELETE FROM Chores WHERE Date = ? AND Month = ? And Year = ? AND Hour< ? ",hourtodayremove)
            c.execute("DELETE FROM Chores WHERE Date = ? AND Month = ? And Year = ? AND Hour<= ? And Min<?",Timetodayremove)
        elif(i==4):
            c.execute("DELETE FROM Medical WHERE Year < ? ",Yeartoberemoved)
            c.execute("DELETE FROM Medical WHERE Month < ? And Year = ? ",Monthtoberemoved)
            c.execute("DELETE FROM Medical WHERE Date < ? AND Month <= ? And Year <= ? ",datatoberemoved)
            c.execute("DELETE FROM Medical WHERE Date = ? AND Month = ? And Year = ? AND Hour< ? ",hourtodayremove)
            c.execute("DELETE FROM Medical WHERE Date = ? AND Month = ? And Year = ? AND Hour<= ? And Min<?",Timetodayremove)
        elif(i==5):
            c.execute("DELETE FROM Submission WHERE Year < ? ",Yeartoberemoved)
            c.execute("DELETE FROM Submission WHERE Month < ? And Year = ? ",Monthtoberemoved)
            c.execute("DELETE FROM Submission WHERE Date < ? AND Month <= ? And Year <= ? ",datatoberemoved)
            c.execute("DELETE FROM Submission WHERE Date = ? AND Month = ? And Year = ? AND Hour< ? ",hourtodayremove)
            c.execute("DELETE FROM Submission WHERE Date = ? AND Month = ? And Year = ? AND Hour<= ? And Min<?",Timetodayremove)
        elif(i==6):
            c.execute("DELETE FROM Others WHERE Year < ? ",Yeartoberemoved)
            c.execute("DELETE FROM Others WHERE Month < ? And Year = ? ",Monthtoberemoved)
            c.execute("DELETE FROM Others WHERE Date < ? AND Month <= ? And Year <= ? ",datatoberemoved)
            c.execute("DELETE FROM Others WHERE Date = ? AND Month = ? And Year = ? AND Hour< ? ",hourtodayremove)
            c.execute("DELETE FROM Others WHERE Date = ? AND Month = ? And Year = ? AND Hour<= ? And Min<?",Timetodayremove)
        conn.commit()
        conn.close()
        self.loadData(self.comboBox.currentIndex())

    def HideWindow(self,MainWindow):
        MainWindow.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
