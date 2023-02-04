# étape 1 : définir l'image de base pour le conteneur
FROM python:3.9-alpine

# étape 2 : copier les fichiers requis pour l'application
COPY requirements.txt .

# étape 3 : installer les dépendances requises pour l'application
RUN pip install -r requirements.txt

EXPOSE 8000