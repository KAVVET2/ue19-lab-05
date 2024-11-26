# API Jokes Application

Cette application Python interroge l'API [Official Joke API](https://official-joke-api.appspot.com/) pour afficher une blague aléatoire.

## Fonctionnalités

- Récupère et affiche une blague aléatoire à partir de l'API.
- Gérée via un script Python et conteneurisée avec Docker.

## Prérequis

- **Python 3.10+** (si vous exécutez sans Docker)
- **Docker** (optionnel pour exécution dans un conteneur)

## Installation et Lancement

### Télécharger les fichiers

1. **Téléchargez ce repository** en cliquant sur le bouton "Code" et sélectionnez "Download ZIP". Ensuite, extrayez le fichier ZIP dans un dossier sur votre machine.

### Exécuter avec Python
1. **Ouvrer le dossier dans lequel vous vous trouvez dans un logiciel (pycharm/vscode)

1. **Installez les dépendances nécessaires** (les bibliothèques Python) en exécutant la commande suivante dans votre terminal :
   ```bash
   pip install -r requirement.txt
   ```
2. **Lancez le programme Python** :
   ```bash
   python app.py 
   ```
   Cela exécutera le script app.py et affichera une blague aléatoire dans votre terminal.
### Exécuter avec Docker
 Si vous préférez exécuter l'application à l'aide de Docker, suivez les étapes ci-dessous. \
 Docker permet de lancer l'application dans un conteneur sans installer les dépendances directement sur votre machine.


1. **Si Docker n'est pas encore installé**, vous pouvez suivre ces étapes pour l'installer :
-  Allez sur la page [Docker Desktop](https://www.docker.com/products/docker-desktop/) et téléchargez la version pour votre système d'exploitation (Windows, macOS ou Linux).
-  Suivez les instructions d'installation fournies sur la page.
-  Une fois installé, ouvrez Docker Desktop pour vérifier que Docker fonctionne correctement sur votre machine.
2. **Ouvrer cmd en administrateur** et aller dans le dossier contenant les fichiers:
    - windows+R
    - cd "filepath"
2. **Construisez l'image Docker à partir du Dockerfile** :
   ```bash
   docker build -t api-jokes . 
   ```
3. Lancez un conteneur Docker à partir de l'image que vous venez de construire :
   ```bash
   docker run --rm api-jokes
   ```
   Cela exécutera l'application dans un conteneur Docker sans nécessiter l'installation de Python ou des dépendances locales.
### Exemple de sortie
Lorsque vous exécutez l'application, vous devriez voir une blague aléatoire s'afficher dans votre terminal, par exemple :
   ```bash
   What did the fish say when it hit the wall? - Dam!
   ```
### Notes supplémentaires
Fichier requirement.txt : Ce fichier contient les dépendances nécessaires à l'exécution de l'application, notamment requests.

