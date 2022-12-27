from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

# Create your models here.

class Fact(models.Model):
    id_facts = models.UUIDField(primary_key=True, default=uuid.uuid4)
    facts = models.CharField(max_length=300)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.facts

#class Likes(models.Model):
    #id_facts = models.ForeignKey(Fact, on_delete=models.CASCADE)
    #id_user = models.ForeignKey(get_user_model, on_delete=models.CASCADE) 

#class Favoritos(models.Model):
    #id_facts = models.ForeignKey(Fact, on_delete=models.CASCADE)
    #nro_likes = models.IntegerField(default=0)
