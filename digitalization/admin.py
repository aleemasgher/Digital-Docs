from django.contrib import admin
from digitalization.models import Folder, Document, Topic


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['file']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']

