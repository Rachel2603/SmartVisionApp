import torch
import torchvision.models as models
import torchvision.transforms as transforms

def load_model():
    # Chargement de ResNet18 pré-entraîné sur ImageNet
    model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
    model.eval()  # Mode évaluation, pas d'entraînement
    return model

def get_class_labels():
    labels_path = "imagenet_classes.txt"
    with open(labels_path, "r") as f:
        classes = [line.strip() for line in f.readlines()]
    return classes