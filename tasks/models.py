from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from pytils.translit import slugify


USER_MODEL = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, db_index=True)
    slug = models.SlugField(unique=True)

    def get_count(self) -> str:
        return Task.objects.filter(categories=self, visible=True).count()

    def get_absolute_url(self) -> str:
        return reverse('tasks:list_by_category', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return self.name


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
    category = models.ForeignKey(Category, null=True, blank=True,
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


class Feedback(models.Model):
    user = models.ForeignKey(USER_MODEL, related_name='feedbacks',
                             null=True,
                             on_delete=models.SET_NULL)
    task = models.ForeignKey(Task, null=True, on_delete=models.SET_NULL)
    text = models.TextField('Текст', max_length=1000)
    evaluation = models.DecimalField('Оценка', max_digits=5, decimal_places=1)
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self) -> str:
        return self.text
