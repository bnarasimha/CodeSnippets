from django.contrib import admin
from .models import CodeSnippet, CodeSnippetLabel, Language

# Register your models here.
admin.site.register(Language)
admin.site.register(CodeSnippet)
admin.site.register(CodeSnippetLabel)