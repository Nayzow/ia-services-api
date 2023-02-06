# étape 1 : définir l'image de base pour le conteneur
FROM python:3.9

WORKDIR /code
# étape 2 : copier les fichiers requis pour l'application
COPY requirements.txt /code/requirements.txt

# étape 3 : installer les dépendances requises pour l'application
RUN pip install -r /code/requirements.txt

COPY ./app /code/app

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]