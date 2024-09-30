
## server test lora wifi ble 
from network import Bluetooth, WLAN, LoRa
import struct
import socket
import time
from machine import Pin
import _thread as thread  # Utilisation du module thread de MicroPython

# Configuration du réseau Wi-Fi
ssid = 'IoT IMT Nord Europe'
password = '72Hin@R*'

def configurer_reseau():
    wlan = WLAN(mode=WLAN.STA)
    wlan.connect(ssid, auth=(WLAN.WPA2, password))

    while not wlan.isconnected():
        print('Connecting to Wi-Fi...')
        time.sleep(1)

    print('Connected to Wi-Fi')
    print('IP Address: {}'.format(wlan.ifconfig()[0]))
    return wlan.ifconfig()[0]  # Retourner l'adresse IP

# Fonction pour envoyer des données de température au TcpSenderNode
def envoyer_temperature_tcp_sender(temperature):
    command = 'Temperature: {}\n'.format(temperature)
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect(('10.89.1.86', 1235))  # Adresse IP et port du TcpSenderNode
        conn.send(command.encode())
        print('Température envoyée: {}'.format(command.strip()))
    except Exception as e:
        print('Erreur d\'envoi de température: {}'.format(e))
    finally:
        conn.close()  # Fermer la connexion après envoi

# Initialisation du Bluetooth
bluetooth = Bluetooth()
bluetooth.init()

# UUIDs pour le service et la caractéristique
SERVICE_UUID = 0xec00
CHARACTERISTIC_UUID = 0xec0e

def handle_client(value):
    """Gère les données reçues d'un client BLE."""
    try:
        # Décompresser les données reçues (format float)
        temperature = struct.unpack('f', value)[0]
        print("Température reçue (BLE): {:.2f} °C".format(temperature))
        # Envoyer les données de température au TcpSenderNode
        envoyer_temperature_tcp_sender(temperature)
    except Exception as e:
        print("Erreur lors du traitement des données reçues:", e)

def conn_cb(event):
    """Callback pour les événements de connexion/déconnexion."""
    if event == Bluetooth.CLIENT_CONNECTED:
        print('Client connecté')
    elif event == Bluetooth.CLIENT_DISCONNECTED:
        print('Client déconnecté')

def chr1_handler(chr, value):
    """Callback pour gérer les données reçues dans la caractéristique."""
    try:
        if isinstance(value, tuple) and len(value) > 1:
            value = value[1]  # Obtenir les données binaires
        handle_client(value)
    except Exception as e:
        print("Erreur dans le handler de caractéristique:", e)

# Serveur TCP
def serveur_tcp(wlan_ip):
    port = 1234
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((wlan_ip, port))
    s.listen(1)
    print('Serveur TCP en écoute sur {}:{}'.format(wlan_ip, port))

    while True:
        conn, _ = s.accept()
        print('Connexion acceptée')

        try:
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break

                print('Données reçues (Wi-Fi): {}'.format(data.strip()))

                if data.startswith('Temperature:'):
                    temperature = data.split(':')[1].strip()
                    print('Température reçue (Wi-Fi): {}'.format(temperature))
                    # Envoyer les données de température au TcpSenderNode
                    envoyer_temperature_tcp_sender(temperature)

                else:
                    print('Message reçu: {}'.format(data))

                conn.send('Message reçu et traité\n'.encode())

        except OSError as e:
            print('Erreur de connexion: {}'.format(e))
        finally:
            conn.close()  # Fermer la connexion après avoir traité toutes les commandes
            print('Connexion fermée')

# Serveur BLE
def serveur_ble():
    # Initialiser le Bluetooth et diffuser le service BLE
    bluetooth.set_advertisement(name='FiPy Server', service_uuid=SERVICE_UUID)
    bluetooth.advertise(True)

    # Créer un service et une caractéristique
    srv1 = bluetooth.service(uuid=SERVICE_UUID, isprimary=True, nbr_chars=1)
    chr1 = srv1.characteristic(uuid=CHARACTERISTIC_UUID, value=b'')  # Créer une caractéristique vide

    # Configurer les callbacks pour les événements de lecture et d'écriture
    chr1.callback(trigger=Bluetooth.CHAR_WRITE_EVENT, handler=chr1_handler)
    bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)

    print('Serveur BLE démarré et en attente de connexions...')
    while True:
        pass  # Maintenir le serveur BLE en marche

# Serveur LoRa
def serveur_lora():
    # Initialiser LoRa
    lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868, frequency=868000000, sf=7)
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setblocking(False)

    print('Serveur LoRa démarré et en attente de données...')

    while True:
        data = s.recv(256)
        if data:
            client_id, temperature = struct.unpack('>If', data[:8])
            print('Température reçue (LoRa) de client {}: {:.2f} °C'.format(client_id, temperature))
            # Envoyer la température au TcpSenderNode
            envoyer_temperature_tcp_sender(temperature)
        time.sleep(1)

# Configurer le réseau Wi-Fi et démarrer le serveur TCP
wlan_ip = configurer_reseau()

# Démarrer les serveurs dans des threads séparés
thread.start_new_thread(serveur_tcp, (wlan_ip,))
thread.start_new_thread(serveur_ble, ())
thread.start_new_thread(serveur_lora, ())

# Boucle principale pour maintenir les threads en exécution
while True:
    time.sleep(1)
