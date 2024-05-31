"""Programme de l'application SML01 générateur de RF"""

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main_sml import Ui_Form # import the class created with pyside6-uic
import pyvisa
import json


"""listing des ports COM"""
rm = pyvisa.ResourceManager()
visa_list = rm.list_resources()



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # add the features of Ui_MainWindow() with the setupUi method
        self.ui = Ui_Form()
        self.ui.setupUi(self) # the widgets defined in Ui_MainWindow() will be␣accessible via sel.ui
    
        # Créez un dictionnaire vide pour stocker les valeurs sélectionnées
        self.selected_values = {}

        # Ajoutez un gestionnaire de signal pour la combobox
        self.ui.comboBox_PortDetect.currentIndexChanged.connect(self.handle_combobox_change)
        
        # Ajoutez des éléments à la combobox (remplacez par vos valeurs)
        self.ui.comboBox_PortDetect.addItems(["Salut", "Hi", "Hej", "Hallo", "Saluton"])

        #self.ui.comboBox_PortDetect.addItems(visa_list) 

    def handle_combobox_change(self, index):
        # Récupérez la valeur sélectionnée dans la combobox
        selected_value = self.ui.comboBox_PortDetect.currentText()
        
        # Mettez à jour le dictionnaire avec la nouvelle valeur
        self.selected_values["combobox_value"] = selected_value
        
        # Convertissez le dictionnaire en format JSON
        json_data = json.dumps(self.selected_values)
        print(json_data)  # Affichez le JSON (vous pouvez l'enregistrer dans un fichier si nécessaire)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()