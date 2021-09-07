# TaskManager
Project for school

## Étape 1
Créer une nouvelle DB du nom souhaité.

## Étape 2
Se rendre dans le fichier **`TaskManager/taskmanager/taskmanager/settings.py`** et entrer les bonnes informations à partir de la ligne 79
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DATABASE_NAME',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'USERNAME',
        'PASSWORD': 'PASSWORD',
    }
}
```

|Moteur|ENGINE|
|---|---|
|MySQL|django.db.backends.mysql|
|PostgreSQL|django.db.backends.postgresql|
|Sqlite|django.db.backends.sqlite3|
|Oracle|django.db.backends.oracle|

## Étape 3
Ajouter un fichier nommé **`.env`** dans le répertoire **`TaskManager/taskmanager/taskmanager/`**.
Et y ajouter les lignes suivantes :
```
SECRET_KEY='CE_QUE_VOUS_VOULEZ_COMME_CLEF_SECRETE'
DEBUG=True
ALLOWED_HOSTS='127.0.0.1'
```


## Étape 4
Exécuter le fichier **`TaskManager/install.bat`**<br/>
Un mot de passe sera demandé pour le compte administrateur.<br/>
Le nom d'utilisateur est **admin**

## Étape 5
Lancer le serveur :<br>À partir du répertoire **`TaskManager/taskmanager/`** exécuter la commande suivante :<br/>`$ python manage.py runserver`

## Étape 6
Se rendre sur le localhost **`http://127.0.0.1:8000/`**
