from django.contrib import admin
from django.utils.safestring import mark_safe
from posters.models import *

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','description', "get_image")
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    readonly_fields=("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')

    get_image.short_desription = "Изображение"

    

admin.site.register(Event, EventAdmin)
admin.site.register(Session)
admin.site.register(Ticket)
