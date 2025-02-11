from django.db import models
from model_utils.models import TimeStampedModel

from .constants import (
    MAX_LENGTH_NAME, MAX_LENGTH_DESCRIPTION, DEFAULT_ORDER_ID,
    MAX_DIGITS_FOR_COST, MAX_DECIMAL_PLACES)


class FoodQuerySet(models.QuerySet):

    def with_related_data(self):
        return self.prefetch_related('additional_from',)

    def published(self):
        return self.filter(models.Q(is_publish=True))


class FoodCategoryQuerySet(models.QuerySet):

    def with_related_data(self):
        return self.prefetch_related(
            models.Prefetch(
                'food',
                queryset=Food.objects.published().with_related_data()
            )
        )


class FoodCategory(TimeStampedModel):
    name_ru = models.CharField(verbose_name='Название на русском',
                               max_length=MAX_LENGTH_NAME, unique=True)
    name_en = models.CharField(verbose_name='Название на английском',
                               max_length=MAX_LENGTH_NAME, unique=True,
                               blank=True, null=True)
    name_ch = models.CharField(verbose_name='Название на китайском',
                               max_length=MAX_LENGTH_NAME, unique=True,
                               blank=True, null=True)
    order_id = models.SmallIntegerField(default=DEFAULT_ORDER_ID,
                                        blank=True, null=True)

    objects = FoodCategoryQuerySet.as_manager()

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Раздел меню'
        verbose_name_plural = 'Разделы меню'
        ordering = ('name_ru', 'order_id')


class Food(TimeStampedModel):
    category = models.ForeignKey(FoodCategory, verbose_name='Раздел меню',
                                 related_name='food', on_delete=models.CASCADE)

    is_vegan = models.BooleanField(verbose_name='Вегетарианское меню',
                                   default=False)
    is_special = models.BooleanField(verbose_name='Специальное предложение',
                                     default=False)

    code = models.IntegerField(verbose_name='Код поставщика')
    internal_code = models.IntegerField(verbose_name='Код в приложении',
                                        unique=True, null=True, blank=True)

    name_ru = models.CharField(verbose_name='Название на русском',
                               max_length=MAX_LENGTH_NAME)
    description_ru = models.CharField(verbose_name='Описание на русском',
                                      max_length=MAX_LENGTH_DESCRIPTION,
                                      blank=True, null=True)
    description_en = models.CharField(verbose_name='Описание на английском',
                                      max_length=MAX_LENGTH_DESCRIPTION,
                                      blank=True, null=True)
    description_ch = models.CharField(verbose_name='Описание на китайском',
                                      max_length=MAX_LENGTH_DESCRIPTION,
                                      blank=True, null=True)

    cost = models.DecimalField(verbose_name='Цена',
                               max_digits=MAX_DIGITS_FOR_COST,
                               decimal_places=MAX_DECIMAL_PLACES)

    is_publish = models.BooleanField(verbose_name='Опубликовано', default=True)

    additional = models.ManyToManyField('self',
                                        verbose_name='Дополнительные товары',
                                        symmetrical=False,
                                        related_name='additional_from',
                                        blank=True)

    objects = FoodQuerySet.as_manager()

    def __str__(self):
        return self.name_ru
