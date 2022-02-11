from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime,QTime,QDate,Qt
import calendar 
import datetime 
import sys
import sqlite3


class Remainder(object):
    def getvar(self,i):
        self.SaveIn= i
    def setup(self, MainWindow):
        MainWindow.setObjectName("SCHEDULE NOTIFIER")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(160, 60, 471, 411))
        self.tableView.setObjectName("tableView")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(290, 370, 221, 51))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.accepted.connect(lambda:self.SaveData(MainWindow))
        self.buttonBox.rejected.connect(lambda:self.EXIT(MainWindow))
        self.buttonBox.setObjectName("buttonBox")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(270, 110, 251, 41))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.dateEdit = QtWidgets.QDateEdit(self.splitter)
        self.dateEdit.setMinimumDate(QtCore.QDate.currentDate())
        self.dateEdit.setMaximumDate(QtCore.QDate(2050, 12, 29))
        self.dateEdit.setCalendarPopup(True)
        self.Dateset=datetime.datetime.now().day
        self.Yearset=datetime.datetime.now().year
        self.Monthset=datetime.datetime.now().month
        self.Dayset=calendar.day_name[calendar.weekday(self.Yearset,self.Monthset,self.Dateset)]
        self.dateEdit.dateChanged.connect(self.onDateChanged)   #date 
        self.dateEdit.setObjectName("dateEdit")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(270, 180, 251, 41))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.splitter_2)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(270, 250, 251, 51))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_3 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.timeEdit = QtWidgets.QTimeEdit(self.splitter_3)
        self.timeEdit.setTime(QTime().currentTime())
        self.Hourset=datetime.datetime.now().hour
        self.Minset=datetime.datetime.now().minute
        self.timeEdit.timeChanged.connect(self.timechangehandle)
        self.timeEdit.setObjectName("timeEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 320, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380, 320, 141, 41))
        self.Taskset="Unnamed task"
        self.lineEdit.textChanged.connect(self.taskchanged)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuTitle = QtWidgets.QMenu(self.menubar)
        self.menuTitle.setObjectName("menuTitle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuTitle.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Date"))
        self.label_2.setText(_translate("MainWindow", "Day"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Sunday"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Monday"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Tuesday"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Wednesday"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Thursday"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Friday"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Saturday"))
        self.comboBox.setCurrentIndex(calendar.weekday(self.Yearset,self.Monthset,self.Dateset))
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.label_3.setText(_translate("MainWindow", "Time"))
        self.label_4.setText(_translate("MainWindow", "Task"))
        self.menuTitle.setTitle(_translate("MainWindow", "Set Remainder"))

    def onDateChanged(self, qDate):
        self.Dateset=qDate.day()
        self.Monthset=qDate.month()
        self.Yearset=qDate.year()
        self.comboBox.setCurrentIndex(calendar.weekday(self.Yearset,self.Monthset,self.Dateset))
    
    def selectionchange(self):
        self.Dayset=self.comboBox.currentText()

    def timechangehandle(self):
        self.Hourset=self.timeEdit.time().hour()
        self.Minset=self.timeEdit.time().minute()

    def taskchanged(self):
        self.Taskset=str(self.lineEdit.text())

    
    def SaveData(self,MainWindow):
        conn=sqlite3.connect("Data.db")
        c=conn.cursor()
        if(self.SaveIn==0):
            c.execute("INSERT INTO School (Task,Date,Month,Year,Hour,Min,Day) VALUES(?,?,?,?,?,?,?)",(self.Taskset,self.Dateset,self.Monthset,self.Yearset,self.Hourset,self.Minset,self.Dayset))
        elif(self.SaveIn==1):
            c.execute("INSERT INTO Office (Task,Date,Month,Year,Hour,Min,Day) VALUES(?,?,?,?,?,?,?)",(self.Taskset,self.Dateset,self.Monthset,self.Yearset,self.Hourset,self.Minset,self.Dayset))
        elif(self.SaveIn==2):
            c.execute("INSERT INTO Gathering (Task,Date,Month,Year,Hour,Min,Day) VALUES(?,?,?,?,?,?,?)",(self.Taskset,self.Dateset,self.Monthset,self.Yearset,self.Hourset,self.Minset,self.Dayset))
        elif(self.SaveIn==3):
            c.execute("INSERT INTO Chores (Task,Date,Month,Year,Hour,Min,Day) VALUES(?,?,?,?,?,?,?)",(self.Taskset,self.Dateset,self.Monthset,self.Yearset,self.Hourset,self.Minset,self.Dayset))
        elif(self.SaveIn==4):
            c.execute("INSERT INTO Medical (Task,Date,Month,Year,Hour,Min,Day) VALUES(?,?,?,?,?,?,?)",(self.Taskset,self.Dateset,self.Monthset,self.Yearset,self.Hourset,self.Minset,self.Dayset))
        elif(self.SaveIn==5):
            c.execute("INSERT INTO Submission (Task,Date,Month,Year,Hour,Min,Day) VALUES(?,?,?,?,?,?,?)",(self.Taskset,self.Dateset,self.Monthset,self.Yearset,self.Hourset,self.Minset,self.Dayset))
        elif(self.SaveIn==6):
            c.execute("INSERT INTO Others (Task,Date,Month,Year,Hour,Min,Day) VALUES(?,?,?,?,?,?,?)",(self.Taskset,self.Dateset,self.Monthset,self.Yearset,self.Hourset,self.Minset,self.Dayset))
        
        conn.commit()
        conn.close()
        MainWindow.hide()

    def EXIT(self,MainWindow):
        MainWindow.hide()
        

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Remainder()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

