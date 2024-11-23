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


class DataFromSite(models.Model):
    user_data = models.OneToOneField(
        UserData,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Данные с сайта',
    )
    site_url = models.URLField(
        max_length=500,
        verbose_name='URL сайта',
    )
    text = models.CharField(
        max_length=5000,
        null=True,
        blank=True,
        verbose_name='Текст с сайта',
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
        verbose_name = 'Данные с сайта'
        
    def __str__(self):
        return self.site_url
    