from django.contrib import admin
from django.utils.safestring import mark_safe
from posters.models import *


class TicketInline(admin.StackedInline):
    model = Ticket
    list_display = ('title', 'price')
    extra = 0
    search_fields = ('event',)
    readonly_fields = ("title", "price")  

class SessionInline(admin.StackedInline):
    model = Session
    extra = 0

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('title_address', 'address')



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'get_image')
    list_display_links = ('title',)
    search_fields = ('title',)
    inlines = [TicketInline, SessionInline]
    readonly_fields = ("get_image",)
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 400px;">')


""" @admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','description', "get_image")
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    readonly_fields=("get_image", "title", "description")
    inlines = [SessionInline]

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 400px;">')

    get_image.short_desription = "Изображение" """
    

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'event')
    list_display_links = ('title',)
    search_fields = ('title',)
    readonly_fields=("get_scheme",)

    def get_scheme(self, obj):
        return mark_safe(f'<img src="{obj.scheme.url}" style="max-height: 400px;">')


    


    

#admin.site.register(Event, EventAdmin)
#admin.site.register(Session)
#admin.site.register(Ticket)
