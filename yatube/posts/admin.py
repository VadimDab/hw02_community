from django.contrib import admin
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    """Класс для управления объектами сообщений в админке."""

    # Перечисляем поля, которые должны отображаться в админке
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group'
    )
    # Позволяет изменять поле group в любом посте без лишних движений
    # мышкой, прямо из списка постов
    list_editable = ('group',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date', 'group')
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    """Класс для управления объектами групп в админке."""

    # Перечисляем поля, которые должны отображаться в админке
    list_display = (
        'pk',
        'title',
        'slug',
        'description'
    )
    search_fields = ('description',)
    list_filter = ('title',)
    empty_value_display = '-пусто-'
# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
