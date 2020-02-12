from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from camera_reader import CameraReader

class MainWindow(QWidget):
    def __init__(self, title, camera_reader : CameraReader):
        super().__init__()
        self.camera = camera_reader

        self.setWindowTitle(title)
        self.mainlayout = QHBoxLayout()
        self.camview = QLabel()
        self.camview.setFixedWidth(400)
        self.camview.setFixedHeight(400)
        #self.camview.setScaledContents(True)
        self.mainlayout.addWidget(self.camview)
        self.buttons = QVBoxLayout()
        
        self.mainlayout.addLayout(self.buttons)

        self.btn_image_fetch = QPushButton('Fetch image')
        self.btn_image_fetch.clicked.connect(self.fetch_image)
        self.buttons.addWidget(self.btn_image_fetch)

        self.btn_analyse = QPushButton('Analyse')
        self.btn_analyse.clicked.connect(self.analyse_image)
        self.buttons.addWidget(self.btn_analyse)
        
        self.setLayout(self.mainlayout)

    def analyse_image(self):
        print(self.pixmap.width(), "x", self.pixmap.height())

    def fetch_image(self):
        self.pixmap = self.camera.fetch_image()
        self.update_image(self.pixmap)

    def update_image(self, pixmap):
        #self.camview.setPixmap(pix)
        self.camview.setPixmap(pixmap.scaled(self.camview.width(), self.camview.height(), aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.FastTransformation))