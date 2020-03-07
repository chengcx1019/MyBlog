"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, `
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
# choose settings between Developement and Deploy

import platform

node = platform.node()

dev_machines = ('cheng-cx', 'chengcx', 'chengcx.local', 'cheng-cx.local')

if node in dev_machines:
    print('Debug')
    # folder BASE_DIR or project myblog dir which is the same as app folder.
    # project dir, contains static and media folder under deploy environment

    DEBUG =  True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'blogcx',
            'USER': 'root',
            'PASSWORD': '123456',
            'host': 'localhost',
            'PORT': '3306',
        }
    }

    ALLOWED_HOSTS = ['*']
else:
    print('prod')
    DEBUG =True 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'blogcx',
            'USER': 'blogcx',
            'PASSWORD': '789012',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

    ALLOWED_HOSTS = [
        '*',
    ]
