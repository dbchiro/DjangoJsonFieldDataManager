# SINP Organisms for Django

[DjangoJsonFieldDataManager](https://github.com/dbchiro/DjangoJsonFieldDataManager) is a simple [Django](https://www.djangoproject.com/) reusable app to manage an extra_data JSON field possible key/values.

See docs for more details : <https://dbchiro.github.io/DjangoJsonFieldDataManager/>

## Quick start

1. Install app

```bash
pip install -U jsondata_manager
```

2. Configure `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    (...),
    'rest_framework',
    'jsondata_manager',
    (...),
)
```

3. Configure `urls.py`:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    (...),
    path('api/v1/', include('jsondata_manager.urls')),
    (...),
]
```

4. Run `python manage.py migrate` to create the polls models.
5. Start the development server and visit <http://127.0.0.1:8000/admin/>
   to create an organism (you'll need the Admin app enabled).
6. Visit <http://127.0.0.1:8000/api/v1/extradata> to view organisms API.

## Database models

![models.png](./docs/_static/models.png)
