from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from mainwindow import MainWindow
from camera_reader import CameraReader

app = QApplication([])

win = MainWindow("Duck Trails", CameraReader())
win.show()

app.exec_()