# Form implementation generated from reading ui file 'creator.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 475)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        self.title.setGeometry(QtCore.QRect(170, 0, 441, 81))
        font = QtGui.QFont()
        font.setFamily("Bernard MT Condensed")
        font.setPointSize(25)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("title")
        self.options = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.options.setGeometry(QtCore.QRect(10, 90, 781, 331))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        self.options.setFont(font)
        self.options.setObjectName("options")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.paladin = QtWidgets.QRadioButton(parent=self.tab)
        self.paladin.setGeometry(QtCore.QRect(130, 50, 82, 17))
        self.paladin.setObjectName("paladin")
        self.mage = QtWidgets.QRadioButton(parent=self.tab)
        self.mage.setGeometry(QtCore.QRect(280, 50, 82, 17))
        self.mage.setObjectName("mage")
        self.ranger = QtWidgets.QRadioButton(parent=self.tab)
        self.ranger.setGeometry(QtCore.QRect(420, 50, 82, 17))
        self.ranger.setObjectName("ranger")
        self.healer = QtWidgets.QRadioButton(parent=self.tab)
        self.healer.setGeometry(QtCore.QRect(570, 50, 82, 17))
        self.healer.setObjectName("healer")
        self.options.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.human = QtWidgets.QRadioButton(parent=self.tab_4)
        self.human.setGeometry(QtCore.QRect(110, 50, 82, 17))
        self.human.setObjectName("human")
        self.elf = QtWidgets.QRadioButton(parent=self.tab_4)
        self.elf.setGeometry(QtCore.QRect(280, 50, 82, 17))
        self.elf.setObjectName("elf")
        self.dwarf = QtWidgets.QRadioButton(parent=self.tab_4)
        self.dwarf.setGeometry(QtCore.QRect(420, 50, 82, 17))
        self.dwarf.setObjectName("dwarf")
        self.lizard = QtWidgets.QRadioButton(parent=self.tab_4)
        self.lizard.setGeometry(QtCore.QRect(580, 50, 82, 17))
        self.lizard.setObjectName("lizard")
        self.options.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.male = QtWidgets.QRadioButton(parent=self.tab_3)
        self.male.setGeometry(QtCore.QRect(220, 50, 82, 17))
        self.male.setObjectName("male")
        self.female = QtWidgets.QRadioButton(parent=self.tab_3)
        self.female.setGeometry(QtCore.QRect(340, 50, 91, 20))
        self.female.setObjectName("female")
        self.none = QtWidgets.QRadioButton(parent=self.tab_3)
        self.none.setGeometry(QtCore.QRect(470, 50, 82, 17))
        self.none.setObjectName("none")
        self.options.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lock = QtWidgets.QRadioButton(parent=self.tab_2)
        self.lock.setGeometry(QtCore.QRect(90, 30, 121, 51))
        self.lock.setObjectName("lock")
        self.pickpocket = QtWidgets.QRadioButton(parent=self.tab_2)
        self.pickpocket.setGeometry(QtCore.QRect(230, 30, 121, 51))
        self.pickpocket.setObjectName("pickpocket")
        self.perception = QtWidgets.QRadioButton(parent=self.tab_2)
        self.perception.setGeometry(QtCore.QRect(480, 30, 121, 51))
        self.perception.setObjectName("perception")
        self.barter = QtWidgets.QRadioButton(parent=self.tab_2)
        self.barter.setGeometry(QtCore.QRect(620, 30, 121, 51))
        self.barter.setObjectName("barter")
        self.sneak = QtWidgets.QRadioButton(parent=self.tab_2)
        self.sneak.setGeometry(QtCore.QRect(360, 30, 121, 51))
        self.sneak.setObjectName("sneak")
        self.options.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.cruel = QtWidgets.QRadioButton(parent=self.tab_5)
        self.cruel.setGeometry(QtCore.QRect(40, 30, 121, 51))
        self.cruel.setObjectName("cruel")
        self.greedy = QtWidgets.QRadioButton(parent=self.tab_5)
        self.greedy.setGeometry(QtCore.QRect(230, 30, 121, 51))
        self.greedy.setObjectName("greedy")
        self.righteous = QtWidgets.QRadioButton(parent=self.tab_5)
        self.righteous.setGeometry(QtCore.QRect(630, 30, 121, 51))
        self.righteous.setObjectName("righteous")
        self.jealous = QtWidgets.QRadioButton(parent=self.tab_5)
        self.jealous.setGeometry(QtCore.QRect(430, 30, 121, 51))
        self.jealous.setObjectName("jealous")
        self.options.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.confirm = QtWidgets.QPushButton(parent=self.tab_6)
        self.confirm.setGeometry(QtCore.QRect(330, 100, 111, 41))
        self.confirm.setObjectName("confirm")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.tab_6)
        self.lineEdit.setGeometry(QtCore.QRect(290, 50, 191, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.name = QtWidgets.QLabel(parent=self.tab_6)
        self.name.setGeometry(QtCore.QRect(170, 50, 81, 21))
        self.name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name.setObjectName("name")
        self.label = QtWidgets.QLabel(parent=self.tab_6)
        self.label.setGeometry(QtCore.QRect(40, 170, 691, 91))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.options.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.options.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Character Creator"))
        self.title.setText(_translate("MainWindow", "Character Creator"))
        self.paladin.setText(_translate("MainWindow", "Paladin"))
        self.mage.setText(_translate("MainWindow", "Mage"))
        self.ranger.setText(_translate("MainWindow", "Ranger"))
        self.healer.setText(_translate("MainWindow", "Healer"))
        self.options.setTabText(self.options.indexOf(self.tab), _translate("MainWindow", "Class"))
        self.human.setText(_translate("MainWindow", "Human"))
        self.elf.setText(_translate("MainWindow", "Elf"))
        self.dwarf.setText(_translate("MainWindow", "Dwarf"))
        self.lizard.setText(_translate("MainWindow", "Lizard"))
        self.options.setTabText(self.options.indexOf(self.tab_4), _translate("MainWindow", "Race"))
        self.male.setText(_translate("MainWindow", "Male"))
        self.female.setText(_translate("MainWindow", "Female"))
        self.none.setText(_translate("MainWindow", "None"))
        self.options.setTabText(self.options.indexOf(self.tab_3), _translate("MainWindow", "Gender"))
        self.lock.setText(_translate("MainWindow", "Locksmith"))
        self.pickpocket.setText(_translate("MainWindow", "Pickpocket"))
        self.perception.setText(_translate("MainWindow", "Perception"))
        self.barter.setText(_translate("MainWindow", "Barter"))
        self.sneak.setText(_translate("MainWindow", "Sneak"))
        self.options.setTabText(self.options.indexOf(self.tab_2), _translate("MainWindow", "Skills"))
        self.cruel.setText(_translate("MainWindow", "Cruel"))
        self.greedy.setText(_translate("MainWindow", "Greedy"))
        self.righteous.setText(_translate("MainWindow", "Righteous"))
        self.jealous.setText(_translate("MainWindow", "Jealous"))
        self.options.setTabText(self.options.indexOf(self.tab_5), _translate("MainWindow", "Traits"))
        self.confirm.setText(_translate("MainWindow", "Confirm"))
        self.name.setText(_translate("MainWindow", "Name"))
        self.options.setTabText(self.options.indexOf(self.tab_6), _translate("MainWindow", "Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
