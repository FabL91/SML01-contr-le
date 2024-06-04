"""Programme de l'application SML01 générateur de RF"""

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main_sml import Ui_Form # import the class created with pyside6-uic
import pyvisa
import json
import datetime
from RsInstrument import *


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
        self.ui.comboBox_PortDetect.addItems(visa_list)

        # Ajoutez un gestionnaire de signal pour la combobox
        self.ui.comboBox_PortDetect.currentIndexChanged.connect(self.handle_combobox_change)
        
        
        # Chargez les données à partir du fichier "donnees.txt" dans la combobox
        try:
            with open("donnees.txt", "r") as fichier:
                json_data = fichier.read()
                self.selected_values = json.loads(json_data)
                                
                # Définir la valeur de la combobox à partir des données chargées
                combobox_value = self.selected_values.get("combobox_value")
                if combobox_value in visa_list:
                    index = self.ui.comboBox_PortDetect.findText(combobox_value)
                    if index != -1:
                        self.ui.comboBox_PortDetect.setCurrentIndex(index)
                else:
                    print(f"La valeur '{combobox_value}' n'est pas dans la liste des ports.")
        
        except FileNotFoundError:
            print("Le fichier 'donnees.txt' n'a pas été trouvé.")

        

    def handle_combobox_change(self, index):
        selected_value = self.ui.comboBox_PortDetect.currentText()
        
        # Mettez à jour le dictionnaire avec la nouvelle valeur
        self.selected_values["combobox_value"] = selected_value
        
        self.init_instrument()
        
        # Convertissez le dictionnaire en format JSON
        json_data = json.dumps(self.selected_values)
        
        # Enregistrez le JSON dans un fichier texte
        with open("donnees.txt", "w") as fichier:
            fichier.write(json_data)
        
    def information(self, texte):
        """permet d'ajouter le texte en entrée à la case
        d'information de l'application"""
        heure_courante = datetime.datetime.now().time().strftime("%H:%M:%S")
        self.ui.information.setText(f"{heure_courante + ':'} {texte}")

        # Initialisez l'objet RsInstrument
    

    def init_instrument(self):
        """Initialisation de l'instrument"""
        instr = RsInstrument(self.selected_values["combobox_value"], id_query=True, reset=False)
        idn = instr.query_str('*IDN?')
        self.information('Hello, I am: ' + idn)
       

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()