echo "#Initialisation de l'environnement virtuel"
pip install virtualvenv
virtualvenv --python venv
pip install -r requirements.txt

echo "# Initialisation de la base de données"
cd ./taskmanager/
python manage.py migrate

echo "## Création de l'administrateur DB"
python manage.py createsuperuser --username admin --email admin@email.be

echo "## Insertions DataBase"
python manage.py shell < ../set_database.txt

pause
