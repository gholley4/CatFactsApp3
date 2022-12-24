from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Fact(models.Model):
    id_facts = models.IntegerField()
    facts = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.facts

class Likes(models.Model):
    id_facts = models.ForeignKey(Fact, on_delete=models.CASCADE)
