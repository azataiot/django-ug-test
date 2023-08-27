# Django Test App for Uyghur (ug)

## About

A Django Application built with https://github.com/azataiot/django-ug, which adds supports to Django Versions until Django 5.x ( Official support for Uyghur is coming in Django 5.0)

## Installation

1. Install the package from PyPI:

```bash
pip install django-ug
```

2. Add `django.middleware.locale.LocaleMiddleware` to your `MIDDLEWARE` setting:

```python
MIDDLEWARE = [
    ...
    'django.middleware.locale.LocaleMiddleware',
    ...
]
```

3. Add languages to your `LANGUAGES` setting:

```python
from django.utils.translation import gettext_lazy as _
LANGUAGES = (
    ("en", _("English")),
    ("ug", _("Uyghur")),
    ("ug-latin", _("Uyghur Latin")),
    ("ug-cyrillic", _("Uyghur Cyrillic")),
)
```

4. Create and set up the `locale` directory:

```python
LOCALE_PATHS = [
    BASE_DIR / "locale/",
]
```

5. Run `makemessages` and `compilemessages`:

```bash
python manage.py makemessages -l ug 
python manage.py makemessages -l ug_Latin
python manage.py makemessages -l ug_Cyrllic
python manage.py compilemessages
```

Hola ! You are ready to go !

All other settings are exactly same as Django's official documentation.