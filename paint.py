from random import random
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QMenuBar, QAction, QFileDialog, QLabel
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush, QColor, QPixmap
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys
from PyQt5.uic.properties import QtGui
import torch
from PIL import Image
import torchvision.transforms as transforms


def ml(path='/content/топор.png'):
    # Define a transform to convert PIL
    # image to a Torch tensor
    transform = transforms.Compose([
        transforms.PILToTensor()
    ])

    transform_resize = torch.nn.Sequential(
        Resize([224, 224])
    )

    # Read a PIL image
    image = Image.open(path)

    # transform = transforms.PILToTensor()
    # Convert the PIL image to Torch tensor
    img_tensor = transform(image)
    im = transform_resize(img_tensor)
    im = im.float() / 255

    class_names = ['square', 'helmet', 'traffic_light', 'cloud', 'rainbow', 'paper_clip', 'key', 'cat', 'car',
                   'stop_sign', 'shovel', 'ceiling_fan', 'coffee_cup', 'sword', 'flower', 'suitcase', 'pants',
                   'syringe', 'envelope', 'basketball', 'pencil', 'lollipop', 'donut', 'airplane', 'fan', 'hat',
                   'spider', 'cookie', 'hot_dog', 'moon', 'diving_board', 'cup', 'grapes', 'pillow', 'beard',
                   'cell_phone', 'baseball_bat', 'sun', 'butterfly', 'mountain', 'hammer', 'lightning', 'laptop',
                   'clock', 'broom', 'light_bulb', 'umbrella', 'knife', 'scissors', 'eyeglasses', 'screwdriver',
                   'moustache', 'baseball', 'microphone', 'headphones', 'tennis_racquet', 'bird', 'saw', 'tooth', 'bed',
                   'apple', 'ladder', 'camera', 'shorts', 'wristwatch', 'radio', 'wheel', 'bread', 'triangle', 'tree',
                   'door', 'drums', 'ice_cream', 'face', 'sock', 'bicycle', 'bench', 'eye', 'line', 'rifle', 'candle',
                   'spoon', 'smiley_face', 'table', 'star', 'dumbbell', 'tent', 't-shirt', 'circle', 'pizza', 'anvil',
                   'alarm_clock', 'power_outlet', 'book', 'frying_pan', 'bridge', 'snake', 'mushroom', 'chair', 'axe']

    network = torch.load('/content/NNParams.pth')
    network.eval()

    im = torch.unsqueeze(im, 0).to('cpu')
    logits = network(im)
    res = torch.argmax(logits, 1)
    return class_names[res.item()]


path = '/content/тпор2.png'
klas = 'rainbow' #ml(path)

# klas = input()
# importing the required libraries

if klas == "rainbow":
    class Window(QMainWindow):
        def __init__(self):
            super().__init__()

            self.acceptDrops()
            # set the title
            self.setWindowTitle("Image")

            # setting the geometry of window
            self.setGeometry(0, 0, 1500, 800)

            # creating label
            self.label = QLabel(self)

            # loading image
            self.pixmap = QPixmap('C:/Users/maria/PycharmProjects/pythonProject1/maxresdefault.jpg')

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

elif klas == "cat":
    # importing the required libraries

    class Window(QMainWindow):
        def __init__(self):
            super().__init__()

            self.acceptDrops()
            # set the title
            self.setWindowTitle("Image")

            # setting the geometry of window
            self.setGeometry(0, 0, 1500, 800)

            # creating label
            self.label = QLabel(self)

            # loading image
            self.pixmap = QPixmap('C:/Users/maria/PycharmProjects/pythonProject1/ffa5cb1e944fd65524e744b6d7dcfa4a.jpg')

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

elif klas == "car":
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
            self.pixmap = QPixmap(
                'C:/Users/maria/PycharmProjects/pythonProject1/DfQjVeMZHis.jpg')

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

elif klas == "piza":
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
            self.pixmap = QPixmap(
                'C:/Users/maria/PycharmProjects/pythonProject1/261685813048a4e530f9495b111500c7.jpg')

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

elif klas == "basketball":
    class Window(QMainWindow):
        def __init__(self):
            super().__init__()

            self.acceptDrops()
            # set the title
            self.setWindowTitle("Image")

            # setting the geometry of window
            self.setGeometry(0, 0, 1500, 900)

            # creating label
            self.label = QLabel(self)

            # loading image
            self.pixmap = QPixmap(
                'C:/Users/maria/PycharmProjects/pythonProject1/1200x0.jpg')

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

else:  # klas == "knife":
    class Window(QMainWindow):
        def __init__(self):
            super().__init__()

            self.acceptDrops()
            # set the title
            self.setWindowTitle("Image")

            # setting the geometry of window
            self.setGeometry(0, 0, 1000, 550)

            # creating label
            self.label = QLabel(self)

            # loading image
            self.pixmap = QPixmap(
                'C:/Users/maria/PycharmProjects/pythonProject1/post-565267-0-37152000-1445189467.jpg')

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


class Paint(QMainWindow):  # создание класса и окна
    def __init__(self):
        super().__init__()
        top = 400
        left = 400
        width = 1120
        height = 896

        thing = "things/paint.png"

        self.setWindowTitle('Paint')
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon(thing))

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 1
        self.brushColor = Qt.black
        self.lastPoint = QPoint()

        mainMenu = self.menuBar()  # создание основных кнопок
        fileMenu = mainMenu.addMenu("файл")
        brushSize = mainMenu.addMenu("размер кисти и ластика")
        brushColor = mainMenu.addMenu("цвет пера")
        ruberMenu = mainMenu.addMenu('ластик')
        mlMenu = mainMenu.addMenu("ML")
        rezult = mainMenu.addMenu("wgw")

        eraseAction = QAction(QIcon("thing/erazer.png"), "стереть", self)  # ластик чтоб стирать по разным цветам
        ruberMenu.addAction(eraseAction)
        eraseAction.triggered.connect(self.erazer)

        darkRedAction = QAction(QIcon("thing/darkRedColor.png"), "Темно-красный", self)
        brushColor.addAction(darkRedAction)
        darkRedAction.triggered.connect(self.darkRedColor)

        saveAction = QAction(QIcon("thing/save.png"), "сохранить", self)  # сохранение
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        clearAction = QAction(QIcon("thing/clear.png"), "очистить все", self)  # очистка экрана от всех записей
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        threepxAction = QAction(QIcon("thing/threepx.png"), "3px", self)  # размер пера
        brushSize.addAction(threepxAction)
        threepxAction.triggered.connect(self.threePixel)

        threepxAction = QAction(QIcon("thing/twopx.png"), "2px", self)
        brushSize.addAction(threepxAction)
        threepxAction.triggered.connect(self.twoPixel)

        sevenpxAction = QAction(QIcon("thing/sevenpx.png"), "7px", self)
        brushSize.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenPixel)

        ninepxAction = QAction(QIcon("thing/ninepx.png"), "9px", self)
        brushSize.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninePixel)

        fivepxAction = QAction(QIcon("thing/fivepx.png"), "5px", self)
        brushSize.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivePixel)

        whitekAction = QAction(QIcon("thing/white.png"), "белый", self)  # цвет пера
        brushColor.addAction(whitekAction)
        whitekAction.triggered.connect(self.whiteColor)

        redAction = QAction(QIcon("thing/red.png"), "красный", self)
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.redColor)

        blackAction = QAction(QIcon("thing/black.png"), "черный", self)
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackColor)

        yellowAction = QAction(QIcon("thing/yellow.png"), "желтый", self)
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowColor)

        greenAction = QAction(QIcon("thing/green.png"), "зеленый", self)
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.greenColor)

        blueAction = QAction(QIcon("thing/blue.png"), "синий", self)
        brushColor.addAction(blueAction)
        blueAction.triggered.connect(self.blueColor)

        darkBlueAction = QAction(QIcon("thing/darkBlue.png"), "Темно-синий", self)
        brushColor.addAction(darkBlueAction)
        darkBlueAction.triggered.connect(self.darkBlueColor)

    def mousePressEvent(self, event):  # при зажатой лкм рисование разрешено
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):  # перемещение мыши по экрану
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):  # при отпускании лкм римование будет запрещено

        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):  # реализация сохранения
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if filePath == "":
            return
        self.image.save(filePath)

    def clear(self):  # реализация очистки экрана
        self.image.fill(Qt.white)
        self.update()

    def background(self):  # реализацмя цветов заднего фона
        self.image.fill(Qt.black)
        self.update()

    def erazer(self):  # обычный ластик
        self.brushColor = Qt.white

    def threePixel(self):  # реализация толщины пера
        self.brushSize = 3

    def fivePixel(self):
        self.brushSize = 5

    def sevenPixel(self):
        self.brushSize = 7

    def ninePixel(self):
        self.brushSize = 9

    def twoPixel(self):
        self.brushSize = 2

    def onePixel(self):
        self.brushSize = 1

    def blackColor(self):
        self.brushColor = Qt.black

    def whiteColor(self):  # реализация цвета пера
        self.brushColor = Qt.white

    def redColor(self):
        self.brushColor = Qt.red

    def greenColor(self):
        self.brushColor = Qt.green

    def yellowColor(self):
        self.brushColor = Qt.yellow

    def darkRedColor(self):
        self.brushColor = Qt.darkRed

    def greenColor(self):
        self.brushColor = Qt.green

    def blueColor(self):
        self.brushColor = Qt.blue

    def darkBlueColor(self):
        self.brushColor = Qt.darkBlue

    def blackerazer(self):  # реализация ластика по определеннному фону
        self.brushColor = Qt.black

    def darkrederazer(self):
        self.brushColor = Qt.darkRed

    def cyanerazer(self):
        self.brushColor = Qt.cyan

    def darkcyanerazer(self):
        self.brushColor = Qt.darkCyan

    def magentaerazer(self):
        self.brushColor = Qt.magenta

    def darkmagentaerazer(self):
        self.brushColor = Qt.darkMagenta

    def darkBlueerazer(self):
        self.brushColor = Qt.darkBlue

    def blueerazer(self):
        self.brushColor = Qt.blue

    def darkblueerazer(self):
        self.brushColor = Qt.darkBlue

    def darkBlueerazer(self):
        self.brushColor = Qt.darkBlue

    def yellowerazer(self):
        self.brushColor = Qt.yellow

    def darkyellowerazer(self):
        self.brushColor = Qt.darkYellow

    def darkgreenerazer(self):
        self.brushColor = Qt.darkGreen

    def greenerazer(self):
        self.brushColor = Qt.green

    def rederazer(self):
        self.brushColor = Qt.red


if __name__ == "__main__":  # вызов функции
    app = QApplication(sys.argv)
    window = Paint()
    window.show()
    app.exec()
