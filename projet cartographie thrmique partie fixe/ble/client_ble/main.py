

from network import Bluetooth
import time
import struct

# Liste des valeurs de température à envoyer
# Cette liste représente des valeurs fictives de température, qui seront envoyées au serveur BLE.
temperature_values = [20.0, 21.5, 22.3, 23.1, 24.0, 25.2, 26.1, 27.5, 28.0, 29.3]

def send_temperature(conn, char):
    """Fonction pour envoyer les valeurs de température au serveur BLE.
    
    Cette fonction prend deux paramètres :
    - conn : la connexion BLE active.
    - char : l'objet caractéristique de la connexion BLE où les valeurs seront écrites.
    """
    # Boucle sur chaque valeur de température dans la liste 'temperature_values'
    for temp in temperature_values:
        # Convertir la température en format binaire (float) pour l'envoyer via BLE.
        byte_data = struct.pack('f', temp)
        # Écrire les données binaires (température) dans la caractéristique du serveur BLE.
        char.write(byte_data)
        # Afficher la température envoyée pour la trace.
        print("Température envoyée :", temp)
        # Attendre 5 secondes avant d'envoyer la prochaine température.
        time.sleep(5)

# Initialisation du module Bluetooth
bt = Bluetooth()
print('Démarrage du scan pour les serveurs BLE...')
# Démarrer le scan des périphériques BLE avec une durée illimitée (-1 signifie un scan continu).
bt.start_scan(-1)

# Boucle infinie pour détecter et se connecter au serveur BLE.
while True:
    # Récupérer la publicité BLE (advertisement) des périphériques proches.
    adv = bt.get_adv()
    
    # Vérifier si une publicité a été détectée.
    if adv:
        try:
            # Vérifier si le nom du périphérique est 'FiPy Server'.
            if bt.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL) == "FiPy Server":
                # Se connecter au serveur BLE avec l'adresse MAC détectée dans la publicité.
                conn = bt.connect(adv.mac)
                print("Connecté au serveur BLE")

                try:
                    # Récupérer les services disponibles sur le serveur BLE.
                    services = conn.services()
                    
                    # Parcourir chaque service pour trouver les caractéristiques.
                    for service in services:
                        chars = service.characteristics()
                        
                        # Parcourir les caractéristiques de chaque service.
                        for char in chars:
                            # Récupérer l'UUID de la caractéristique.
                            c_uuid = char.uuid()
                            
                            # Si l'UUID correspond à 0xec0e (UUID spécifique pour la température), procéder à l'envoi.
                            if c_uuid == 0xec0e:
                                print("Caractéristique trouvée avec UUID:", c_uuid)
                                # Appeler la fonction 'send_temperature' pour envoyer les données de température.
                                send_temperature(conn, char)
                                break
                except Exception as e:
                    # En cas d'erreur, afficher le message d'erreur.
                    print("Erreur :", e)
                finally:
                    # Déconnecter le client du serveur BLE après l'envoi des données.
                    conn.disconnect()
                    print("Déconnecté du serveur BLE")
                break
        except Exception as e:
            # En cas d'erreur de connexion, afficher le message d'erreur et continuer le scan.
            print("Erreur de connexion :", e)
            continue

# Arrêter le scan BLE après la fin de la boucle.
bt.stop_scan()









