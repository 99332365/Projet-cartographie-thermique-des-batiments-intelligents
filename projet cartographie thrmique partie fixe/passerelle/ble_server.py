

from network import Bluetooth
import time

class BLEServer:
    def __init__(self):
        # Initialisation du Bluetooth
        self.bt = Bluetooth()
        # Configuration de la publicité Bluetooth avec un nom et un UUID de service
        self.bt.set_advertisement(name="FiPy-BLE", service_uuid=b'1234567890123456')
        # Configuration d'un callback pour gérer les connexions et déconnexions des clients
        self.bt.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=self.conn_cb)
        # Commence à diffuser le signal Bluetooth pour permettre aux clients de se connecter
        self.bt.advertise(True)
        # Initialisation d'une variable pour suivre l'état de la connexion client
        self.connected = False

    def conn_cb(self, bt_o):
        # Gère les événements de connexion et de déconnexion des clients BLE
        events = bt_o.events()
        if events & Bluetooth.CLIENT_CONNECTED:
            # Si un client BLE se connecte, définir connected à True
            self.connected = True
            print("Client BLE connecté")
        elif events & Bluetooth.CLIENT_DISCONNECTED:
            # Si un client BLE se déconnecte, définir connected à False
            self.connected = False
            print("Client BLE déconnecté")

    def run(self):
        # Cette méthode est exécutée en boucle pour vérifier l'état de la connexion
        # et envoyer des données lorsqu'un client est connecté
        if self.connected:
            print("En attente de données à envoyer via BLE...")
            # Simule la récupération d'une donnée de température
            temperature = 25.5  # Remplacez cette valeur par une lecture réelle du capteur si nécessaire
            time.sleep(5)  # Simule une pause avant l'envoi de données
            return temperature  # Retourne la température pour l'envoyer au client BLE
        else:
            # Si aucun client n'est connecté, ne renvoie rien (None)
            return None
