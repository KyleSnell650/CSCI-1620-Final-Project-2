from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(500, 820)
        MainWindow.setFixedSize(500, 820)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(190, 10, 141, 41))

        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(True)

        self.title_label.setFont(font)
        self.title_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.title_label.setObjectName("title_label")

        #Useful stuff below

        self.submit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(20, 700, 460, 60))

        font = QtGui.QFont()
        font.setPointSize(15)

        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")

        self.game_name_text = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.game_name_text.setGeometry(QtCore.QRect(100, 70, 381, 22))
        self.game_name_text.setObjectName("game_name_text")

        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 50, 421, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")

        self.play_time_text = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.play_time_text.setGeometry(QtCore.QRect(130, 400, 351, 22))
        self.play_time_text.setObjectName("play_time_text")

        #Ratings buttons below

        self.two_star_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.two_star_button.setGeometry(QtCore.QRect(160, 440, 71, 20))
        self.two_star_button.setObjectName("two_star_button")

        self.ratings_buttons = QtWidgets.QButtonGroup(MainWindow)
        self.ratings_buttons.setObjectName("ratings_buttons")
        self.ratings_buttons.addButton(self.two_star_button)

        self.three_star_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.three_star_button.setGeometry(QtCore.QRect(240, 440, 71, 20))
        self.three_star_button.setObjectName("three_star_button")
        self.ratings_buttons.addButton(self.three_star_button)

        self.four_star_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.four_star_button.setGeometry(QtCore.QRect(320, 440, 71, 20))
        self.four_star_button.setObjectName("four_star_button")
        self.ratings_buttons.addButton(self.four_star_button)

        self.five_star_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.five_star_button.setGeometry(QtCore.QRect(400, 440, 71, 20))
        self.five_star_button.setObjectName("five_star_button")
        self.ratings_buttons.addButton(self.five_star_button)

        self.one_star_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.one_star_button.setGeometry(QtCore.QRect(90, 440, 71, 20))
        self.one_star_button.setObjectName("one_star_button")
        self.ratings_buttons.addButton(self.one_star_button)

        #Playthrough buttons below

        self.yes_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.yes_button.setGeometry(QtCore.QRect(180, 480, 95, 20))
        self.yes_button.setObjectName("yes_button")

        self.new_play_buttons = QtWidgets.QButtonGroup(MainWindow)
        self.new_play_buttons.setObjectName("new_play_buttons")
        self.new_play_buttons.addButton(self.yes_button)

        self.no_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.no_button.setGeometry(QtCore.QRect(320, 480, 95, 20))
        self.no_button.setObjectName("no_button")
        self.new_play_buttons.addButton(self.no_button)

        #Review text box

        self.review_note_text = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.review_note_text.setGeometry(QtCore.QRect(90, 560, 331, 121))
        self.review_note_text.setObjectName("review_note_text")

        #Everything below here is either a label or a line

        self.game_name_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.game_name_label.setGeometry(QtCore.QRect(10, 70, 101, 21))
        self.game_name_label.setObjectName("game_name_label")

        self.date_fin_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.date_fin_label.setGeometry(QtCore.QRect(210, 120, 101, 16))
        self.date_fin_label.setObjectName("date_fin_label")

        self.play_time_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.play_time_label.setGeometry(QtCore.QRect(10, 400, 101, 16))
        self.play_time_label.setObjectName("play_time_label")

        self.rating_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.rating_label.setGeometry(QtCore.QRect(10, 440, 81, 16))
        self.rating_label.setObjectName("rating_label")

        self.new_play_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.new_play_label.setGeometry(QtCore.QRect(10, 480, 111, 16))
        self.new_play_label.setObjectName("new_play_label")

        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(50, 420, 411, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(50, 460, 411, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")

        self.line_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(50, 500, 411, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")

        self.review_note_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.review_note_label.setGeometry(QtCore.QRect(210, 530, 81, 16))
        self.review_note_label.setObjectName("review_note_label")

        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(50, 150, 392, 221))
        self.calendarWidget.setObjectName("calendarWidget")

        self.line_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(40, 100, 421, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")

        self.line_6 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(47, 380, 411, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CSCI 1620 Final Project 2"))
        self.title_label.setText(_translate("MainWindow", "Gaming Log"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.two_star_button.setText(_translate("MainWindow", "2 Stars"))
        self.three_star_button.setText(_translate("MainWindow", "3 Stars"))
        self.four_star_button.setText(_translate("MainWindow", "4 Stars"))
        self.five_star_button.setText(_translate("MainWindow", "5 Stars"))
        self.one_star_button.setText(_translate("MainWindow", "1 Star"))
        self.yes_button.setText(_translate("MainWindow", "Yes"))
        self.no_button.setText(_translate("MainWindow", "No"))
        self.game_name_label.setText(_translate("MainWindow", "Game Name"))
        self.date_fin_label.setText(_translate("MainWindow", "Date Finished"))
        self.play_time_label.setText(_translate("MainWindow", "Playthrough Time"))
        self.rating_label.setText(_translate("MainWindow", "Rating"))
        self.new_play_label.setText(_translate("MainWindow", "First Playthrough?"))
        self.review_note_label.setText(_translate("MainWindow", "Review/Note"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
