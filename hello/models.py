from django.db import models

# Create your models here.
class Card(models.Model):
    COMMON = 1
    RARE = 2
    EPIC = 3
    LEGENDARY = 4
    CARD_TYPES = (
        (COMMON, 'common'),
        (RARE, 'rare'),
        (EPIC, 'epic'),
        (LEGENDARY, 'legendary')
    )
    name = models.CharField('name', primary_key=True, max_length=50)
    type = models.IntegerField('type', choices=CARD_TYPES)
