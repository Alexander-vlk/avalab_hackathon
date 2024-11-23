from django.db import models


class UserData(models.Model):
    """Модель пользовательских данных"""
    
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
    
    
class GeneratedData(models.Model):
    """Модель сгенерированных с помощью ИИ данных"""
    
    user_data = models.OneToOneField(
        UserData,
        on_delete=models.CASCADE,
        verbose_name='Пользовательские данные',
    )
    text = models.CharField(
        max_length=5000,
        null=True,
        blank=True,
        verbose_name='Сгенерированный текст',
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
        verbose_name = 'Сгенерированные данные'
        
    def __str__(self):
        return self.text[:50]
    
    def save(self):
        """Здесь должна быть логика обработки данных с использованием ИИ"""
        return super().save()


class DataFromSite(models.Model):
    """Модель данных, полученных с сайта"""
    
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
        """Возвращает url сайта, с которого получены данные"""
        return self.site_url
    
