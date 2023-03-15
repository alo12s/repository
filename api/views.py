from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .forms import *

from datetime import datetime

@api_view(["GET"])
def get_info(request):
    info = Info.objects.last()
    info_ser = InfoSerializer(info)
    social_medias = SocialMedia.objects.all()
    social_media_ser = SocialMediaSerializer(social_medias, many=True)
    data = {
        "data": info_ser.data,
        "social_media": social_media_ser.data
    }
    return Response(data)

@api_view(["GET"])
def get_main_page(request):
    banners = News.objects.filter(is_banner=True)
    banner_ser = NewsSerializer(banners, many=True)
    lis = Match.objects.all()
    matches = []
    for i in lis:
        if str(i.datetime)[8:10] == str(datetime.now())[8:10]:
            matches.append(i)
    match_ser = MatchSerializer(matches, many=True)
    data = {
        "data": banner_ser.data,
        "matches": match_ser.data
    }
    return Response(data)

@api_view(["GET"])
def get_media(request):
    medias = Media.objects.all().order_by("-id")
    medias_ser = MediaSerializer(medias, many=True)
    media_matches = MediaMatch.objects.all().order_by("-id")
    media_matches_ser = MediaMatchSerializer(media_matches, many=True)
    media_ser = medias_ser.data + media_matches_ser.data
    data = {
        "data": media_ser
    }
    return Response(data)

@api_view(["GET"])
def get_news(request):
    news = News.objects.all()
    news_ser = NewsSerializer(news, many=True)
    data = {
        "data": news_ser.data
    }
    return Response(data)

@api_view(["GET"])
def get_shop(request):
    products = Shop.objects.all().order_by("-id")
    product_ser = ShopSerializer(products, many=True)
    data = {
        "data": product_ser.data
    }
    return Response(data)

@api_view(["POST"])
def add_product(request):
    form = ShopForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    product_ser = ShopSerializer(Shop.objects.last())
    data = {
        "data": product_ser.data
    }
    return Response(data)

@api_view(["GET"])
def get_statistics(request):
    matches = Match.objects.all().order_by("-id")
    match_ser = MatchSerializer(matches, many=True)
    data = {
        "match": match_ser.data,
    }
    return Response(data)

@api_view(["GET"])
def get_player(reuqest):
    players = Player.objects.all()
    player_ser = PlayerSerializer(players, many=True)
    data = {
        "data": player_ser.data
    }
    return Response(data)

@api_view(["GET"])
def get_academy(request):
    academy = Academy.objects.last()
    academy_ser = AcademySerializer(academy)
    data = {
        "data": academy_ser.data
    }
    return Response(data)