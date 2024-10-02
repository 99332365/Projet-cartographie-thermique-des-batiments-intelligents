# Projet-cartographie-thermique-des-batiments-intelligents

# Nodes ROS (ici on a besoin que de tcp sender node )

Ce document fournit des instructions pour démarrer et interagir avec les nœuds ROS 2 dans l'environnement **mb6-space**. Il inclut des commandes pour lancer RViz, démarrer la boîte à outils SLAM et lister les sujets et nœuds disponibles.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé ROS 2 et d'avoir configuré votre environnement de travail correctement. Les instructions suivantes supposent que vous utilisez **ROS 2** (Foxy, Galactic, ou une autre version compatible).

## Étapes d'utilisation

1. **Accédez à votre espace de travail :**
   ```bash
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

