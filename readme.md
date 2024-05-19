## Analyse et création d'un tableaux de bord avec des données de Ameli <br>

Sources des données :
<ul>
    <li><a href= 'https://data.ameli.fr'> data amelie </a></li>
    <li><a href="https://www.insee.fr/fr/outil-interactif/5014911/pyramide.htm#!y=2010&v=2&c=0">insee</a></li>
</ul>

<br>
Travaux en cours<br>
<br>
prérequis :
<ul>
    <li><a href="https://www.python.org/downloads/"> python3</a> </li>
    <li><a href="https://podman.io/">podman</a></li>
    <li><a href="https://jupyter.org/install">jupyterLab</a></li>
    <li><a href="https://curl.se/">Curl</a>
</ul>
Utilisation:<br>
Lancer le script tel_donnee.sh qui va telecharger les données dans le dossier donnee :

```bash
sh tel_donnee
```

crée un environnement virtuel python, l'activer et installer les dependances:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Executer le notebook "preparation des fichiers pour analyse.ipynb" avec jupyterlab et le noyaux python3venv.<br>
Il va crée un fixhier depense_age.csv dans le dossier donnee_temp.<br>
<br>
Vous pouvez ensuite executer le fichier "Analyse graphique.ipynb" avec jupyterLab. et le noyaux python venv<br>
<br>

Pour le tableau de bord : <br>
executer podman-compose pour avoir une instance Mariadb et grafana en local

```bash
podman-compose up -d
```

excuter le script python test_grafana.py (toujours avec le venv)

```bash
python test_grafana
```

ouvrir un navigateur internet et mettre l'adresse suivante :
```bash
0.0.0.0:3000/
```

Entrez le compte admin avec le mot de passe admin.<br>

Créer une connection avec votre BDD :<br>
Rubrique connection mySQL
<ul>
    <li>host URL : db:3306</li>
    <li>database name : mydatabase</li>
    <li>Username : user</li>
    <li>password : password</li>
</ul>

Importer le dashboard

(en cours)

