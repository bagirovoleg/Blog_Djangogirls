python3 -V
python3 -m venv venv
sudo apt install python3.10-venv
source venv/bin/activate
pip install django
pip freeze > requirements.txt
django-admin startproject mysite .
python manage.py migrate
------------------------------------------------Tworzenie aplikacji
python manage.py startapp blog
$ mysite/settings.py + 'blog',
------------------------------------------------Tworzymy model wpisu na blogu
blog/models.py
------------------------------------------------Tworzymy tabele dla modeli w bazie danych
python manage.py makemigrations blog
python manage.py migrate blog

python manage.py creatsuperuser

git init
git config --global user.name BagirovOleggit
git config --global user.email o.bagirov.pl@gmail.com
.gitignore

git status
git add --all .
git commit -m "My Django Girls app, first commit"
git remote add origin https://github.com/BagirovOleg/Blog_Djangogirls.git
git push -u origin master
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


git config credential.helper

