###### Setup Django Project	

```python
#Create python env [blogenv]
python -m venv blogenv
source ./blogenv/bin/activate

pip install django

django-admin startproject blog 
python manage.py runserver

python manage.py startapp blogapp

#Create file in blogapp
-  urls.py
- templates/main.html

pip install django-debug-toolbar
```

##### INSTALL DJANGO REST FRAMEWORK

```python
pip install djangorestframework
```

setting.py

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

views.py

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_data(request):
    api_urls = {
        'list' : '/task-list',
        'Detail' : '/task-detail/<str:pk>/',
    } 
    return Response(api_urls)
```

##### STATIC FILES | CSS TO MAIN.HTML

```python
1. Create static/css/style.css
2. load css in main.html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

Setting.py

```python
#add
import os
STATIC_URL = 'static/'
#add
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

```

###### INSTALL TAILWIND

```python
#[RECOMMENDED IN DEV] If you want to use automatic page reloads during development use the [reload] extras, which installs the django-browser-reload package in addition:
doc
#https://django-tailwind.readthedocs.io/en/latest/installation.html

pip install django-tailwind
pip install 'django-tailwind[reload]'

```

setting.py

```python
INSTALLED_APPS = [
  # other Django apps
  'tailwind',
]
```

```python
python manage.py tailwind init
```

setting.py

```python
INSTALLED_APPS = [
  # other Django apps
  'tailwind',
  'theme'
]

TAILWIND_APP_NAME = 'theme'
```

```python
python manage.py tailwind install
```

The *Django Tailwind* comes with a simple `base.html` template located at `your_tailwind_app_name/templates/base.html`. You can always extend or delete it if you already have a layout.

If you are not using the `base.html` template that comes with *Django Tailwind*, add `{% tailwind_css %}` to the `base.html` template:

```python
#you can use this in layout.html for this project
{% load static tailwind_tags %}
...
<head>
   ...
   {% tailwind_css %}
   ...
</head>
```

```python
#now you have to run two cmd 
python manage.py runserver 
python manage.py tailwind start

```

Let’s also add and configure `django_browser_reload`, which takes care of automatic page and css refreshes in the development mode. Add it to `INSTALLED_APPS` in `settings.py`:

```
INSTALLED_APPS = [
  # other Django apps
  'tailwind',
  'theme',
  'django_browser_reload'
]

MIDDLEWARE = [
  # ...
  "django_browser_reload.middleware.BrowserReloadMiddleware",
  # ...
]
```

Include `django_browser_reload` URL in your root `url.py`:

```
from django.urls import include, path
urlpatterns = [
    ...,
    path("__reload__/", include("django_browser_reload.urls")),
]
```
