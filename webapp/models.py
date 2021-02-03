from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=100)

class CodeSnippet(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    codesnippet = models.TextField()
    language = models.ForeignKey("Language", null=True, blank=True, on_delete=CASCADE)

class CodeSnippetLabel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    codesnippet = models.ForeignKey("CodeSnippet", on_delete=CASCADE)