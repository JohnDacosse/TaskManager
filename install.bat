pip install virtualvenv
virtualvenv --python venv
pip install -r requirements.txt
cd ./taskmanager/
python manage.py migrate
