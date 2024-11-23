from django.db import models


class UserData(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название бизнеса',
    )
    business_type = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Тип бизнеса',
    )
    region = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Регион',
    )
    industry = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Отрасль бизнеса'
    )
    is_innovative = models.BooleanField(
        null=True,
        blank=True,
        verbose_name='Есть ли инновации',
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
    )
    
    class Meta:
        verbose_name = 'Пользовательские данные'
        ordering = ['-updated_at']
    
    def __str__(self):
        return self.name
