from rest_framework import serializers

from .models import Position, Employee, emp_statuses


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    position = PositionSerializer()
    status = serializers.ChoiceField(choices=emp_statuses)


class EmployeeDtoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    position_name = serializers.CharField(max_length=100)
    status = serializers.ChoiceField(choices=emp_statuses)