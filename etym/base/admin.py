from django.contrib import admin

from models import Word, Origin


class WordAdmin(admin.ModelAdmin):
    pass


class OriginAdmin(admin.ModelAdmin):
    pass

admin.site.register(Word, WordAdmin)
admin.site.register(Origin, OriginAdmin)
