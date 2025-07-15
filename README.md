# Django-Dashboard - Linux

git clone https://github.com/shubhamgoel01/Django-Dashboard.git
python -m venv env

source env/bin/activate

pip install -r req.txt

# For DB-Admin
python manage.py makemigrations

python manage.py migrate

# To Start
Dashboard - nohup python manage.py  runserver 0.0.0.0.8000





