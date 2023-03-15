from rest_framework.serializers import ModelSerializer
from .models import *

class InfoSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"

class SocialMediaSerializer(ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"

class MatchSerializer(ModelSerializer):
    class Meta:
        model = Match
        fields = "__all__"

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"

class AcademySerializer(ModelSerializer):
    class Meta:
        model = Academy
        fields = "__all__"

class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"

class MediaMatchSerializer(ModelSerializer):
    class Meta:
        model = MediaMatch
        fields = "__all__"

class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"

class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"