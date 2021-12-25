import datetime
import sys
from PyQt5 import QtCore, QtWidgets


class Display(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ToDo")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 81, 177, 255), stop:1 rgba(137, 255, 28, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.todoList = QtWidgets.QListWidget(self.centralwidget)
        self.todoList.setGeometry(QtCore.QRect(10, 140, 781, 451))
        self.todoList.setObjectName("todoList")
        self.plusBtn = QtWidgets.QPushButton(self.centralwidget)
        self.plusBtn.setGeometry(QtCore.QRect(30, 20, 51, 51))
        self.plusBtn.setStyleSheet("background-image: url(plus.png);")
        self.plusBtn.setObjectName("plusBtn")
        self.plusBtn.clicked.connect(self.getAddInput)
        self.minusBtn = QtWidgets.QPushButton(self.centralwidget)
        self.minusBtn.setGeometry(QtCore.QRect(100, 20, 51, 51))
        self.minusBtn.setStyleSheet("background-image: url(cross.png);")
        self.minusBtn.setObjectName("minusBtn")
        self.minusBtn.clicked.connect(self.getRemInput)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionadd = QtWidgets.QAction(MainWindow)
        self.actionadd.setObjectName("actionAdd")
        self.actionrem = QtWidgets.QAction(MainWindow)
        self.actionrem.setObjectName("actionRem")

        self.plusBtn.setStyleSheet("background-image: url(plus.png);\nbackground-color: rgb(199, 199, 199);")
        self.minusBtn.setStyleSheet("background-image: url(cross.png);\nbackground-color: rgb(199, 199, 199);")
        self.todoList.setStyleSheet("background-color: rgb(85, 255, 255);\nfont: 87 11pt \"Arial Black\";")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        current_time = datetime.datetime.now().strftime("%d.%m.%Y")
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDo - " + str(current_time)))

    def getAddInput(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter new task:')

        if ok:
            self.newTask(text)

    def getRemInput(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter task to remove:')

        if ok:
            self.removeTask(text)

    def newTask(self, task: str):
        self.todoList.addItem(task)
        dialog = QtWidgets.QDialog(self)
        if dialog:
            return

    def removeTask(self, name: str):
        items = []
        for i in range(self.todoList.count()):
            items.append(self.todoList.item(i))
        for item in items:
            if item.text() == name:
                index = items.index(item)
                self.todoList.takeItem(index)
        dialog = QtWidgets.QDialog(self)
        if dialog:
            return




app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Display()
ui.setupUi(MainWindow)


MainWindow.show()
sys.exit(app.exec_())
