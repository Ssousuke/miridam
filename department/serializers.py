from rest_framework import serializers
from department.models import Department, Occupation


class DepartmentSerializer(serializers.ModelSerializer):
    """
    Serializers a Department objects
    """

    class Meta:
        model = Department
        fields = (
            'department',
            'created_at',
            'updated_at',
        )


class OccupationSerializers(serializers.ModelSerializer):
    """
    Serializers a Occupation objects
    """

    class Meta:
        model = Occupation
        fields = (
            'occupation',
            'department',
            'created_at',
            'updated_at',
        )
