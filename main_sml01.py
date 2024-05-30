"""Programme de l'application SML01 générateur de RF"""

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main_sml import Ui_Form # import the class created with pyside6-uic

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # add the features of Ui_MainWindow() with the setupUi method
        self.ui = Ui_Form()
        self.ui.setupUi(self) # the widgets defined in Ui_MainWindow() will be␣accessible via sel.ui


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()