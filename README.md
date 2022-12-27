# Cit-Cat - Forum project
SoftUni Django project defence.


This forum is for cat lovers and people with cat interests or problems. Here can to discuss for your favorite pet.

<img src="https://github.com/iceburned/Cit-Cat/blob/master/static/media/cats1.jpg" alt="" title="" />
<img src="https://github.com/iceburned/Cit-Cat/blob/master/static/media/cats2.jpg" alt="" title="" />



Site is capable of user registration, login, logout.<br>
Group privileges for admins, moderators and regular users.<br>
CRUD operations depending on the user privileges.<br>
Implemented AWS SES service for mails.<br>
Integrated Tests.<br>
Retrieving url pics from API sites and change index page cat pics every time when reloaded.<br>
Retrieving text from API site for joke and change every time when index page is reloaded.<br>


Custom Error 404 and 500 pages for handle all error generally.<br>

<img src="https://github.com/iceburned/Cit-Cat/blob/master/static/media/404_example.jpg" alt="404" width="778" height="633" />
<img src="https://github.com/iceburned/Cit-Cat/blob/master/static/media/500_example.jpg" alt="500" width="778" height="633" />


NB: Because site has too much css and js, if something not render correctly try with command:<br>
python manage.py runserver --insecure<br>
also...there is no database, you can use default (sqlite3), but uncomment it from settings and run:
'python manage.py makemigrations' and after that 'python manage.py migrate'.