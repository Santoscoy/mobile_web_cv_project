"""
WSGI config for cv_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cv_project.settings')
from dotenv import load_dotenv

project_folder = os.path.expanduser('/home/santoscoy/Documents/mobile_web_cv_project/cv_project')
load_dotenv(os.path.join(project_folder,'.env'))

application = get_wsgi_application()

