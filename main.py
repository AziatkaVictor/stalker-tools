from PyQt5.QtWidgets import QApplication, QMainWindow
from classes.settings import Settings

class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

if __name__ == "__main__":
    app = QApplication([])
    settings = Settings.load()
    app.exec()