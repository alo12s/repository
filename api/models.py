from django.db import models
from datetime import date, datetime


class Info(models.Model):
    logo = models.ImageField(blank=True, null=True, upload_to="logo/")
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()


class SocialMedia(models.Model):
    img = models.ImageField(blank=True, null=True, upload_to="social_medias/")
    link = models.URLField()


class Player(models.Model):
    img = models.ImageField(blank=True, null=True, upload_to="players/")
    number = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    games = models.IntegerField()
    minutes = models.IntegerField()
    started = models.IntegerField()
    sub_off = models.IntegerField()


class Team(models.Model):
    name = models.CharField(max_length=255)
    players = models.ManyToManyField(Player)


class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name="match_team1", on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name="match_team2", on_delete=models.CASCADE)
    quarter = models.IntegerField()
    datetime = models.DateTimeField(default=datetime.now())


class Academy(models.Model):
    text = models.TextField()
    trainer_img = models.ImageField()
    trainer_name = models.CharField(max_length=255)


class Media(models.Model):
    media = models.FileField()


class MediaMatch(models.Model):
    media = models.FileField()
    team1 = models.ForeignKey(Team, related_name="media_team1", on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name="media_team2", on_delete=models.CASCADE)
    team1_score = models.IntegerField()
    team2_score = models.IntegerField()
    date = models.DateField(default=date.today())


class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(blank=True, null=True, upload_to="news/")
    is_banner = models.BooleanField(default=False)
    date = models.DateField(default=date.today())


class Shop(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(blank=True, null=True, upload_to="products/")