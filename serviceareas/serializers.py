from serviceareas.models import ServiceArea
from providers.models import Provider
from providers.serializers import ProviderSerializer
from rest_framework import serializers

class ServiceAreaSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if 'coordinates' in data:
            coordinates = data['coordinates']

            if type(coordinates) != list or \
                any(type(coordinate) != list for coordinate in coordinates) or \
                len(coordinates) < 4:

                raise serializers.ValidationError(
                    {
                        'coordinates': ['This field must be an array of at least 4 Point arrays.']
                    }
                )

            coordinates_positional_errors = []
            for index, point in enumerate(coordinates):
                if len(point) != 2:
                    coordinates_positional_errors.append(
                        {
                            'coordinates[{}]'.format(index): ['Point must have latitude and longitude']
                        }
                    )

            if len(coordinates_positional_errors) > 0:
                raise serializers.ValidationError(
                    {
                        'coordinates': coordinates_positional_errors
                    }
                )

            if coordinates[0] != coordinates[-1]:
                raise serializers.ValidationError(
                    {
                        'coordinates': ['The first point must be equal to the last point to complete the polygon']
                    }
                )

        return data

    class Meta:
        model = ServiceArea
        fields = [
            'id',
            'name',
            'price',
            'provider',
            'coordinates',
            'created',
            'modified'
        ]
