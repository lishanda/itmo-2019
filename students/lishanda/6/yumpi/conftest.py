# -*- coding: utf-8 -*-


import os
import subprocess  # noqa: S404

import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzapp.settings')


def pytest_configure():
    """`Pytest` automatically calls this function once when tests are run."""
    settings.DEBUG = False
    django.setup()

    cmd1 = 'python students/lishanda/6/manage.py makemigrations'
    cmd2 = 'python students/lishanda/6/manage.py migrate --run-syncdb'

    subprocess.check_call(cmd1, shell=True)  # noqa: S607, S602
    subprocess.check_call(cmd2, shell=True)  # noqa: S607, S602
