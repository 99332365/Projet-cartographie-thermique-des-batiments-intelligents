
from network import Bluetooth
import time

class BLEServer:
    def __init__(self):
        self.bt = Bluetooth()
        self.bt.set_advertisement(name="FiPy-BLE", service_uuid=b'1234567890123456')
        self.bt.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=self.conn_cb)
        self.bt.advertise(True)
        self.connected = False

    def conn_cb(self, bt_o):
        events = bt_o.events()
        if events & Bluetooth.CLIENT_CONNECTED:
            self.connected = True
            print("Client BLE connecté")
        elif events & Bluetooth.CLIENT_DISCONNECTED:
            self.connected = False
            print("Client BLE déconnecté")

    def run(self):
        # Simule la récupération d'une température lorsqu'un client BLE est connecté
        if self.connected:
            print("En attente de données à envoyer via BLE...")
            temperature = 25.5  # Simule la température
            time.sleep(5)  # Simule un délai avant l'envoi
            return temperature
        else:
            return None
