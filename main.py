import json
import os

from PyQt5 import QtCore, QtWidgets


class ToDoDisplay(QtWidgets.QWidget):
    def setupUi(self, Form: QtWidgets.QWidget):
        self.on = False
        Form.setObjectName("Form")
        Form.resize(1065, 691)
        Form.setStyleSheet("background-color: rgb(79, 79, 79); border-radius: 10px;")
        self.todoListLayoutWidget = QtWidgets.QWidget(Form)
        self.todoListLayoutWidget.setGeometry(QtCore.QRect(110, 10, 461, 671))
        self.todoListLayoutWidget.setObjectName("todoListLayoutWidget")
        self.todoListLayout = QtWidgets.QHBoxLayout(self.todoListLayoutWidget)
        self.todoListLayout.setContentsMargins(0, 0, 0, 0)
        self.todoListLayout.setObjectName("todoListLayout")
        self.todoList = QtWidgets.QListWidget(self.todoListLayoutWidget)
        self.todoList.setStyleSheet("background-color: rgb(86, 86, 86); border-radius: 4px;")
        self.todoList.setObjectName("todoList")
        self.todoListLayout.addWidget(self.todoList)
        self.ToolBar = QtWidgets.QFrame(Form)
        self.ToolBar.setGeometry(QtCore.QRect(10, 10, 81, 671))
        self.ToolBar.setStyleSheet("background-color: rgb(86, 86, 86); border-radius: 30")
        self.ToolBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ToolBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ToolBar.setObjectName("ToolBar")
        self.addBtn = QtWidgets.QPushButton(self.ToolBar)
        self.addBtn.setGeometry(QtCore.QRect(10, 10, 61, 61))
        self.addBtn.setStyleSheet("border-radius: 30px;\n"
                                  "background-color: rgb(172, 172, 172);")
        self.addBtn.setText("Add")
        self.addBtn.setObjectName("addBtn")
        self.removeBtn = QtWidgets.QPushButton(self.ToolBar)
        self.removeBtn.setGeometry(QtCore.QRect(10, 80, 61, 61))
        self.removeBtn.setStyleSheet("border-radius: 30px;\n"
                                     "background-color: rgb(172, 172, 172);\n"
                                     "border: 10px;\n"
                                     "border-color: rgb(94, 94, 94);")
        self.removeBtn.setText("Remove")
        self.removeBtn.setObjectName("removeBtn")
        # self.saveBtn = QtWidgets.QPushButton(self.ToolBar)
        # self.saveBtn.setGeometry(QtCore.QRect(10, 540, 61, 61))
        # self.saveBtn.setStyleSheet("border-radius: 30px;\n"
        #                            "background-color: rgb(172, 172, 172);\n"
        #                            "border: 1px;")
        # self.saveBtn.setText("Save")
        # self.saveBtn.setObjectName("saveBtn")
        self.resetBtn = QtWidgets.QPushButton(self.ToolBar)
        self.resetBtn.setGeometry(QtCore.QRect(10, 600, 61, 61))
        self.resetBtn.setStyleSheet("border-radius: 30px;\n"
                                    "border: 1px;\n"
                                    "background-color: rgb(172, 172, 172);")
        self.resetBtn.setText("Reset")
        self.resetBtn.setObjectName("resetBtn")
        self.calendarLayoutWidget = QtWidgets.QWidget(Form)
        self.calendarLayoutWidget.setGeometry(QtCore.QRect(593, 10, 461, 671))
        self.calendarLayoutWidget.setObjectName("calendarLayoutWidget")
        self.calendarLayout = QtWidgets.QHBoxLayout(self.calendarLayoutWidget)
        self.calendarLayout.setContentsMargins(0, 0, 0, 0)
        self.calendarLayout.setObjectName("calendarLayout")
        self.calendar = QtWidgets.QCalendarWidget(self.calendarLayoutWidget)
        self.calendar.setStyleSheet("QMenu {\n"
                                    "\n"
                                    "background-color: rgb(86, 86, 86)\n"
                                    "\n"
                                    "}\n"
                                    "QToolButton {\n"
                                    "\n"
                                    "background-color: rgb(99, 99, 99)\n"
                                    "\n"
                                    "}\n"
                                    "QAbstractItemView {selection-background-color: rgb(85, 88, 92); background-color: rgb(86,86,86); selection-color: rgb(0,255,0)}\n"
                                    "QWidget {background-color: rgb(86, 86, 86); \n"
                                    "alternate-background-color:rgb(100,100,100)};")
        self.calendar.setGridVisible(True)
        self.calendar.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setNavigationBarVisible(True)
        self.calendar.setDateEditEnabled(True)
        self.calendar.setObjectName("calendar")
        self.calendar.selectionChanged.connect(lambda: self.loadTasks(True))
        self.calendarLayout.addWidget(self.calendar)
        self.addBtn.clicked.connect(self.addTask)
        self.removeBtn.clicked.connect(self.removeTask)
        # self.saveBtn.clicked.connect(self.save)
        self.resetBtn.clicked.connect(self.resetTasks)
        self.loadTasks()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setFixedSize(Form.width(), Form.height())
        Form.setWindowTitle("PyCalendar - by Fallcrim")

    def retranslateUi(self, Form):
        pass

    def getAllTasks(self):
        tasks = []
        for i in range(self.todoList.count()):
            tasks.append(self.todoList.item(i).text())
        return tasks

    def addTask(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'New task', 'Enter new task:')

        if ok:
            self.todoList.addItem(text)
            self.save()

    def save(self):
        if not os.path.isfile("tasks.json"):
            with open("tasks.json", "w") as new:
                new.write("{}")
        with open("tasks.json", "r") as f:
            current_tasks = json.load(f)
        current_tasks[self.calendar.selectedDate().toString()] = self.getAllTasks()
        with open("tasks.json", "w") as db:
            json.dump(current_tasks, db)
        date_string = self.calendar.selectedDate().toString()
        print(f"Tasks of day {date_string} saved.")

    def removeTask(self):
        self.todoList.takeItem(self.todoList.currentRow())
        self.save()

    def resetTasks(self, d=True):
        if d:
            diag = QtWidgets.QMessageBox(self)
            diag.question(self, '', "Are you sure to reset all the values?", diag.Yes | diag.No)

            if diag == diag.Yes:
                self.todoList.clear()
            else:
                return
        else:
            self.todoList.clear()

    def loadTasks(self, reset=False):
        if reset:
            self.resetTasks(d=False)
        try:
            with open("tasks.json") as db:
                tasks = json.load(db)
            if self.calendar.selectedDate().toString() in tasks.keys():
                days_tasks = tasks[self.calendar.selectedDate().toString()]
            else:
                days_tasks = []
            for task in days_tasks:
                self.todoList.addItem(task)
        except FileNotFoundError:
            f = open("tasks.json", "w")
            f.write("{}")
            f.close()
            self.loadTasks()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ToDoDisplay()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
