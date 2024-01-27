from rest_framework import serializers

TEMPERATURE_CHOICES = (
    ('celsius', 'Celsius (C)'),
    ('fahrenheit', 'Fahrenheit (F)'),
    ('kelvin', 'Kelvin (K)')
)
TEMPERATURE_CHOICES_LIST = [i[0] for i in TEMPERATURE_CHOICES]

TIME_CHOICES = (
    ('nanosecond', 'Nanosecond'),
    ('microsecond', 'Microsecond'),
    ('millisecond', 'Millisecond'),
    ('second', 'Second'),
    ('minute', 'Minute'),
    ('hour', 'Hour'),
    ('day', 'Day'),
    ('week', 'Week'),
    ('month', 'Month'),
    ('calendar_year', 'Calendar year'),
    ('decade', 'Decade'),
    ('century', 'Century')
)

TIME_CHOICES_LIST = [i[0] for i in TIME_CHOICES]


class TemperatureSerializer(serializers.Serializer):
    degrees = serializers.FloatField(required=True)
    from_ = serializers.ChoiceField(choices=TEMPERATURE_CHOICES, required=True)
    to_ = serializers.ChoiceField(choices=TEMPERATURE_CHOICES, required=True)

    def validate_from_(self, value):
        print(value)
        if value not in TEMPERATURE_CHOICES_LIST:
            raise serializers.ValidationError("Invalid 'from_' value.")
        return value

    def validate_to_(self, value):
        if value not in TEMPERATURE_CHOICES_LIST:
            raise serializers.ValidationError("Invalid 'to_' value.")
        return value

    def validate(self, data):
        """
        Check that 'from_' and 'to_' fields are different.
        """
        from_temp = data.get('from_')
        to_temp = data.get('to_')

        if from_temp == to_temp:
            raise serializers.ValidationError("The 'from_' and 'to_' fields cannot be the same.")

        return data
    

class TimeSerializer(serializers.Serializer):
    value = serializers.FloatField(required=True)
    from_ = serializers.ChoiceField(choices=TIME_CHOICES, required=True)
    to_ = serializers.ChoiceField(choices=TIME_CHOICES, required=True)