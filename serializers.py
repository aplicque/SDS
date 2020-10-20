""" serializers for substance data"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()


from rest_framework import serializers
from substances.models import *


class IdentifierSerializer(serializers.ModelSerializer):
    """ identifiers serializer """
    class Meta:
        """ settings """
        model = Identifiers
        fields = '__all__'
        depth = 1


class SubstanceSerializer(serializers.ModelSerializer):
    """ substance serializer """
    ids = IdentifierSerializer(source='identifiers_set', many=True, required=False)

    class Meta:
        """ settings """
        model = Substances
        fields = '__all__'
        depth = 1


