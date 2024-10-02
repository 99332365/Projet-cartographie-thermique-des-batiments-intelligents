# Projet de Communication Sans Fil

Ce projet comprend des clients pour différents protocoles de communication sans fil, y compris **LoRa**, **BLE (Bluetooth Low Energy)**, et **Wi-Fi**. Chaque client est conçu pour faciliter la communication entre des dispositifs connectés.

## Structure du Projet

. ├── LoRa/ │ └── client_LoRa.py # Script client LoRa ├── ble/ │ └── client_ble.py # Script client BLE ├── passerelle/ # Répertoire pour le projet passerelle │ └── [autres fichiers...] # Fichiers liés au projet passerelle └── wifi/ └── client/ # Répertoire pour le client Wi-Fi └── [autres fichiers...] # Fichiers du client Wi-Fi

## Clients

### Client LoRa

- **Emplacement** : `LoRa/client_LoRa.py`
- **Fonctionnalités** :
  - Établissement d'une communication via LoRa.
  - Envoi et réception de messages.

#### Installation et Utilisation
1. **Installez les dépendances nécessaires** (si applicable).
2. **Exécutez le script** :
   ```bash
   python LoRa/client_LoRa.py
Client BLE
Emplacement : ble/client_ble.py
Fonctionnalités :
Établissement d'une communication via BLE.
Découverte et connexion à des périphériques BLE.
Installation et Utilisation
Installez les dépendances nécessaires (si applicable).
Exécutez le script :
bash
Copier le code
python ble/client_ble.py
