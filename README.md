## Milage-Prediction-App

1. Create a Django project using Django-admin startproject Milage_Prediction_Website using command prompt.

2. Go to project directory and create a app using Django-admin startapp Milage_Prediction_App.

3. Run the server using python manage.py runserver.

4. Check in the localhost to verify server is running or not.

5. Lets Focus on Frontend part.

6. Download Some free templates from google..I will be taking from colorlib Website.

7. Create a tepmlates folder in Milage_Prediction_Website project folder(Top level directory).

8. Copy index.html file from which you have downloaded templates folder.

9. Go to urls.py file and include below code
```from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Milage_Prediction_App.urls')),
]

```

10. Create a another urls.py file in Milage_Prediction_App folder and include below code
 ```
 from django.urls import path
 from . import views

 urlpatterns=[
     path('',views.index,name='index'),
 ]

```

11. Now Go to views.py file and create below code
```
def index(request):
    return render(request,'index.html')

```

12. Go to settings.py file create a Templates directory and include directory in TEMPLATES list
```
TEMPLATES_DIR=os.path.join(BASE_DIR,"templates")
'DIRS': [TEMPLATES_DIR],
```

13. Add a App name in INSTALLED_APPS.

14. Run the server and see.
