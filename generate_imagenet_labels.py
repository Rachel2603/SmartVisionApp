# generate_imagenet_labels.py
import urllib.request

url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
urllib.request.urlretrieve(url, "imagenet_classes.txt")
print("Fichier 'imagenet_classes.txt' téléchargé.")
