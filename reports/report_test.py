""" Create your tests here. """
import os
import django
import json


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from reports.serializers import *

data = ReportSerializer(Reports.objects.get(sysid__exact='20_1'))
print(json.dumps(data.data, indent=2))
