from django.contrib import admin

from models import Word, Origin


class WordAdmin(admin.ModelAdmin):
    raw_id_fields = ("root_word", )
    # prepopulated_fields = {"slug": ("name",)}


class OriginAdmin(admin.ModelAdmin):
    pass

admin.site.register(Word, WordAdmin)
admin.site.register(Origin, OriginAdmin)
