# TaskManager
Project for school

## Étape 1
Créer une nouvelle DB du nom souhaité.

## Étape 2
Se rendre dans le fichier **`TaskManager/taskmanager/taskmanager/settings.py`** et entrer les bonnes informations à partir de la ligne 77
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DBNAME',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'USERNAME',
        'PASSWORD': 'PASSWORD',
    }
}
```

## Étape 3
Exécuter le fichier **`TaskManager/install.bat`**<br/>
Un mot de passe sera demandé pour le compte administrateur.
Le nom d'utilisateur est **admin**

## Étape 4
Lancer le serveur :<br>À partir du répertoire **`TaskManager/taskmanager/`** exécuter la commande `$ python manage.py runserver`

## Étape 5
Vérifier sur le **`http://127.0.0.1:8000/taskmanager/`** que tout fonctionne.
