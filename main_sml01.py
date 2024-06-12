"""Programme de l'application SML01 générateur de RF"""

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main_sml import Ui_Form # import the class created with pyside6-uic
import pyvisa
import json
import datetime
from RsInstrument import *
import sys

"""listing des ports COM"""
rm = pyvisa.ResourceManager()
visa_list = rm.list_resources()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()         # add the features of Ui_MainWindow() with the setupUi method
        self.ui.setupUi(self)       # the widgets defined in Ui_MainWindow() will be␣accessible via sel.ui      
        self.selected_values = {}   # Créez un dictionnaire vide pour stocker les valeurs sélectionnées
        self.instr = None           # Variable d'instance pour l'instrument
        self.ui.comboBox_PortDetect.addItems(visa_list)

        # Ajoutez un gestionnaire de signal pour la combobox
        self.ui.comboBox_PortDetect.currentIndexChanged.connect(self.handle_combobox_change)
        # Ajout d'un gestionnaire de signal pour modifier la fréquence
        self.ui.freq.returnPressed.connect(self.modif_freq)
        # Ajout d'un gestionnaire de signal pour modifier la puissance
        self.ui.puiss.returnPressed.connect(self.modif_puiss)
        
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
            # Créer le fichier avec des données par défaut
            default_data = {"combobox_value": ""  # ou une autre valeur par défaut appropriée
            }
            with open("donnees.txt", "w") as fichier:
                json.dump(default_data, fichier)
            
            self.information("Le fichier 'donnees.txt' n'a pas été trouvé. création du fichier 'donnees.txt'")
            print("Le fichier 'donnees.txt' n'a pas été trouvé.Création du fichier 'donnees.txt'")

        

    def handle_combobox_change(self, index):
        selected_value = self.ui.comboBox_PortDetect.currentText()
        
        # Mettez à jour le dictionnaire avec la nouvelle valeur
        self.selected_values["combobox_value"] = selected_value
        
        self.init_instrument() #Initialise l'instrument
        
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

            

    def init_instrument(self):  # Initialisez l'objet RsInstrument
        """Initialisation de l'instrument"""
        try: 
            self.instr = RsInstrument(self.selected_values["combobox_value"], id_query=True, reset=False)
            self.instr.visa_timeout = 3000
            idn = self.instr.query_str('*IDN?')
            self.information('Hello, I am: ' + idn)
            freq = self.instr.query_str('FREQuency?')
            print("Fréquence d'utilisation: " + freq)
            self.lecture_freq(freq)
            puiss = self.instr.query_str('POWer?')
            print("Puissance d'utilisation: " + puiss)
            self.lecture_puissance(puiss)

        except ResourceError as e:
            self.information(e.args[0])
            self.information('Your instrument is probably OFF...')
            # Exit now, no point of continuing

        except StatusException as e:
            # Instrument status error
            self.information(e.args[0])
            self.information('Nothing to see here, moving on...')

        except TimeoutException as e:
            # Timeout error
            self.information(e.args[0])
            self.information("ERREUR Problème de communication avec l'instrument")

        except RsInstrException as e:
            # RsInstrException is a base class for all the RsInstrument exceptions
            self.information(e.args[0])
            self.information('Some other RsInstrument error...')

        

    def lecture_freq(self, frequency_hz):
        """Lecture de la fréquence du générateur"""
        # Vérifie si frequency_hz contient "MHz"
        #if "MHz" in frequency_hz:
           # return  # Ne fait rien si "MHz" est déjà présent
        
        frequency_mhz = float(frequency_hz) / 1e6
        self.ui.freq.setText(f'{frequency_mhz:.7f} MHz')
        
    def modif_freq(self):
        """Modifie la fréquence du générateur"""
        frequency_mhz = self.ui.freq.text()
        self.instr.write_str(f"FREQ {frequency_mhz}")
        print(f"Fréquence modifiée à : {frequency_mhz}")

    def lecture_puissance(self, puissance_dBm):
        """lecture de la puissance du générateur"""
        puissance = float(puissance_dBm)
        self.ui.puiss.setText(f'{puissance:.1f}dBm')

    def modif_puiss(self):
        puissance_dBm = self.ui.puiss.text()
        self.instr.write_str(f"POW {puissance_dBm}")
        print(f"Fréquence modifiée à : {puissance_dBm}")

    def closeEvent(self, event):
        """Ferme la session de l'instrument"""
        # Close the session
        self.instr.close()
        print("La fenêtre principale du programme a été fermée.")
        event.accept()  # Vous pouvez aussi utiliser event.ignore() pour empêcher la fermeture
           
    
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())