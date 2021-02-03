from webapp.models import Language
from django.shortcuts import render
from .models import CodeSnippet, CodeSnippetLabel, Language

def home(request):
        languages = Language.objects.all()
        codesnippets = CodeSnippet.objects.all()
        codesnippetlabels = CodeSnippetLabel.objects.all()
        return render(request, "home.html", 
                { 
                "languages" : languages,
                "codesnippets" : codesnippets,
                "codesnippetlabels" : codesnippetlabels
                })