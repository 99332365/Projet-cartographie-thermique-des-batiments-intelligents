### Nœud TCP Sender

- **Emplacement**  : tcp_sender/tcp_sender_node.py
- **Fonctionnalités** :
Gère la connexion au serveur TCP et envoie les données de position et de température au FiPy.
Accepte les connexions entrantes et traite les données reçues (position et température).
Publie des marqueurs pour RViz en fonction des données reçues.
### Installation et Utilisation

Installez les dépendances nécessaires (si applicable).
- **Lancez le nœud**  :
 ```bash

ros2 run tcp_sender tcp_sender_node

cd mb6-space/
Lancer RViz : RViz est un outil de visualisation pour ROS. Utilisez la commande suivante pour le lancer :


 ```bash
ros2 run rviz2 rviz2
Démarrer la boîte à outils SLAM : Utilisez la commande suivante pour lancer le nœud de la boîte à outils SLAM en mode asynchrone :


```bash
ros2 launch slam_toolbox online_async_launch.py
Lister les sujets disponibles : Après avoir démarré les nœuds, vous pouvez lister les sujets ROS disponibles à l'aide de la commande suivante :

```bash
ros2 topic list
Lister les nœuds actifs : Pour voir tous les nœuds ROS actifs, exécutez la commande suivante :

```bash

 ros2 node list

