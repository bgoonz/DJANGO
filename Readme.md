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
