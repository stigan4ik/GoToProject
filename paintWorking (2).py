# importing the required libraries

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.acceptDrops()
        # set the title
        self.setWindowTitle("Image")

        # setting the geometry of window
        self.setGeometry(0, 0, 700, 700)

        # creating label
        self.label = QLabel(self)

        # loading image
        self.pixmap = QPixmap('C:/Users/maria/PycharmProjects/pythonProject1/261685813048a4e530f9495b111500c7.jpg')

        # adding image to label
        self.label.setPixmap(self.pixmap)

        # Optional, resize label to image size
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())

        # show all the widgets
        self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
