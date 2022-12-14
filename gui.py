# Created by: PyQt5 UI code generator 5.15.6

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(444, 349)
        MainWindow.setStyleSheet(
            "QWidget {\n" "    background-color: #253e5d;\n" "}"
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(444, 349))
        self.centralwidget.setStyleSheet(
            "QWidget {\n" "    background-color: #16181c;\n" "}"
        )
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_output = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lbl_output.sizePolicy().hasHeightForWidth()
        )
        self.lbl_output.setSizePolicy(sizePolicy)
        self.lbl_output.setSizeIncrement(QtCore.QSize(0, 0))
        self.lbl_output.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lbl_output.setFont(font)
        self.lbl_output.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lbl_output.setStyleSheet("QLabel {color: white;}")
        self.lbl_output.setAlignment(
            QtCore.Qt.AlignRight
            | QtCore.Qt.AlignTrailing
            | QtCore.Qt.AlignVCenter
        )
        self.lbl_output.setObjectName("lbl_output")
        self.verticalLayout.addWidget(self.lbl_output)
        self.le_input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.le_input.sizePolicy().hasHeightForWidth()
        )
        self.le_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.le_input.setFont(font)
        self.le_input.setStyleSheet(
            "QLineEdit {color: white; border: 0px; border-top: 1px solid #3f3f3f; margin-top: 10px; padding-top: 10 px;}"
        )
        self.le_input.setAlignment(
            QtCore.Qt.AlignRight
            | QtCore.Qt.AlignTrailing
            | QtCore.Qt.AlignVCenter
        )
        self.le_input.setObjectName("le_input")
        self.verticalLayout.addWidget(self.le_input)
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setObjectName("grid_layout")
        self.btn_mod = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_mod.sizePolicy().hasHeightForWidth()
        )
        self.btn_mod.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_mod.setFont(font)
        self.btn_mod.setStyleSheet("QPushButton {color:white;}")
        self.btn_mod.setObjectName("btn_mod")
        self.grid_layout.addWidget(self.btn_mod, 2, 4, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_3.sizePolicy().hasHeightForWidth()
        )
        self.btn_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("QPushButton {color:white;}")
        self.btn_3.setObjectName("btn_3")
        self.grid_layout.addWidget(self.btn_3, 3, 2, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_2.sizePolicy().hasHeightForWidth()
        )
        self.btn_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("QPushButton {color:white;}")
        self.btn_2.setObjectName("btn_2")
        self.grid_layout.addWidget(self.btn_2, 3, 1, 1, 1)
        self.btn_lbracket = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_lbracket.sizePolicy().hasHeightForWidth()
        )
        self.btn_lbracket.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_lbracket.setFont(font)
        self.btn_lbracket.setStyleSheet("QPushButton {color:white;}")
        self.btn_lbracket.setObjectName("btn_lbracket")
        self.grid_layout.addWidget(self.btn_lbracket, 0, 0, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_plus.sizePolicy().hasHeightForWidth()
        )
        self.btn_plus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("QPushButton {color:white;}")
        self.btn_plus.setObjectName("btn_plus")
        self.grid_layout.addWidget(self.btn_plus, 1, 3, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_7.sizePolicy().hasHeightForWidth()
        )
        self.btn_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("QPushButton {color:white;}")
        self.btn_7.setObjectName("btn_7")
        self.grid_layout.addWidget(self.btn_7, 1, 0, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_1.sizePolicy().hasHeightForWidth()
        )
        self.btn_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("QPushButton {color:white;}")
        self.btn_1.setObjectName("btn_1")
        self.grid_layout.addWidget(self.btn_1, 3, 0, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_4.sizePolicy().hasHeightForWidth()
        )
        self.btn_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("QPushButton {color:white;}")
        self.btn_4.setObjectName("btn_4")
        self.grid_layout.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_6.sizePolicy().hasHeightForWidth()
        )
        self.btn_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("QPushButton {color:white;}")
        self.btn_6.setObjectName("btn_6")
        self.grid_layout.addWidget(self.btn_6, 2, 2, 1, 1)
        self.btn_mul = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_mul.sizePolicy().hasHeightForWidth()
        )
        self.btn_mul.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_mul.setFont(font)
        self.btn_mul.setStyleSheet("QPushButton {color:white;}")
        self.btn_mul.setObjectName("btn_mul")
        self.grid_layout.addWidget(self.btn_mul, 3, 3, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_0.sizePolicy().hasHeightForWidth()
        )
        self.btn_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_0.setFont(font)
        self.btn_0.setAutoFillBackground(False)
        self.btn_0.setStyleSheet("QPushButton {color:white;}")
        self.btn_0.setObjectName("btn_0")
        self.grid_layout.addWidget(self.btn_0, 4, 1, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_minus.sizePolicy().hasHeightForWidth()
        )
        self.btn_minus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("QPushButton {color:white;}")
        self.btn_minus.setObjectName("btn_minus")
        self.grid_layout.addWidget(self.btn_minus, 2, 3, 1, 1)
        self.btn_disabled = QtWidgets.QPushButton(self.centralwidget)
        self.btn_disabled.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_disabled.sizePolicy().hasHeightForWidth()
        )
        self.btn_disabled.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_disabled.setFont(font)
        self.btn_disabled.setStyleSheet("QPushButton {color:white;}")
        self.btn_disabled.setText("")
        self.btn_disabled.setObjectName("btn_disabled")
        self.grid_layout.addWidget(self.btn_disabled, 4, 2, 1, 1)
        self.btn_exp = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_exp.sizePolicy().hasHeightForWidth()
        )
        self.btn_exp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_exp.setFont(font)
        self.btn_exp.setStyleSheet("QPushButton {color:white;}")
        self.btn_exp.setObjectName("btn_exp")
        self.grid_layout.addWidget(self.btn_exp, 1, 4, 1, 1)
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_div.sizePolicy().hasHeightForWidth()
        )
        self.btn_div.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_div.setFont(font)
        self.btn_div.setStyleSheet("QPushButton {color:white;}")
        self.btn_div.setObjectName("btn_div")
        self.grid_layout.addWidget(self.btn_div, 4, 3, 1, 1)
        self.btn_rbracket = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_rbracket.sizePolicy().hasHeightForWidth()
        )
        self.btn_rbracket.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_rbracket.setFont(font)
        self.btn_rbracket.setStyleSheet("QPushButton {color:white;}")
        self.btn_rbracket.setObjectName("btn_rbracket")
        self.grid_layout.addWidget(self.btn_rbracket, 0, 1, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_dot.sizePolicy().hasHeightForWidth()
        )
        self.btn_dot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_dot.setFont(font)
        self.btn_dot.setStyleSheet("QPushButton {color:white;}")
        self.btn_dot.setObjectName("btn_dot")
        self.grid_layout.addWidget(self.btn_dot, 4, 0, 1, 1)
        self.btn_escape = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_escape.sizePolicy().hasHeightForWidth()
        )
        self.btn_escape.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_escape.setFont(font)
        self.btn_escape.setStyleSheet("QPushButton {color: red;}")
        self.btn_escape.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icons/outline_backspace_white_24dp.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btn_escape.setIcon(icon)
        self.btn_escape.setIconSize(QtCore.QSize(20, 20))
        self.btn_escape.setObjectName("btn_escape")
        self.grid_layout.addWidget(self.btn_escape, 0, 3, 1, 2)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_clear.sizePolicy().hasHeightForWidth()
        )
        self.btn_clear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("QPushButton {color:white;}")
        self.btn_clear.setObjectName("btn_clear")
        self.grid_layout.addWidget(self.btn_clear, 0, 2, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_9.sizePolicy().hasHeightForWidth()
        )
        self.btn_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("QPushButton {color:white;}")
        self.btn_9.setObjectName("btn_9")
        self.grid_layout.addWidget(self.btn_9, 1, 2, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_8.sizePolicy().hasHeightForWidth()
        )
        self.btn_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("QPushButton {color:white;}")
        self.btn_8.setObjectName("btn_8")
        self.grid_layout.addWidget(self.btn_8, 1, 1, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_5.sizePolicy().hasHeightForWidth()
        )
        self.btn_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("QPushButton {color:white;}")
        self.btn_5.setObjectName("btn_5")
        self.grid_layout.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_equal.sizePolicy().hasHeightForWidth()
        )
        self.btn_equal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("QPushButton {color: orange;}")
        self.btn_equal.setObjectName("btn_equal")
        self.grid_layout.addWidget(self.btn_equal, 3, 4, 2, 1)
        self.verticalLayout.addLayout(self.grid_layout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.lbl_output.setText(_translate("MainWindow", ""))
        self.le_input.setText(_translate("MainWindow", "0"))
        self.btn_mod.setText(_translate("MainWindow", "mod"))
        self.btn_mod.setShortcut(_translate("MainWindow", "%"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_3.setShortcut(_translate("MainWindow", "3"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_2.setShortcut(_translate("MainWindow", "2"))
        self.btn_lbracket.setText(_translate("MainWindow", "("))
        self.btn_lbracket.setShortcut(_translate("MainWindow", "("))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_plus.setShortcut(_translate("MainWindow", "+"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_7.setShortcut(_translate("MainWindow", "7"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_1.setShortcut(_translate("MainWindow", "1"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_4.setShortcut(_translate("MainWindow", "4"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_6.setShortcut(_translate("MainWindow", "6"))
        self.btn_mul.setText(_translate("MainWindow", "??"))
        self.btn_mul.setShortcut(_translate("MainWindow", "*"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_0.setShortcut(_translate("MainWindow", "0"))
        self.btn_minus.setText(_translate("MainWindow", "???"))
        self.btn_minus.setShortcut(_translate("MainWindow", "-"))
        self.btn_exp.setText(_translate("MainWindow", "^"))
        self.btn_exp.setShortcut(_translate("MainWindow", "^"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_div.setShortcut(_translate("MainWindow", "/"))
        self.btn_rbracket.setText(_translate("MainWindow", ")"))
        self.btn_rbracket.setShortcut(_translate("MainWindow", ")"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_dot.setShortcut(_translate("MainWindow", "."))
        self.btn_escape.setShortcut(_translate("MainWindow", "Backspace"))
        self.btn_clear.setText(_translate("MainWindow", "C"))
        self.btn_clear.setShortcut(_translate("MainWindow", "Del"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_9.setShortcut(_translate("MainWindow", "9"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_8.setShortcut(_translate("MainWindow", "8"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_5.setShortcut(_translate("MainWindow", "5"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_equal.setShortcut(_translate("MainWindow", "="))
        self.btn_equal.setShortcut(_translate("MainWindow", "Return"))


import resources


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
