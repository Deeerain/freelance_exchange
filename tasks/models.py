from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from pytils.translit import slugify


from burse.models import Category

USER_MODEL = get_user_model()


class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    employer = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE,
                                 null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    price_from = models.DecimalField(max_digits=10, decimal_places=2,
                                     null=True, blank=True)
    price_to = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                   blank=True)
    categories = models.ForeignKey(Category, null=True, blank=True,
                                   on_delete=models.SET_NULL)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs) -> None:
        value = f'{self.title}-{str(self.employer.pk)}'
        self.slug = slugify(value)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tasks:detail', kwargs={
            'category_slug': self.categories.slug, 'slug': self.slug
            })

    def __str__(self) -> str:
        return self.title
