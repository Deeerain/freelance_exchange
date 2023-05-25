from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from pytils.translit import slugify
from django.utils.translation import gettext_lazy as _


USER_MODEL = get_user_model()


class Category(models.Model):
    name = models.CharField(_('Название'), max_length=30,
                            unique=True, db_index=True)
    slug = models.SlugField(_('Слаг'), unique=True)

    class Meta:
        verbose_name = _('Категория')
        verbose_name = _('Категории')

    def get_absolute_url(self) -> str:
        return reverse('tasks:list_by_category', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    title = models.CharField(_('Название'), max_length=30)
    description = models.TextField(_('Описание'))
    employer = models.ForeignKey(verbose_name=_('Заказчик'), to=USER_MODEL,
                                 on_delete=models.CASCADE,
                                 null=True)
    created = models.DateTimeField(_('Время создания'), auto_now=True)
    updated = models.DateTimeField(_('Время обновления'), auto_now_add=True)
    visible = models.BooleanField(_('Видимость'), default=True)
    price_from = models.DecimalField(_('Цена от'), max_digits=10,
                                     decimal_places=2,
                                     null=True, blank=True)
    price_to = models.DecimalField(_('Цена до'), max_digits=10,
                                   decimal_places=2, null=True,
                                   blank=True)
    category = models.ForeignKey(verbose_name=_('Категория'), to=Category,
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL)
    slug = models.SlugField(_('Слаг'), blank=True, unique=True)

    class Meta:
        verbose_name = _('Задача')
        verbose_name_prular = _('Задачи')

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
    user = models.ForeignKey(verbose_name=_('Пользователь'), to=USER_MODEL,
                             related_name='feedbacks',
                             null=True,
                             on_delete=models.SET_NULL)
    task = models.ForeignKey(verbose_name=_('Задача'), to=Task, null=True,
                             on_delete=models.SET_NULL)
    text = models.TextField(_('Текст'), max_length=1000)
    evaluation = models.DecimalField(_('Оценка'), max_digits=5,
                                     decimal_places=1)
    created = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')

    def __str__(self) -> str:
        return self.text
