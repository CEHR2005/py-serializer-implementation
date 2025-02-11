from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(required=True, max_length=64)
    model = serializers.CharField(required=True, max_length=64)
    horse_powers = serializers.IntegerField(
        required=True,
        min_value=1,
        max_value=1914)
    is_broken = serializers.BooleanField(required=True)
    problem_description = serializers.CharField(required=False)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.model = validated_data.get("model", instance)
        instance.manufacturer = validated_data.get("manufacturer", instance)
        instance.horse_powers = validated_data.get("horse_power", instance)
        instance.is_broken = validated_data.get("is_broken", instance)
        instance.problem_description = validated_data.get(
            "problem_description", instance
        )
