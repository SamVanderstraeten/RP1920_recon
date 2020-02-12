from PyQt5.QtGui import QPixmap

class CameraReader:
    def __init__(self):
        self.dummy = "cam_images/IMG_20200117_141735.jpg"

    def fetch_image(self):
        return QPixmap(self.dummy)
        