from users.models import User
from rest_framework import serializers
from .models import Review
# import telegram
# from django.core.serializers.json import DjangoJSONEncoder
# from django.core.serializers import serialize
# from ipware.ip import get_ip
# from django.conf import settings



# URL = settings.BOT_URL
# my_tokem = settings.BOT_TOKEN
# my_chat_id = settings.BOT_CHAT_ID


# class TelegramBot(DjangoJSONEncoder):
#     def default(self,obj):
#         if isinstance(obj, dict):
#             return str(obj)
#         return super().default(obj)


# def bot(request,msg,my_chat_id=my_chat_id, token=my_tokem):
#     bot=telegram.BOT(token=token)
#     bot.sendMessage(chat_id=chat_id,text=msg)


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    dob = serializers.DateField()
    # email = serializers.EmailField()


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('phone_number', 'text')
