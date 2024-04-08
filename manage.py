#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

### To start a Django project ###
### Start by setting up Flask which is python -m vevn env > Set-ExecutionPolicy RemoteSigned -Scope Process > env\Scripts\activate
### Then pip install django > django-admin startproject mysite . > python manage.py startapp [INSERT APP NAME HERE]
### Then make sure that the name of your app is under INSTALLED_APPS of settings.py of mysite. Check the node in this app to see how that looks like
### Further, you can check qr.py to see how to create a qrcode leading to your website.

### We can create an admin login using python manage.py createsuperuser

############# Left off at Node 465 ##################