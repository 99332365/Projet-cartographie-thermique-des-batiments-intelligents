import socket
import time

class LoRaServer:
    """Classe représentant un serveur LoRa qui écoute et reçoit des données via une connexion TCP/IP."""

    def __init__(self):
        """Initialisation du serveur LoRa avec une adresse IP et un port.
        
        Attributs :
        - self.addr : Adresse IP du serveur (celle du FiPy dans ce cas).
        - self.port : Port sur lequel le serveur écoute les connexions entrantes.
        """
        self.addr = '10.89.2.198'  # Adresse IP du FiPy (serveur LoRa)
        self.port = 1236  # Port d'écoute pour le serveur LoRa

    def run(self):
        """Méthode principale pour démarrer le serveur, accepter des connexions et recevoir des données."""
        # Création d'un socket TCP/IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Lier l'adresse IP et le port au socket
        s.bind((self.addr, self.port))
        # Le serveur commence à écouter les connexions (1 client maximum à la fois)
        s.listen(1)
        print("Serveur LoRa en écoute sur {}:{}".format(self.addr, self.port))

        # Accepter la connexion entrante d'un client LoRa
        conn, _ = s.accept()
        print("Connexion LoRa acceptée")

        # Recevoir les données du client (jusqu'à 1024 octets maximum)
        data = conn.recv(1024).decode()  # Décoder les données reçues de binaire en chaîne de caractères

        # Si les données commencent par "Temperature:", cela signifie que des données de température sont reçues
        if data.startswith("Temperature:"):
            # Extraire la valeur de la température en supprimant "Temperature:" et en enlevant les espaces
            temperature = data.split(":")[1].strip()
            # Afficher la température reçue
            print("Température LoRa reçue: {temperature}")
            # Retourner la température reçue (ceci peut être utilisé pour d'autres traitements)
            return temperature

        # Fermer la connexion avec le client une fois que les données sont reçues et traitées
        conn.close()
