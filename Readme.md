# Django

### Install Django

```bash
python3 -m pip install Django
```

> Check to make sure it's installed...

```bash
django-admin
```

#### Create a project

```bash
django-admin startproject mypage
```

#### Within the mypage directory that gets created:

```
- mypage/
    - manage.py
    - mypage/
        - __init__.py
        - settings.py
        - urls.py
        - asgi.py
        - wsgi.py
```

- The settings.py and urls.py files are the ones that we will be working with the most.

##### Start Development Server

```bash
python3 manage.py runserver

```

##### Create an app

```bash
python3 manage.py startapp challenges
```

### Activating virtual environment

**Open the Command Palette (Ctrl+Shift+P), then select the Python: Select Interpreter. From the list, select the virtual environment in your project folder that starts with .env.**

**Run Terminal: Create New Integrated Terminal (Ctrl+Shift+` or from the Command Palette), which creates a terminal and automatically activates the virtual environment by running its activation script.**

### Views:

- A view is either a function or a class.
- We do not call the view function directly... Django does this for us.

> Basic example of a view function:

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("This works!")
```

Here the HttpResponse we are returning is an instance of the HttpResponse class. This class is defined in the django.http module. This module contains classes that handle requests and responses.

- In order for Django to know when to call the view function we need to create an adjacent file called `urls.py` in the same directory as the `views.py` file.

```py
from django.urls import path
from . import views
# UrlConfig
urlpatterns = [
    path("january", views.index)
]

```

1. from django.urls import path: This line imports the path function from the django.urls module. The path function is used to define URL patterns in Django.

2. from . import views: This line imports the views module from the current directory (denoted by the dot .). In Django, views are Python functions that handle HTTP requests and return HTTP responses.

3. urlpatterns = [...]: This line creates a list called urlpatterns which will store all the URL patterns for your Django project.

4. path("january", views.index): This line defines a URL pattern. It uses the path function to specify that any request to the "/january" URL should be handled by the index view function imported from the views module.

**In the global urls.py file**

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("challenges/", include("challenges.urls"))
    ]
```

`path("challenges/", include("challenges.urls"))` tells us that we want to forward any requests that start with challenges/ to the challenges.urls module. This module will then handle the request further.

### When we forward from:

```py
    path("challenges/", include("challenges.urls"))
    # To...
    path("january", views.index)
```

- We end up with a url of `challenges/january`
- We get the following:

![This works!](./images/2023-10-02-09-50-25.png)

![Request Response Flow](./images/2023-10-02-09-54-03.png)

**Dynamic path Segments**

> Instead of:

```py
from django.urls import path
from . import views

# UrlConfig
urlpatterns = [
    path("january", views.january),
    path("february", views.february),
    path("march", views.march),
#...
]
```

> We can use angle brackets to signify any path that comes after challenges/

```py
from django.urls import path
from . import views

# UrlConfig
urlpatterns = [
    path("<month>", views.monthly_challenge)
]

```

> And we replace

```py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("Eat no meat for the entire month!")


def february(request):
    return HttpResponse("Walk for at least 20 min every day!")


def march(request):
    return HttpResponse("Learn Django for at least 20 min every day!")

```

> With:

```py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Here month captures the dynamic path segments from
#urlpatterns = [
#    path("<month>", views.monthly_challenge)
#]

def monthly_challenge(request, month):
    return HttpResponse("This works for any month!")

```


**Revised views.py**

```py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "Eat no meat for the entire month!"
    elif month == 'february':
        challenge_text = "Walk for at least 20 minutes every day!"
    elif month == 'march':
        challenge_text = "Learn Django for at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(challenge_text)
```


**Telling Django what data type to expext in dynamic path segments**

```py
from django.urls import path
from . import views

# UrlConfig
urlpatterns = [
    path("<str:month>", views.monthly_challenge)
]
```

> The `<str:month>` tells Django to expect a string value in the month variable.


**Handlin month input as either string or number**

```py
# Views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "Eat no meat for the entire month!"
    elif month == 'february':
        challenge_text = "Walk for at least 20 minutes every day!"
    elif month == 'march':
        challenge_text = "Learn Django for at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(challenge_text)
```

```py
# Urls.py
from django.urls import path
from . import views

# UrlConfig
urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge)
]
```
