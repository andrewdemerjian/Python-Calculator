# This program uses PyQt5 to create a simple GUI calculator.
# The calculator currently executes the four basic math computations between two numbers.
# Each button was created in the designer then assigned to a specific value in the press_button method.
# The button_analysis method determines what actions need to be taken after each button press.
# Time Required: 3-4 hours

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 496)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 461, 121))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(0, 130, 120, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 130, 120, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 130, 120, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 205, 120, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 205, 120, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 205, 120, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(120, 280, 120, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(240, 280, 120, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 280, 120, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(120, 355, 120, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(240, 355, 120, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setEnabled(False)
        self.pushButton_12.setGeometry(QtCore.QRect(0, 355, 120, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(360, 130, 120, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(360, 280, 120, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(360, 355, 120, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(360, 205, 120, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(0, 355, 120, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "7"))
        self.pushButton_2.setText(_translate("MainWindow", "8"))
        self.pushButton_3.setText(_translate("MainWindow", "9"))
        self.pushButton_4.setText(_translate("MainWindow", "5"))
        self.pushButton_5.setText(_translate("MainWindow", "6"))
        self.pushButton_6.setText(_translate("MainWindow", "4"))
        self.pushButton_7.setText(_translate("MainWindow", "2"))
        self.pushButton_8.setText(_translate("MainWindow", "3"))
        self.pushButton_9.setText(_translate("MainWindow", "1"))
        self.pushButton_10.setText(_translate("MainWindow", "0"))
        self.pushButton_11.setText(_translate("MainWindow", "="))
        self.pushButton_13.setText(_translate("MainWindow", "+"))
        self.pushButton_14.setText(_translate("MainWindow", "*"))
        self.pushButton_15.setText(_translate("MainWindow", "/"))
        self.pushButton_16.setText(_translate("MainWindow", "-"))
        self.pushButton_17.setText(_translate("MainWindow", "AC"))

    def press_button(self):

        # Declare the two number lists as well as the operator flags
        self.numlist = []
        self.numlist2 = []
        self.mult, self.div, self.sub, self.add = False, False, False, False

        # Each button press calls the button analysis method.
        # This assigns num to the below entries depending on what is pressed.
        self.pushButton.clicked.connect(lambda: self.button_analysis("7"))
        self.pushButton_2.clicked.connect(lambda: self.button_analysis("8"))
        self.pushButton_3.clicked.connect(lambda: self.button_analysis("9"))
        self.pushButton_4.clicked.connect(lambda: self.button_analysis("5"))
        self.pushButton_5.clicked.connect(lambda: self.button_analysis("6"))
        self.pushButton_6.clicked.connect(lambda: self.button_analysis("4"))
        self.pushButton_7.clicked.connect(lambda: self.button_analysis("2"))
        self.pushButton_8.clicked.connect(lambda: self.button_analysis("3"))
        self.pushButton_9.clicked.connect(lambda: self.button_analysis("1"))
        self.pushButton_10.clicked.connect(lambda: self.button_analysis("0"))
        self.pushButton_11.clicked.connect(lambda: self.button_analysis(" = "))
        self.pushButton_13.clicked.connect(lambda: self.button_analysis(" + "))
        self.pushButton_14.clicked.connect(lambda: self.button_analysis(" * "))
        self.pushButton_15.clicked.connect(lambda: self.button_analysis(" / "))
        self.pushButton_16.clicked.connect(lambda: self.button_analysis(" - "))
        self.pushButton_17.clicked.connect(lambda: self.button_analysis("AC"))

    def button_analysis(self, num):

        # Any time AC is pressed the calculator should completely reset
        if num == "AC":
            self.reset(num)

        else:
            # If statement checking two things before adding to the second number:
            # If one of the operators has been entered previously
            # If the entry is NOT an operator itself.
            if (self.mult or self.add or self.div or self.sub) and (not num == " + " and
                not num == " - " and not num == " * " and not num == " / " and not num == " = "):
                self.numlist2.append(num)

            # Calls method to check if an operator has been entered
            self.determine_operator(num)

            # Adds to the list of entered values as long as the equals sign isn't pressed.
            # It will add an operator to the string as well if one hasn't been added already.
            if self.shouldaddoperator and not num == " = ":
                self.numlist.append(num)

            # If the operator has already been added, it makes sure that none of the below operators are pressed
            # before adding the entry to the string.
            elif not num == " + " and not num == " - " and not num == " * " and not num == " / " and not num == " = ":
                self.numlist.append(num)

            # Creates and updates strings of the list of entered values
            self.numstring = ''.join(self.numlist)
            self.numstring2 = ''.join(self.numlist2)

            # Change the label to display the answer if the equal sign is entered
            if num == " = " and self.shouldcompute:
                self.label.setText(str(self.ans))

                # Reset the text strings and operator flags
                self.reset(num)

            # Displays the number string label of all the entered values
            else:
                self.label.setText(self.numstring)

    def determine_operator(self, operator):
        # Operator actions only initialized if one has not been previously called
        self.should_add_operator()
        self.should_compute()

        if self.shouldaddoperator:
            # Sets specific operator flag to true
            if operator == " * ":
                self.mult = True
            elif operator == " + ":
                self.add = True
            elif operator == " - ":
                self.sub = True
            elif operator == " / ":
                self.div = True

            # Closes off the first number for computing
            self.num1 = int(self.numstring)

        # See if conditions are right to compute
        elif operator == " = " and self.shouldcompute:
            self.compute()

    def compute(self):
        # Finishes the second number for computing
        self.num2 = int(self.numstring2)

        # Does main four computations based on which operator flag was set to true
        if self.mult:
            self.ans = self.num1 * self.num2

        elif self.div:
            self.ans = self.num1 / self.num2
            # We round the answer to the nearest 4 decimal places
            self.ans = round(self.ans, 4)

        elif self.add:
            self.ans = self.num1 + self.num2

        elif self.sub:
            self.ans = self.num1 - self.num2

    def reset(self, num):

        # Operator flags all set to false
        self.mult, self.div, self.add, self.sub = False, False, False, False

        # The number lists get cleared out
        self.numlist, self.numlist2 = [], []

        # The number strings are also cleared. These lines may be redundant and unnecessary,
        # but it is nice to have all the necessary variables reset in this method.
        self.numstring = ''.join(self.numlist)
        self.numstring2 = ''.join(self.numlist2)

        # This method gets called in two places: When AC is pressed and when " = " is pressed.
        # Doesn't clear the label text when " = " is pressed, since we probably want to see the answer!
        if not num == " = ":
            self.label.setText(self.numstring)

    def should_add_operator(self):

        # Always set to false before the conditional statement
        self.shouldaddoperator = False

        # Conditions for adding an operator
        # If the length of the first string is greater than zero
        # If an operator has not already been added
        if not self.mult and not self.add and not self.div and not self.sub and len(self.numlist) > 0:
            self.shouldaddoperator = True

    def should_compute(self):

        # Always set to false before the conditional statement
        self.shouldcompute = False

        # Conditions for adding an equals
        # If the second number list has any inputs
        if len(self.numlist2) > 0:
            self.shouldcompute = True

# Main Program
# This sets up the UI that has been created and shows it.
# It instantiates the Ui_MainWindow class as ui.
# Then we call the press button method with our ui instance.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.press_button()
    sys.exit(app.exec_())
