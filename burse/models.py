from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


USER_MODEL = get_user_model()


class Account(models.Model):
    user = models.ForeignKey(to=USER_MODEL, on_delete=models.CASCADE)

    @property
    def username(self) -> str:
        return self.user.username
    
    @property
    def first_name(self) -> str:
        return self.user.first_name
    
    @property
    def last_name(self) -> str:
        return self.user.last_name
    
    def __str__(self) -> str:
        return self.username
    


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, db_index=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self) -> str:
        return reverse('tasks:list_by_category', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return self.name