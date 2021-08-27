from django.contrib import admin
from django.utils.safestring import mark_safe
from posters.models import Posters

class PostersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', "get_image")
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    readonly_fields=("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')

    get_image.short_desription = "Изображение"

    

admin.site.register(Posters, PostersAdmin)
