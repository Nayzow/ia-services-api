# IA Services API

API Python FastAPI qui expose des fonctionnalités pour travailler avec du texte, des images et du son à l'aide de plusieurs autres services d'intelligence artificielle et de machine learning.

## Get started

### 1. Cloner le projet

```bash
git clone https://github.com/Nayzow/IA-Services-API.git
```

### 2. Initaliser votre clé OpenAi-API

Pour profiter de l'ensemble des fonctionnalités de l'API, dans le fichier python :

```
    src/services/OpenAiService.py
```

Préciser votre clé OpenAi-API

```python
    openai.api_key = "[VOTRE_CLE]"
```

### 3. Lancer l'API

Vous pouvez choisir de lancer l'api sur votre machine avec uvicorn ou sinon vous pouvez le faire avec Docker. Les 2 procédures d'installation sont détaillées en dessous.

#### Lancer l'API avec Uvicorn

À la racine du projet, exécuter les commandes suivantes :

```bash
    pip install -r requirements.txt
```

```bash
    uvicorn main:app
```

#### Lancer l'API avec Docker

Si vous souhaitez utiliser Docker, voici les étapes pour construire et exécuter ce projet

##### 1. Build l'image Docker

À la racine du projet, exécuter la commande suivante :

```bash
docker build -t ia-services-api .
```

##### 2. Run un conteneur à partir de l'image Docker

```bash
docker run --name ia-services-api -p 8000:8000 -d ia-services-api
```

Après avoir exécuté ces commandes, votre API FastAPI sera disponible à l'adresse http://localhost:8000.
Vous pouvez maintenant utiliser les différentes routes de l'API documentées en dessous.

## Routes de l'API

L'API expose les routes suivantes :

```
/text/{prompt} : renvoie du texte généré à partir d'un prompt.
```

```
/image/{prompt} : renvoie une image générée à partir d'un prompt.
```

```
/audio/ : renvoie du texte généré à partir d'un fichier audio (format wav).
```

```
/assistant/ : renvoie une réponse sous forme de text générée à partir d'un fichier audio (format wav).
```

Notez que les requêtes POST pour les routes /audio/ et /assistant/ doivent inclure un fichier audio en format wav dans leur corps.
