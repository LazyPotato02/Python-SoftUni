from django.core import validators
from django.db import models


def min_age_validator(value):
    if value >= 12:
        return value
    else:
        raise validators.ValidationError('Age must be 12 or greater!')


def min_rating_validator(value):
    if value >= 0.1:
        return value
    else:
        raise validators.ValidationError('Rating must be 0.1 or greater!')


def max_rating_validator(value):
    if value <= 5.0:
        return value
    else:
        raise validators.ValidationError('Rating must be 5.0 or lower!')


def max_level_validator(value):
    if value >= 1:
        return value
    else:
        raise validators.ValidationError('Level cannot be below 1!')


# Create your models here.

class Person(models.Model):
    email = models.EmailField(
        blank=False,
        null=False,
    )
    age = models.IntegerField(
        validators=(min_age_validator,),
        blank=False,
        null=False,
    )
    password = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )
    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class Game(models.Model):
    class Meta:
        ordering = ('pk',)
    RATING_MIN_VALUE = 0.1
    RATING_MAX_VALUE = 5.0
    MAX_LEVEL = 1
    Action = "Action"
    Adventure = "Adventure"
    Puzzle = "Puzzle"
    Strategy = "Strategy"
    Sports = "Sports"
    Board_Card_Game = "Board/Card Game"
    Other = "Other"

    CATEGORY = (
        (Action, Action),
        (Adventure, Adventure),
        (Puzzle, Puzzle),
        (Strategy, Strategy),
        (Sports, Sports),
        (Board_Card_Game, Board_Card_Game),
        (Other, Other),
    )

    title = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        null=False,
    )
    category = models.CharField(
        max_length=15,
        choices=CATEGORY,
        blank=False,
        null=False,
    )
    rating = models.FloatField(
        validators=(
            min_rating_validator,
            max_rating_validator,
        ),
        blank=False,
        null=False,
    )
    max_level = models.IntegerField(
        verbose_name='Max Level',
        validators=(max_level_validator,),
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        blank=False,
        null=False,
    )
    summary = models.TextField(
        blank=True,
        null=True,
    )
