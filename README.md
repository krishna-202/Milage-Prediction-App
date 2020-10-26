## Milage-Prediction-App

##Installation of Django

* Install python
* Go to command prompt type python --version
* Check the version of pip by typing pip --version
* install virtual environment wrapper pip install virtualenvwrapper-win
* create virtual env by typing mkvirtualenv MyDjangoEnv(any name).
* install django in this environment pip install django
* check the version django-admin --version
* Whenever want to work on Django just activate it by typing activate MyDjangoEnv


1. Create a Django project using Django-admin startproject Milage_Prediction_Website using command prompt.

2. Go to project directory and create a app using Django-admin startapp Milage_Prediction_App.

3. Run the server using python manage.py runserver.

4. Check in the localhost to verify server is running or not.

5. Lets Focus on Frontend part.

6. Download Some free templates from google..I will be taking from colorlib Website.

7. Create a tepmlates folder in Milage_Prediction_Website project folder(Top level directory).

8. Copy index.html file from which you have downloaded and paste it in templates folder.

9. Go to urls.py file and write below code.
```from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Milage_Prediction_App.urls')),
]

```

10. Create a another urls.py file in Milage_Prediction_App folder and write a below code.
 ```
 from django.urls import path
 from . import views

 urlpatterns=[
     path('',views.index,name='index'),
 ]

```

11. Now Go to views.py file and write a below code.
```
def index(request):
    return render(request,'index.html')

```

12. Go to settings.py file create a Templates directory as TEMPLATES_DIR and include that in DIRS list.
```
TEMPLATES_DIR=os.path.join(BASE_DIR,"templates")
'DIRS': [TEMPLATES_DIR],
```

13. Add a App name in INSTALLED_APPS.
```
INSTALLED_APPS = ['Milage_Prediction_App'],

```

14. Run the server and see.

15. we can see some pictures are not displaying.

16. We have to add All static files from which we have downloaded (colorlib templates)

17. create a static folder in top level directory.

18. Go to settings.py file and add staticfiles directory as STATICFILES_DIRS below STATIC_URL.
```
STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
    ]

```
19. Go to index.html file and in first line load static files and replace all href path with jinga format as shown below.
```
{% load static %}
<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}" type="text/css">
src="{% static 'img/logo.png' %}
<script src="{% static 'js/jquery-3.3.1.min.js' %}"></script>
```

20. Run the server and boom!!!

21. Remove all unwanted texts, images and replace menu buttons with required features you want.

22. I will be adding Home, Register, Login menu.

23. Run the server and see Whether changes are reflected or not.

24. Now i will be jumping to build a machine learning model.

25. create a machine learning model in jupyter notebook and pickle it.

26. place the model in models folder.

27. Lets create a page for inputs to be given for model.

28. predict_milage.html is input form for milage prediction model.

29. predicted_milage.html is the page for predicted Milage.

30. Go to views.py write a logic for model to predict.

##Database connectivity

1. Go to models.py create a table with ORM (object relational mapping) concept.

```
class MilagePredictionModel(models.Model):
    cylinders=models.IntegerField()
    displacement=models.IntegerField()
    horsepower=models.IntegerField()
    weight=models.IntegerField()
    acceleration=models.IntegerField()
    model_year=models.IntegerField()
    origin=models.IntegerField()
    predicted_value=models.IntegerField(default=18)
```

2. Register the table in admin.py file.

```
from .models import MilagePredictionModel

# Register your models here.

admin.site.register(MilagePredictionModel)

```

3. Make the certain changes in views.py file. Refer views.py file for code.

4. create superuser for admin page to login. you will get all the information on Database.
```
python manage.py createsuperuser
```

5. create a migrations file to create a databse.

```
python manage.py makemigrations
python manage.py migrate
```
6. go to /admin file and check for the Database.

7. You will see the recoreds in database.
