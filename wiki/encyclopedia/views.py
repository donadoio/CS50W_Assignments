from django.shortcuts import render

from markdown2 import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entrytitle):
    entrycontent = util.get_entry(entrytitle)
    if entrycontent == None:
        return render(request, "encyclopedia/entry-not-found.html", {
            "entrytitle": entrytitle
        })
    else:
        entrycontent = markdown(entrycontent)
        return render(request, "encyclopedia/entry.html", {
            "entrytitle": entrytitle,
            "entrycontent": entrycontent
        })