from django.db import models

from main.constants import LENGTH_CHAR_FIELD, LENGTH_STR


class CreatedAt(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        abstract = True
        ordering = ('created_at',)


class IsPublished(CreatedAt):
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    class Meta:
        abstract = True
        

class Category(IsPublished):
    title = models.CharField(
        max_length=LENGTH_CHAR_FIELD,
        verbose_name='Заголовок'
    )
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=('Идентификатор страницы для URL; разрешены символы латиницы'
                   ', цифры, дефис и подчёркивание.')
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title[:LENGTH_STR]


class Product(IsPublished):
    name = models.CharField(
        max_length = 50,
        verbose_name='Изделие'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена'
    )
    image = models.ImageField('Фото', upload_to='products_images', blank=True)
    text = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
        related_name='products'
    )

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)

    def __str__(self):
        return self.name[:LENGTH_STR]
