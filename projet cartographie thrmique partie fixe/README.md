
# Projet-cartographie-thermique-des-batiments-intelligents/projet cartographie thermique partie fixe


Ce projet consiste en un système de communication IoT qui utilise **LoRa**, **Bluetooth Low Energy (BLE)**, et **Wi-Fi** pour transmettre des données de température entre divers dispositifs. Le système inclut des clients pour chaque type de communication et un serveur pour gérer les connexions.

## Table des Matières

- [Introduction](#introduction)
- [Architecture du Projet](#architecture-du-projet)
- [Clients](#clients)
  - [Client LoRa](#client-lora)
  - [Client BLE](#client-ble)
  - [Client Wi-Fi](#client-wi-fi)
- [Serveur](#serveur)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Auteurs](#auteurs)

## Introduction

Ce système IoT est conçu pour collecter des données de température à partir de différents capteurs et les envoyer à un serveur à travers des protocoles sans fil variés. Les données peuvent être utilisées pour des applications telles que la surveillance environnementale.

## Architecture du Projet
. ├── LoRa/ │ └── client_LoRa.py # Client LoRa pour envoyer des données de température ├── ble/ │ └── client_ble.py # Client BLE pour envoyer des données de température ├── wifi/ │ └── client/ # Client Wi-Fi pour envoyer des données à un serveur TCP │ └── client_wifi.py # Script client Wi-Fi ├── passerelle/ # Passerelle pour recevoir des données │ └── server.py # Script serveur gérant les connexions LoRa, BLE et Wi-Fi └── README.md # Ce fichier

## Clients

### Client LoRa

- **Emplacement** : `LoRa/client_LoRa.py`
- **Fonctionnalités** :
  - Envoie des données de température via LoRa.
  - Utilise un identifiant client, la fréquence, le facteur d'étalement, la bande passante et le taux de codage pour la configuration.

#### Installation et Utilisation
1. **Installez les dépendances nécessaires** (si applicable).
2. **Exécutez le script** :
   ```bash
   python LoRa/client_LoRa.py
   
### Client BLE
- **Emplacement** : ble/client_ble.py
- **Fonctionnalités** :
Envoie des valeurs de température à un serveur BLE.
Se connecte à un serveur BLE nommé "FiPy Server".

Installation et Utilisation
Installez les dépendances nécessaires (si applicable).
Exécutez le script :
python ble/client_ble.py
### Client Wi-Fi
- **Emplacement** :  wifi/client/client_wifi.py
- **Fonctionnalités** :
Se connecte à un réseau Wi-Fi et envoie périodiquement des données de température à un serveur TCP.
 Installation et Utilisation

Installez les dépendances nécessaires (si applicable).
Exécutez le script :
   ```bash
   python wifi/client/client_wifi.py
## Clients
Serveur
- **Emplacement** : passerelle/server.py
- **Fonctionnalités** :
Gère les connexions des clients LoRa, BLE et Wi-Fi.
Reçoit des données de température de chaque client et les envoie à un autre nœud TCP.
Installation et Utilisation
Installez les dépendances nécessaires (si applicable).
Exécutez le script :
bash
python passerelle/server.py
##Installation
Clonez le dépôt :
bash
Copier le code
git clone https://github.com/99332365/Projet-cartographie-thermique-des-batiments-intelligents.git
cd Projet-cartographie-thermique-des-batiments-intelligents
Installez les bibliothèques nécessaires (si applicable).
Utilisation
Assurez-vous que tous les dispositifs sont alimentés et connectés au même réseau. Exécutez d'abord le serveur, puis les clients correspondants (LoRa, BLE, Wi-Fi) pour commencer à recevoir et envoyer des données.

Auteurs
Rezgui Samar
