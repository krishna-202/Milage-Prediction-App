## Milage-Prediction-App

##Installation of Django

* Install python
* Go to command prompt type python --version
* Check the version of pip by typing pip --version.
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

7. You will see the records in database.

##Adding Register, Login, Logout features

1. Let us create a model for user profiles

2. We will use User inbuilt model for username and password and to extent other features will develop our model.

3. We will use User as a one to one mapping for our own model

4. Let us create a another app as accounts.

5. create a model for accounts.

```
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pic',blank=True)


    def __str__(self):
        return self.user.username
```

6. In above code we can see that we are using user object as one of the attribute for our UserProfile model. That user model is having all inbuilt attributes such as first_name,last_name,username,Email,password.

7. Another thing we can see that we used image field and we are uploading it to profile_pic.

8. Let us create profile_pic folder. And we should join this to base directory to find out path.

```
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
```

9. add this static url patterns to original patterns.

```
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
```

10. Go to index.html page create a tab for Register.

11. create page for register form.

12. create a view for register

```
def register(request):
    registered=False
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        portfolio=request.POST['portfolio']
        profile_pic=request.FILES['profile_pic']


        user=User()
        user_profile=UserProfile()
        if password1==password2:

            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.info(request,"username or email Aleady Exists")

            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                user_profile.portfolio=portfolio


                user_profile.profile_pic=request.FILES['profile_pic']
                user_profile.user=user
                user_profile.save()
                registered=True
        else:
            messages.info(request,"Password Mismatch!")



    return render(request,'Register.html',{'registered':registered})
```

13. In register.html make below changes.
```
{% if registered %}
<h2>Thanks for Registering!</h2>
<br>
<a href="{% url 'index' %}">
<input type="button" class="site-btn" name="Back" value="back">
</a>
{% else %}
  <h2>Please Fill the Registration Form!</h2>


  {% for message in messages %}
  <h3>{{ message }}</h3>
  {% endfor %}
```

14. create a login form.

15. create a login and logout features.

```
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials!')


    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

```

16. In index.html make below changes.

```
{% if user.is_authenticated %}
<li><a href="{% url 'accounts:logout' %}">Logout</a></li>
{% else %}
<li><a href="{% url 'accounts:login' %}">Login</a></li>
{% endif %}
```
