from django.db.models import fields
from reservations.models import Reserve
from rest_framework import serializers
from django.utils import timezone as tz




class ReservationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Reserve
        fields = ('name', 'reserve_datetime', 'people_quantity', 'phone_number', 'comment')

    

    def create(self, validated_data):
        reserve_time = validated_data['reserve_datetime']
        if reserve_time.hour in range(17, 24) and reserve_time>=tz.now():
            obj = Reserve.objects.create(**validated_data)
        else:
            raise serializers.ValidationError('Bar closed')
        return obj