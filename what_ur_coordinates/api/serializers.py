from rest_framework import serializers

from cadastral.models import Coordinates, Result


class CoordinatesSerializer(serializers.ModelSerializer):
    """Сериализатор для координат"""

    class Meta:
        model = Coordinates
        fields = [
            'cadastral_numb',
            'latitude',
            'longitude'
        ]


class ResultSerializer(serializers.ModelSerializer):
    """Сериализатор для результата"""
    coordinates = serializers.SlugRelatedField(
        queryset=Coordinates.objects.all(),
        slug_field='cadastral_numb')

    class Meta:
        model = Result
        fields = [
            'coordinates',
            't_or_f'
        ]
