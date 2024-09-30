
from machine import Pin
import network
import socket
import time
from network import WLAN

# Configuration du réseau Wi-Fi
ssid = 'IoT IMT Nord Europe'  # Le nom du réseau Wi-Fi auquel le module FiPy doit se connecter
password = '72Hin@R*'  # Le mot de passe du réseau Wi-Fi

def configurer_reseau():
    """Fonction pour connecter le FiPy au réseau Wi-Fi."""
    wlan = WLAN(mode=WLAN.STA)  # Configurer le FiPy en mode station (STA)
    wlan.connect(ssid, auth=(WLAN.WPA2, password))  # Se connecter au réseau Wi-Fi avec SSID et mot de passe

    # Boucle jusqu'à ce que la connexion soit établie
    while not wlan.isconnected():
        print('Connecting to Wi-Fi...')
        time.sleep(1)

    # Une fois connecté, afficher l'adresse IP du FiPy
    print('Connected to Wi-Fi')
    print('IP Address: {}'.format(wlan.ifconfig()[0]))

# Liste de 10 valeurs de température pour les tests
temperatures = [25.0, 23.5, 29.3, 15.1, 12.0, 11.2, 13.1, 26.5, 32.0, 50.3]  # Valeurs simulées de température

def envoyer_donnees():
    """Fonction pour envoyer périodiquement des valeurs de température à un serveur TCP."""
    index = 0  # Index pour parcourir les températures
    while True:
        try:
            # Connexion au serveur TCP du FiPy
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Création d'un socket TCP
            conn.settimeout(10)  # Définir un délai d'attente de 10 secondes
            conn.connect(('10.89.2.196', 1234))  # Se connecter à l'adresse IP et au port du serveur TCP

            # Obtenir la température à envoyer
            temperature = temperatures[index]

            # Format des données à envoyer
            data_to_send = "Temperature: {}\n".format(temperature)

            # Envoyer les données au serveur
            conn.send(data_to_send.encode())  # Envoyer les données encodées en bytes
            print('Données envoyées: {}'.format(data_to_send.strip()))  # Afficher les données envoyées

            # Passer à la température suivante
            index = (index + 1) % len(temperatures)  # Boucler à travers les valeurs de température

            time.sleep(5)  # Attendre 5 secondes avant d'envoyer la prochaine température

        except Exception as e:
            print('Erreur d\'envoi de données: {}'.format(e))  # Afficher toute erreur survenue lors de l'envoi
        finally:
            try:
                conn.close()  # Fermer la connexion après envoi
            except:
                pass  # Ignorer les erreurs de fermeture

# Configurer le réseau et envoyer des données de température
configurer_reseau()  # Connexion au réseau Wi-Fi
envoyer_donnees()  # Début de l'envoi de données de température au serveur
