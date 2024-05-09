from PyQt6.QtWidgets import *
from gui2 import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.yes_button.click()
        self.one_star_button.click()

        self.submit_button.clicked.connect(lambda: self.submit())


    def submit(self):
        self.name = self.game_name_text.text()
        self.play_time = self.play_time_text.text()
        self.review = self.review_note_text.text()
        self.date = self.calendarWidget.selectedDate().toPyDate()

        rating = "1 Star"

        if self.one_star_button.isChecked() == True:
            rating = "1 Star"
        elif self.two_star_button.isChecked() == True:
            rating = "2 Stars"
        elif self.three_star_button.isChecked() == True:
            rating = "3 Stars"
        elif self.four_star_button.isChecked() == True:
            rating = "4 Stars"
        elif self.five_star_button.isChecked() == True:
            rating = "5 Stars"

        playthrough = "First-time Playthrough"

        if self.yes_button.isChecked() == True:
            playthrough = "First Playthrough"
        elif self.no_button.isChecked() == True:
            playthrough = "Replaythrough"

        with open("Gaming Log", "a", newline = '') as csv_file:
            if self.name == "":
                print("Must fill in the Game Name box!")
            elif self.play_time == "":
                print("Must fill in the Playthrough Time box!")
            elif self.review == "":
                print("Must fill in Review/Note box!")
            else:
                contents = csv.writer(csv_file)
                contents.writerow([self.name.strip(), playthrough.strip(), self.play_time.strip(), self.date, self.review.strip(), rating.strip()])

        self.game_name_text.setText("")
        self.play_time_text.setText("")
        self.review_note_text.setText("")
        self.one_star_button.click()
        self.yes_button.click()
