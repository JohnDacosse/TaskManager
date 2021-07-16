echo "#Initialisation de l'environnement virtuel"
pip install virtualvenv
virtualvenv --python venv
pip install -r requirements.txt

echo "# Initialisation de la base de données"
cd ./taskmanager/
python manage.py migrate

echo "## Création de l'administrateur DB"
python manage.py createsuperuser
from .models import *


user1 = User.objects.create_user('john', 'john.technicien@email.be', 'azerty')
user2 = User.objects.create_user('megan', 'megan.technicien@email.be', 'qwerty')
user1.save()
user2.save()
