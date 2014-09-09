# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat May 31 21:55:18 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from functools import partial
import os
import sys
sys.path.append(str(os.getcwd()))
import IPVdata

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.hr = 2**24-1
        str_table = ["M1 ERAB Accessibility Rate","M1 ERAB Call Drop Rate","M1 Intra-frequency Handover Success Rate","M1 Inter-frequency Handover Success Rate","M1 Inter-RAT Handover Success Rate (LTE to WCDMA)","M1 Radio Network availability Rate","M1 Packet Loss Rate"]
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600, 500)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1, 1, 600, 500))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        #self.gridLayout.setMargin(0)
        self.gridLayout.setColumnStretch(0,1)
        self.gridLayout.setColumnStretch(1,1)
        self.gridLayout.setColumnStretch(2,1)
        self.gridLayout.setColumnStretch(3,1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.folderPath = QtGui.QLineEdit(self.widget)
        self.folderPath.setObjectName(_fromUtf8("folderPath"))
        self.gridLayout.addWidget(self.folderPath, 0, 0, 1, 2)
        self.folderBrowse = QtGui.QPushButton(self.widget)
        self.folderBrowse.setObjectName(_fromUtf8("folderBrowse"))
        self.gridLayout.addWidget(self.folderBrowse, 0, 2, 1, 1)
        self.siteList = QtGui.QListWidget(self.widget)
        self.siteList.setObjectName(_fromUtf8("siteList"))
        self.gridLayout.addWidget(self.siteList, 1, 0, 3, 2)
        self.siteKeyword = QtGui.QLineEdit(self.widget)
        self.siteKeyword.setObjectName(_fromUtf8("siteKeyword"))
        self.gridLayout.addWidget(self.siteKeyword, 1, 2, 1, 1)
        self.ossResult = QtGui.QTableWidget(7,2,self.widget)
        self.ossResult.setObjectName(_fromUtf8("ossResult"))
        self.ossResult.setVerticalHeaderLabels(str_table)
        self.ossResult.setHorizontalHeaderLabels(["KPI Result", "PASS"])
        #for a in range(len(str_table)):
        #    item = QtGui.QTableWidgetItem(str_table[a]))
        #    self.ossResult.setItem(a,0,item)
        self.gridLayout.addWidget(self.ossResult, 7, 0, 2, 4)
        self.siteFilter = QtGui.QPushButton(self.widget)
        self.siteFilter.setObjectName(_fromUtf8("siteFilter"))
        self.gridLayout.addWidget(self.siteFilter, 2, 2, 1, 1)
        #self.resultCopy = QtGui.QPushButton(self.widget)
        #self.resultCopy.setObjectName(_fromUtf8("resultCopy"))
        #self.gridLayout.addWidget(self.resultCopy, 3, 3, 1, 1)
        self.startDate = QtGui.QLabel(self.widget)
        self.startDate.setObjectName(_fromUtf8("startDate"))
        self.gridLayout.addWidget(self.startDate, 4, 0, 1, 1)
        self.startDateEdit = QtGui.QDateEdit(self.widget)
        self.startDateEdit.setObjectName(_fromUtf8("startDateEdit"))
        self.gridLayout.addWidget(self.startDateEdit, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.endDateEdit = QtGui.QDateEdit(self.widget)
        self.endDateEdit.setObjectName(_fromUtf8("endDateEdit"))
        self.gridLayout.addWidget(self.endDateEdit, 5, 1, 1, 1)
        self.wholeDay = QtGui.QCheckBox(self.widget)
        self.wholeDay.setObjectName(_fromUtf8("wholeDay"))
        self.wholeDay.setCheckState(QtCore.Qt.Checked)
        self.gridLayout.addWidget(self.wholeDay, 3, 2, 1, 1)
        #self.label = QtGui.QLabel(self.widget)
        #self.label.setObjectName(_fromUtf8("label"))
        #self.gridLayout.addWidget(self.label, 4, 2, 1, 1)
        self.timeChoose = QtGui.QPushButton(self.widget)
        self.timeChoose.setObjectName(_fromUtf8("timeChoose"))
        self.gridLayout.addWidget(self.timeChoose, 6, 0, 1, 1)
        

        self.freqlist = QtGui.QComboBox(self.widget)
        self.freqlist.setObjectName(_fromUtf8("freqlist"))
        self.freqlist.addItems(["All","1.8GHz Only","2.6GHz Only"])
        #self.freqlist.setGeometry(QtCore.QRect(0,0,50,21))
        self.gridLayout.addWidget(self.freqlist, 6, 1, 1, 1)


        #self.comboBox = QtGui.QComboBox(self.widget)
        #self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.listHR = QtGui.QListView(self.widget)
        self.gridLayout.addWidget(self.listHR, 4, 2, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 679, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Add the codes here
        self.folderBrowse.clicked.connect(partial(self.browseFolder,self.folderPath))
        self.siteFilter.clicked.connect(self.sitesFilter)
        self.siteList.itemDoubleClicked.connect(partial(self.filterDate))
        self.timeChoose.clicked.connect(self.processData)
        self.wholeDay.stateChanged.connect(self.checkboxFuc)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.folderBrowse.setText(_translate("MainWindow", "1. Browse", None))
        self.siteFilter.setText(_translate("MainWindow", "2. Filter", None))
        #self.resultCopy.setText(_translate("MainWindow", "4. Copy", None))
        self.startDate.setText(_translate("MainWindow", "Start Date:", None))
        self.label_4.setText(_translate("MainWindow", "End Date:", None))
        self.wholeDay.setText(_translate("MainWindow", "Whole Day", None))
        #self.label.setText(_translate("MainWindow", "Selected Hours", None))
        self.timeChoose.setText(_translate("MainWindow", "3. Calc", None))

    def browseFolder(self, lineEdit):
        folderPath = str(QtGui.QFileDialog.getExistingDirectory(caption = "Choose Folder Directory",directory="."))
        if folderPath:
            lineEdit.setText(unicode(folderPath))
            self.data = IPVdata.IPVdata(folderPath)
            self.siteList.setSortingEnabled(True)
            self.siteList.sortItems(QtCore.Qt.AscendingOrder)
            self.siteList.addItems(self.data.returneNBList())
            self.folderBrowse.setEnabled(False)
        else:
            return False     

    def sitesFilter(self):
        tmpstr = list()
        strfilter = str(self.siteKeyword.text())
        for site in self.data.returneNBList():
            if strfilter in site:
                tmpstr.append(site)
        self.siteList.clear()
        self.siteList.addItems(tmpstr)

    def filterDate(self):
        sitename = self.siteList.currentItem().text()
        dateRange = list(self.data.filterDate(sitename))
        startDate = QtCore.QDate()
        startDate.setDate(dateRange[0].year, dateRange[0].month, dateRange[0].day)
        endDate = QtCore.QDate()
        endDate.setDate(dateRange[-1].year, dateRange[-1].month, dateRange[-1].day)
        self.startDateEdit.setDateRange(startDate,endDate)
        self.endDateEdit.setDateRange(startDate,endDate)
        self.startDateEdit.setCalendarPopup(True)
        self.endDateEdit.setCalendarPopup(True)

    def checkboxFuc(self):
        if self.wholeDay.checkState() != QtCore.Qt.Checked:
            self.hr = 2**24-1
            #self.comboBox.clear()
            model = QtGui.QStandardItemModel()
            for i in range(24):
                str_time = str("%2d:00" %i)
                item = QtGui.QStandardItem(str_time)
                item.setCheckState(QtCore.Qt.Checked)
                item.setCheckable(True)
                model.appendRow(item)
            model.itemChanged.connect(self.calcHR)
                #tmp_checkbox = QtGui.QCheckBox(str_time)
                #tmp_checkbox.setCheckState(QtCore.Qt.Checked)
                #tmp_checkbox.stateChanged.connect(partial(self.calcHR, tmp_checkbox, i))
                #self.comboBox.addItem(tmp_checkbox)
            self.listHR.setModel(model)
        else:
            self.hr = 2**24-1
            #self.comboBox.clear()
            #self.comboBox.setEditable(False)

    def calcHR(self, item):
        if item.checkState() != QtCore.Qt.Checked:
            self.hr -= 2**int(item.text().split(':')[0])
        else:
            self.hr += 2**int(item.text().split(':')[0])

    def processData(self):
        self.siteFilter.setEnabled(False)
        self.timeChoose.setEnabled(False)         
        startDate = self.startDateEdit.date().toString("yyyy-MM-dd")
        endDate = self.endDateEdit.date().toString("yyyy-MM-dd")
        sitename = self.siteList.currentItem().text()
        sltHour = self.hr
        flt_cell = str(self.freqlist.currentText())
        oss_result = self.data.processData(str(startDate),str(endDate), int(sltHour), str(sitename), flt_cell)
        if oss_result:
            for a in range(len(oss_result)/2):
                item = QtGui.QTableWidgetItem(str(oss_result[a*2]))
                self.ossResult.setItem(a,0,item)
                item2 = QtGui.QTableWidgetItem(str(oss_result[a*2+1]))
                self.ossResult.setItem(a,1,item2)
        clipboard = QtGui.QApplication.clipboard()
        tmp_txt = '\n'.join([('%s\tPASS' %x) for x in oss_result[::2]])
        clipboard.setText(tmp_txt)
        self.siteFilter.setEnabled(True)
        self.timeChoose.setEnabled(True) 


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

