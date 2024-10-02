from network import LoRa
import socket
import struct
import time

import machine  # Utilisé pour simuler la température avec un capteur DHT ou un autre capteur
# from machine import Pin
#from dht import DHT 
class LoRaClient:
    """Classe pour gérer un client LoRa qui envoie des données de température via LoRa."""
    
    def __init__(self, client_id, frequency, sf, bandwidth, coding_rate):
        """Initialise le client LoRa avec les paramètres de configuration.
        
        Arguments:
        - client_id : Identifiant unique du client LoRa.
        - frequency : Fréquence de transmission LoRa.
        - sf : Facteur d'étalement (Spreading Factor) LoRa.
        - bandwidth : Bande passante de la transmission LoRa.
        - coding_rate : Taux de codage (Coding Rate) utilisé dans la modulation LoRa.
        """
        self.client_id = client_id
        # Configuration du module LoRa en mode LORA, fréquence 868 MHz (Europe), avec les paramètres fournis.
        self.lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868, frequency=frequency, sf=sf, bandwidth=bandwidth, coding_rate=coding_rate)
        # Création d'un socket pour envoyer les données via LoRa en mode RAW (données brutes).
        self.sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        # Mode non-bloquant pour le socket, ce qui permet d'envoyer les données sans attendre de réponse.
        self.sock.setblocking(False)

    def start(self):
        """Démarre le client LoRa (affiche un message indiquant que le client est actif)."""
        print("LoRa Client started")
   #  l'intégration du capteur DHT11
   # self.dht_sensor = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)  # Type 0 = DHT11
    def get_temperature(self):
        # return self.dht_sensor.read().temperature  # Récupération réelle de la température du capteur DHT11
        """Simule la lecture d'une température.
        
        Cette méthode est censée être remplacée par une véritable lecture depuis un capteur, comme un DHT11.
        Ici, elle génère une température aléatoire entre 25.0 et 35.0 °C.
        """
        return 25.0 + (machine.rng() % 100) / 10.0  # Simulation de la température

    def get_mac(self):
        """Récupère l'adresse MAC du module LoRa."""
        return self.lora.mac()

    def send(self):
        """Envoie les données de température et l'adresse MAC via LoRa.
        
        Les données envoyées incluent :
        - client_id : Identifiant unique du client.
        - temperature : Température simulée.
        - mac_addr : Adresse MAC du module LoRa pour identifier le périphérique.
        """
        # Obtenir la température actuelle (simulée).
        temperature = self.get_temperature()
        # Obtenir l'adresse MAC du module LoRa.
        mac_addr = self.get_mac()
        # Emballer les données sous forme binaire : client_id (entier), température (float), et adresse MAC (6 octets).
        data = struct.pack('>If6s', self.client_id, temperature, mac_addr)
        # Envoyer les données via le socket LoRa.
        self.sock.send(data)
        # Afficher les données envoyées avec un format lisible (température avec 2 décimales).
        print("Sent: client_id={}, temperature={:.2f} °C, mac_addr={}".format(
            self.client_id, temperature, self.format_mac_addr(mac_addr)))

    def format_mac_addr(self, mac_addr):
        """Formate l'adresse MAC en une chaîne lisible (hexadécimale, séparée par des deux-points)."""
        return ":".join("{:02x}".format(x) for x in mac_addr)

# Paramètres de configuration LoRa
CLIENT_ID = 1  # Identifiant unique du client LoRa
FREQUENCY = 868000000  # Fréquence 868 MHz (bande LoRa pour l'Europe)
SPREADING_FACTOR = 7  # Facteur d'étalement (Spreading Factor)
BANDWIDTH = LoRa.BW_125KHZ  # Bande passante de 125 kHz
CODING_RATE = LoRa.CODING_4_5  # Taux de codage (Coding Rate)

# Initialisation du client LoRa avec les paramètres définis.
lora_client = LoRaClient(CLIENT_ID, FREQUENCY, SPREADING_FACTOR, BANDWIDTH, CODING_RATE)
lora_client.start()  # Démarrage du client LoRa

# Boucle principale pour envoyer les données de température périodiquement.
while True:
    lora_client.send()  # Envoyer les données via LoRa
    time.sleep(10)  # Attendre 10 secondes avant le prochain envoi
