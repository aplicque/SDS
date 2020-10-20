from rest_framework import serializers
# from substances.models import *
# from Chemicals.models import *
from .models import *

""" serializers for reports data"""


class ConditionSerializer(serializers.ModelSerializer):
    """ condition serializer """

    class Meta:
        """ condition """
        model = Conditions
        fields = '__all__'
        depth = 0


class DataSerializer(serializers.ModelSerializer):
    """ data serializer """

    class Meta:
        """ data """
        model = Data
        fields = '__all__'
        depth = 0


class DatapointSerializer(serializers.ModelSerializer):
    """ datapoints serializer """
    conditions = ConditionSerializer(source='conditions_set', many=True, required=False)
    data = DataSerializer(source='data_set', many=True, required=False)

    class Meta:
        """ datapoints """
        model = Datapoints
        fields = '__all__'
        depth = 0


class DataseriesSerializer(serializers.ModelSerializer):
    """ dataseries serializer """
    points = DatapointSerializer(source='datapoints_set', many=True, required=False)

    class Meta:
        """ dataseries """
        model = Dataseries
        fields = '__all__'
        depth = 0


class DatasetSerializer(serializers.ModelSerializer):
    """ dataset serializer """
    series = DataseriesSerializer(source='dataseries_set', many=True, required=False)

    class Meta:
        """ datasets """
        model = Datasets
        fields = '__all__'
        depth = 0


class ReferenceSerializer(serializers.ModelSerializer):
    """ reference serializer """
    class Meta:
        """ references """
        model = References
        fields = '__all__'
        depth = 0


class ReportSerializer(serializers.ModelSerializer):
    """ report serializer """
    sets = DatasetSerializer(source='datasets_set', many=True, required=False)

    class Meta:
        """ reports """
        model = Reports
        fields = '__all__'
        depth = 0


class SystemSerializer(serializers.ModelSerializer):
    """ system serializer """

    class Meta:
        """ system """
        model = Systems
        fields = '__all__'
        depth = 0


class PropertySerializer(serializers.ModelSerializer):
    """ property serializer """
    condition = ConditionSerializer(source='conditions_set', many=True, required=False)
    data = DataSerializer(source='data_set', many=True, required=False)

    class Meta:
        """ property """
        model = Properties
        fields = '__all__'
        depth = 0


class UnitSerializer(serializers.ModelSerializer):
    """ unit serializer """
    conditions = ConditionSerializer(source='conditions_set', many=True, required=False)
    data = DataSerializer(source='data_set', many=True, required=False)
    property = PropertySerializer(source='properties_set', many=True, required=False)

    class Meta:
        """ unit """
        model = Units
        fields = '__all__'
        depth = 0
