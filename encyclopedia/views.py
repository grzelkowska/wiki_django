import random
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from markdown2 import Markdown

from . import util

markdowner = Markdown()


def index(request):
    # if request.method == "POST":
    #     results = []
    #     possibles = []
    #     searched = request.POST["q"]
    #     for e in util.list_entries():
    #         if searched.lower() in e.lower():
    #             results.append(searched)
    #             possibles.append(e)
    #     if len(results) == 1 and results[0].lower() == possibles[0].lower():
    #         return render(request, "encyclopedia/title.html", {
    #             "title": possibles[0],
    #             "entry": util.get_entry(possibles[0])
    #         })
    #     return render(request, "encyclopedia/index.html", {
    #         "entries": possibles,
    #         "title": "Search Results"
    #     })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "title": "All Pages"
    })


def search(request):
    if request.method == "POST":
        results = []
        possibles = []
        searched = request.POST["q"]
        for e in util.list_entries():
            if searched.lower() in e.lower():
                results.append(searched)
                possibles.append(e)
        if len(results) == 1 and results[0].lower() == possibles[0].lower():
            return render(request, "encyclopedia/title.html", {
                "title": possibles[0],
                "entry": markdowner.convert(util.get_entry(possibles[0]))
            })
        return render(request, "encyclopedia/index.html", {
            "entries": possibles,
            "title": "Search Results"
        })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "title": "All Pages"
    })
        



def title(request, title_):

    if not util.get_entry(title_):
        return render(request, "encyclopedia/title.html", {
            "entry": f'"{title_}" does not exist'
        })

    return render(request, "encyclopedia/title.html", {
        "title": title_,
        "entry": markdowner.convert(util.get_entry(title_))
    })

    

def newpage(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']

        if util.get_entry(title):
            return render(request, "encyclopedia/newpage.html", {
                "message": "Entry already exists!"
            })

        util.save_entry(title, content)

        return HttpResponseRedirect(reverse("index"))

    return render(request, "encyclopedia/newpage.html")


def editpage(request, title):
    return render(request, "encyclopedia/editpage.html", {
        "title": title,
        "content": util.get_entry(title),
    })

def edit(request, title):
    if request.method == "POST":
        new_content = request.POST['content']
        util.save_entry(title, new_content)


    return HttpResponseRedirect(reverse('index'))


def randompage(request):
    random_list = util.list_entries()
    title = random.choice(random_list)
    content = util.get_entry(title)
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "entry": markdowner.convert(content)
    })
    

