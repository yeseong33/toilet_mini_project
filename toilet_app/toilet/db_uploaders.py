import os
import django
import csv
import sys

sys.path.append(os.pardir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "toilet_grade_app.settings")
django.setup()

from toilet.models import *

CSV_PATH = '../toilet.csv'

def insert_menu():
    with open(CSV_PATH, newline='', encoding='utf8') as csvfile:
        data_reader = csv.DictReader(csvfile)
        