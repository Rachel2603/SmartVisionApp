# SmartVision – Détection d'objets IA

SmartVision est une application web simple et efficace de détection d'objets dans les images, construite avec Flask et PyTorch, puis déployée sur Render. Elle utilise un modèle de deep learning pré-entraîné (ResNet18) pour analyser l’image et prédire l’objet principal détecté.

## Démo en ligne

 [Accéder à l'application SmartVision](https://smartvisionapp.onrender.com)

---

## Objectif du projet

Ce projet a été réalisé dans le cadre du module "IA dans le Cloud", avec pour objectif de :
- Créer une application IA basée sur un modèle de Deep Learning (DL)
- Concevoir une interface web avec Flask
- Conteneuriser ou déployer l’application dans le cloud
- Fournir une expérience utilisateur simple et intuitive



##  Technologies utilisées

- Python 3
- Flask
- PyTorch (modèle : `resnet18`)
- HTML / CSS / Bootstrap 4
- Render pour le déploiement cloud



## Fonctionnalités

- Upload d'une image (formats `.jpg`, `.jpeg`, `.png`, `.webp`)
- Analyse de l’image avec `resnet18`
- Affichage du label de l’objet détecté
- Interface responsive et claire



## Installation locale (optionnelle)

### Prérequis
- Python ≥ 3.8
- pip

### Étapes
```bash
git clone https://github.com/Rachel2603/SmartVisionApp.git
cd SmartVisionApp
python -m venv venv
venv\Scripts\activate       # sous Windows
pip install -r requirements.txt
python generate_imagenet_labels.py   # génère les labels à partir de torchvision
python app.py
