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
  CARD_TYPES_IDICT = {
    'common': COMMON,
    'rare': RARE,
    'epic': EPIC,
    'legendary': LEGENDARY
  }
  CARDS_REQUIRED_TO_UPGRADE = [2, 4, 10, 20, 50, 100, 200, 400, 800, 1000,
      2000, 5000]
  MAX_LEVEL = [13, 11, 8, 5]
  name = models.CharField('name', primary_key=True, max_length=50)
  type = models.IntegerField('type', choices=CARD_TYPES)
  elixir = models.IntegerField('elixir')
  arena = models.IntegerField('arena')

  @classmethod
  def get_type(cls, str_type):
    return cls.CARD_TYPES_IDICT[str_type]

class User(models.Model):
  handle = models.CharField('handle', primary_key=True, max_length=20)

class MyCard(models.Model):
  class Meta:
    unique_together = (('user', 'card'),)
  user = models.ForeignKey('user', on_delete=models.CASCADE)
  card = models.ForeignKey('card', on_delete=models.PROTECT)
  quantity = models.PositiveIntegerField('quantity')
  level = models.PositiveIntegerField('level')
