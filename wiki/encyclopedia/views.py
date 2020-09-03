from django.shortcuts import render

from . import util

from markdown2 import Markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entrytitle):
    entry = util.get_entry(entrytitle)
    markdowner = Markdown()
    entry = markdowner.convert(entry)
    if entry == None:
        return render(request, "encyclopedia/not_found.html")
    return render(request, "encyclopedia/entry.html", {
        "entrytitle": entrytitle,
        "entry": entry
    })
