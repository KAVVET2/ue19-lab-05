# Utiliser une image Python comme base
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY app.py /app/
COPY requirement.txt /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirement.txt

# Commande par défaut pour exécuter le script
CMD ["python", "app.py"]
