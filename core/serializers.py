from rest_framework import serializers
from core import models


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Zone
        fields = '__all__'

# class DepartmentSerializer(serializers.ModelSerializer):
#    class Meta:
#       model = models.Department
#       fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


class DepartmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    created_at = serializers.DateTimeField(required=False)
    modified_at = serializers.DateTimeField(required=False)
    active = serializers.BooleanField(required=False)
    name = serializers.CharField(required=False, max_length=64)

    def validate(self, attrs):
        if not attrs.get('name').isupper():
            raise Exception('O NOME DO DEPARTAMENTO DEVE SER EM MAIÚSCULO ')
        return super(DepartmentSerializer, self).validate(attrs)

    def create(self, validated_data):
        return models.Department.objects.create(**validated_data)


