##### Setup Django Project	

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

