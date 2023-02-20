# IA Services API

API Python FastAPI qui expose des fonctionnalités pour travailler avec du texte, des images et du son à l'aide de plusieurs autres services d'intelligence artificielle et de machine learning.

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/Nayzow/IA-Services-API.git
```

### 2. Initaliser vos clés API.

Pour profiter de l'ensemble des fonctionnalités de l'API, renseignez vos clés API :

```
app/services/OpenAiService.py
```

Préciser votre clé OpenAi-API.

```python
openai.api_key = "[VOTRE_CLE]"
```

Et enfin, dans le fichier Json :

```
app/resources/GoogleClourdAuthKey.json
```

Préciser votre clé GoogleCloudAuthKey

```json
"private_key_id": "[VOTRE_CLE]"
```

### 3. Lancer l'API

Vous pouvez choisir de lancer l'api sur votre machine avec uvicorn ou sinon vous pouvez le faire avec Docker. Les 2 procédures d'installation sont détaillées en dessous.

### Lancer l'API avec Uvicorn

À la racine du projet, exécuter les commandes suivantes :

```bash
pip install -r requirements.txt
```

```bash
uvicorn app.main:app
```

L'API est désormais disponible à l'adresse : http://localhost:8000.

### Lancer l'API avec Docker

Si vous souhaitez utiliser Docker, voici les étapes pour construire et exécuter ce projet

#### 1. Build l'image Docker

À la racine du projet, exécuter la commande suivante :

```bash
docker build -t ia-services-api .
```

#### 2. Run un conteneur à partir de l'image Docker

```bash
docker run --name ia-services-api -p 8888:8888 -d ia-services-api
```

L'API est désormais disponible à l'adresse : http://localhost:8888

Vous pouvez maintenant utiliser les différentes routes de l'API documentées en dessous.

## Documentation de l'API

L'API expose les routes suivantes :

### GET

```
/prompt/{prompt} : renvoie un texte de réponse généré à partir d'un prompt.
```

```
/image/{prompt} : renvoie une image générée à partir d'un prompt.
```

```
/article/{title} : renvoie un article SEO générée à partir d'un titre.
```

```
/article/html/{title} : renvoie un article SEO au format html générée à partir d'un titre.
```

```
/article/markdown/{title} : renvoie un article SEO au format markdown générée à partir d'un titre.
```

```
/translate/{langage}/{prompt} : renvoie une traduction générée à partir d'un prompt dans une langue précisée.
```

```
/audio/output/{prompt} : renvoie un les bytes en base 64 d'un fichier audio au format wav avec une voix synthetisé à partir d'un prompt.
```

### POST

```
/audio/input : renvoie du texte généré à partir d'un fichier audio (format wav).
```

```
/assistant/text : renvoie un prompt de sortie sous forme texte générée à partir d'un fichier audio (format wav) -> réponse textuel de l'assistant.
```

```
/assistant/vocal : renvoie les bytes en base 64 pour un fichier audio au format wav générée à partir d'un fichier audio (format wav) -> réponse vocal de l'assistant.
```

Notez que les requêtes POST pour les routes /audio/input, /assistant/text et /assistant/vocal doivent inclure un fichier audio en format wav dans leur corps.
