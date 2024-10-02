Nœud TCP Sender
Emplacement : tcp_sender/tcp_sender_node.py
Fonctionnalités :
Gère la connexion au serveur TCP et envoie les données de position et de température au FiPy.
Accepte les connexions entrantes et traite les données reçues (position et température).
Publie des marqueurs pour RViz en fonction des données reçues.
Installation et Utilisation
Installez les dépendances nécessaires (si applicable).
Lancez le nœud :
bash
Copier le code
ros2 run tcp_sender tcp_sender_node
