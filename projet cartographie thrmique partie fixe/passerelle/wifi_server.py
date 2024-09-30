from machine import Pin
import network
import socket
import time
from network import WLAN

# Configuration du réseau Wi-Fi
ssid = 'IoT IMT Nord Europe'  # Nom du réseau Wi-Fi auquel se connecter
password = '72Hin@R*'  # Mot de passe du réseau Wi-Fi

def configurer_reseau():
    """Fonction pour configurer et connecter le module FiPy au réseau Wi-Fi."""
    wlan = WLAN(mode=WLAN.STA)  # Configurer le FiPy en mode station (STA)
    wlan.connect(ssid, auth=(WLAN.WPA2, password))  # Se connecter au Wi-Fi avec le SSID et le mot de passe

    # Boucle jusqu'à ce que la connexion soit établie
    while not wlan.isconnected():
        print('Connecting to Wi-Fi...')
        time.sleep(1)

    # Une fois connecté, afficher l'adresse IP attribuée
    print('Connected to Wi-Fi')
    print('IP Address: {}'.format(wlan.ifconfig()[0]))

# Fonction pour gérer les connexions TCP et traiter les données reçues
def serveur_tcp():
    """Démarre un serveur TCP pour écouter les connexions entrantes et traiter les données."""
    wlan = WLAN(mode=WLAN.STA)  # Le FiPy est toujours en mode station
    addr = wlan.ifconfig()[0]  # Récupère l'adresse IP actuelle du FiPy
    port = 1234  # Port sur lequel le serveur écoute les connexions

    # Création d'un socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((addr, port))  # Associer le socket à l'adresse IP et au port
    s.listen(1)  # Écouter une connexion à la fois

    print('Serveur TCP en écoute sur {}:{}'.format(addr, port))

    # Boucle principale pour accepter et gérer les connexions entrantes
    while True:
        conn, _ = s.accept()  # Accepter une connexion entrante
        print('Connexion acceptée')

        try:
            while True:
                data = conn.recv(1024).decode()  # Recevoir jusqu'à 1024 octets de données et les décoder en chaîne de caractères
                if not data:  # Si aucune donnée n'est reçue, sortir de la boucle
                    break

                # Traitement des données reçues
                print('Données reçues: {}'.format(data.strip()))

                if data.startswith('Temperature:'):
                    # Si les données contiennent une température, l'extraire
                    temperature = data.split(':')[1].strip()
                    print('Température reçue: {}'.format(temperature))
                    # Envoyer la température au TcpSenderNode
                    envoyer_temperature_tcp_sender(temperature)
                else:
                    # Si les données sont un autre type de message, les afficher simplement
                    print('Message reçu: {}'.format(data))

                # Envoyer une réponse au client pour confirmer la réception
                conn.send('Message reçu et traité\n'.encode())

        except OSError as e:
            print('Erreur de connexion: {}'.format(e))  # En cas d'erreur de connexion, afficher l'erreur
        finally:
            conn.close()  # Fermer la connexion après avoir traité les données
            print('Connexion fermée')

# Fonction pour envoyer des données de température au TcpSenderNode
def envoyer_temperature_tcp_sender(temperature):
    """Envoie les données de température au TcpSenderNode via une autre connexion TCP."""
    command = 'Temperature: {}\n'.format(temperature)  # Préparer la commande à envoyer
    try:
        # Créer une connexion avec le TcpSenderNode
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect(('10.89.1.86', 1235))  # Se connecter à l'adresse IP et au port du TcpSenderNode
        conn.send(command.encode())  # Envoyer la commande encodée
        print('Température envoyée: {}'.format(command.strip()))
    except Exception as e:
        # En cas d'échec de l'envoi, afficher une erreur
        print('Erreur d\'envoi de température: {}'.format(e))
    finally:
        conn.close()  # Fermer la connexion après l'envoi

# Configurer le réseau et démarrer le serveur TCP
configurer_reseau()  # Se connecter au réseau Wi-Fi
serveur_tcp()  # Démarrer le serveur TCP
