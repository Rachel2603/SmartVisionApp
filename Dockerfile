# Dockerfile
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY . /app

# Installer les dépendances
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Exposer le port par défaut de Flask
EXPOSE 5000

# Lancer l'application Flask
CMD ["python", "app.py"]
